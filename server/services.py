import re
import shortuuid
from decimal import Decimal
from datetime import datetime
from fastapi import APIRouter, Request, HTTPException
from src.logger import logger
from src.data_model import OrderCreate
from library.cache import save_service_cache, get_service_cache
from library.db import (session_scope, Users, Catalog as Cat, Category as Cgry, Services as Srv, Order, OrderItem,
                         UserAddress as UA, Professional as pf, receive_query)
router = APIRouter()

def slugify(text: str) -> str:
    """Convert title to frontend-friendly id"""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s]+", "_", text)

def build_category_response(catalog: str):
    categories_map = {}
    services = []

    with session_scope() as session:
        rows = receive_query(session.query(
                Cat.id, Cat.visit_fee, Cgry.category_name, Cgry.icon, Srv.id.label('service_id'), Srv.category_id, Srv.title,
                    Srv.price_min, Srv.price_max, Srv.duration_minutes,
                Srv.rating, Srv.review_count, Srv.pricing_note).join(
                    Cgry, Cgry.catalog_id == Cat.id
                    ).join(Srv, Srv.category_id == Cgry.id).filter(
                        Cat.catalog_name == catalog,
                        Cat.is_active == True,
                        Cgry.is_active == True,
                        Srv.is_active == True
                    ).order_by(Srv.id).all())

    for row in rows:
        cat_id = str(row["category_id"])

        # ---------- Build Categories (unique) ----------
        if cat_id not in categories_map:
            categories_map[cat_id] = {
                "id": cat_id,
                "name": row["category_name"],
                "icon": f'{row["icon"]}'
            }

        # ---------- Build Services ----------
        services.append({
            "id": str(row["service_id"]),
            "category_id": cat_id,
            "title": row["title"],
            "price_min": float(row["price_min"]) if isinstance(row["price_min"], Decimal) else row["price_min"],
            "price_max": float(row["price_max"]) if isinstance(row["price_max"], Decimal) else row["price_max"],
            # "visit_fee": float(row["visit_fee"]) if isinstance(row["visit_fee"], Decimal) else row["visit_fee"],
            "duration_minutes": row["duration_minutes"],
            "rating": float(row["rating"]) if isinstance(row["rating"], Decimal) else row["rating"],
            "review_count": row["review_count"],
            "variable_pricing": False if isinstance(row["price_max"], type(None)) else True,
            # "pricing_note": row["pricing_note"]
        })

    return {
        "category": catalog,
        "categories": list(categories_map.values()),
        "services": services
        # "visit_fee": 99,
        # "pricing_note": "Final price after inspection"
    }

@router.get("/services")
def get_services(request: Request, catalog: str | None= "electrician"):
    try:
        logger.info(f"Fetching services for category: {catalog}")
        logger.info(f"user request: {request.state.context}")
        # getting service details from cache
        data = get_service_cache(catalog)
        if data:
            return data
        data = build_category_response(catalog)
        logger.info(data)
        return data
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=500, detail="Something went wrong!")

@router.get("/set-service")
def set_services(request: Request, catalog: str | None= "electrician"):
    try:
        data = build_category_response(catalog)
        logger.info(f"Data availabe in db for redis: {True if data else False}")
        save_service_cache(catalog, data)
        return {"success": True}
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=500, detail="Something went wrong!")
        
@router.post("/orders/create")
def create_order(request: Request, order: OrderCreate):
    try:
        context = request.state.context
        logger.info(f"user request: {context['user']['user_id']}")
        with session_scope() as session:
            try:
                query = Order(
                    user_id=context['user']['user_id'],
                    address_id=order.address_id,
                    slot_type=order.slot_type,
                    scheduled_date=order.scheduled_date,
                    scheduled_time=order.scheduled_time,
                    tip_amount=order.tip_amount,
                    subtotal=order.total_amount,
                    taxes=9.00,
                    total_amount=order.total_amount,
                    payment_method=order.payment_method,
                    order_number = shortuuid.ShortUUID().random(length=8).upper()
                )
                session.add(query)
                session.flush()

                order_id = int(query.id)
                
                logger.info(f"order created: {order_id}")

                for service in order.services:
                    item = OrderItem(
                        order_id=order_id,
                        service_id=service.service_id,
                        quantity=service.quantity
                    )
                    session.add(item)
                
                session.commit()
            except Exception as ex:
                session.rollback()
                raise ValueError
        return {
            "success": True,
            "order_id": order_id,
            "message": "Order created successfully"
        }
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=500, detail="Something went wrong!")
    
@router.get("/orders/my-orders")
def get_orders(request: Request):
    try:
        context = request.state.context
        logger.info(f"user info: {context}")
        order_data = {
           "total_count": 2,
            "page": 1,
            "per_page": 10
        }
        order_arg = {}
        order_ids = set()

        with session_scope() as session:
            order_details = receive_query(session.query(
                Order.id.label("order_id"), Order.slot_type, Order.scheduled_date, Order.scheduled_time, 
                Order.total_amount,
                Order.order_status, Order.order_number, Order.professional_id, Order.created_on, 
                UA.flat, UA.society, UA.city
                ).join(UA, UA.address_id == Order.address_id
                ).filter(Order.user_id == context['user']['user_id'],
                         Order.is_active == True).all())
        
            logger.info(f"order details: \n{order_details}")

            for details in order_details:
                # Adding order_id in set for order items
                order_ids.add(details['order_id'])
                
                # order details
                order_arg[details['order_id']] = {
                    "order_id": details['order_id'],
                    "order_number": details['order_number'],
                    "created_on": details['created_on'].isoformat(),
                    "slot_type": details['slot_type'],
                    "scheduled_date": details["scheduled_date"].isoformat() if isinstance(details["scheduled_date"], datetime) else details["scheduled_date"],
                    "scheduled_time": details["scheduled_time"].isoformat() if isinstance(details["scheduled_time"], datetime) else details["scheduled_time"],
                    "status": details["order_status"],
                    # "payment_status": details["payment_status"],
                    # "payment_method": details["payment_method"],
                    # "address_city": details["city"],
                    "total_amount": float(details["total_amount"]),
                    "has_professional": True if details["professional_id"] is not None else False,
                    "address": {
                        "flat": details["flat"],
                        "society": details["society"],
                        "city": details["city"]
                    },
                    # "pricing": {
                    #     "subtotal": float(details["subtotal"]),
                    #     "visit_fee": float(details["visit_fee"]),
                    #     "taxes": float(details["taxes"]),
                    #     "tip_amount": float(details["tip_amount"]),
                    #     "total_amount": float(details["total_amount"])
                    # },
                    # "professional": {
                    #     "id": details["professional_id"],
                    #     "name": details["full_name"],
                    #     "phone": details["phone_number"],
                    #     "rating": float(details["rating"]) if isinstance(details["rating"], Decimal) else details["rating"],
                    #     "photo_url": details["photo_url"]
                    # },
                    "services": []
                }

            order_items = receive_query(session.query(
                OrderItem.service_id, Srv.title, OrderItem.quantity, Srv.price_min, Cgry.icon, OrderItem.order_id
            ).join(Srv, Srv.id == OrderItem.service_id).join( Cgry, Cgry.id == Srv.category_id
                ).filter(OrderItem.order_id.in_(list(order_ids))))

            for item in order_items:
                order_arg[item['order_id']]["services"].append({
                    # "service_id": item["service_id"],
                    "title": item["title"],
                    "quantity": item["quantity"],
                    # "price": float(item["price_min"]),
                    "category_icon": item["icon"]
                })
        order_data["orders"] = list(order_arg.values())
        logger.info("order information formatted!")
        return order_data
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=500, detail="Something went wrong!")
    
@router.get("/orders/{orderId}")
def get_order(request: Request, orderId: str):
    try:
        context = request.state.context
        with session_scope() as session:
            details = receive_query(session.query(
                Order.id.label("order_id"), Order.slot_type, Order.scheduled_date, Order.scheduled_time, Order.tip_amount, 
                Order.subtotal, Order.visit_fee, Order.taxes, Order.total_amount, Order.payment_method, Order.payment_status,
                Order.order_status, Order.order_number, Order.professional_id, Order.created_on, UA.address_id, UA.flat, UA.society, UA.landmark,
                UA.city, UA.state, UA.pincode, UA.phone,  Users.full_name, Users.phone_number, pf.rating, pf.photo_url
                ).join(UA, UA.address_id == Order.address_id
                ).outerjoin(pf, pf.id == Order.professional_id
                ).outerjoin(Users, Users.id == pf.id
                ).filter(Order.user_id == context['user']['user_id'],
                         Order.id == orderId,
                         Order.is_active == True).all())

            details = details[0]
            logger.info(f"order details: \n{details}")


            order_arg = {
                "order_id": details['order_id'],
                "order_number": details['order_number'],
                "created_on": details['created_on'].isoformat(),
                "slot_type": details['slot_type'],
                "scheduled_date": details["scheduled_date"].isoformat() if isinstance(details["scheduled_date"], datetime) else details["scheduled_date"],
                "scheduled_time": details["scheduled_time"].isoformat() if isinstance(details["scheduled_time"], datetime) else details["scheduled_time"],
                "status": details["order_status"],
                "payment_status": details["payment_status"],
                "payment_method": details["payment_method"],
                "address": {
                    "address_id": details["address_id"],
                    "flat": details["flat"],
                    "society": details["society"],
                    "landmark": details["landmark"],
                    "city": details["city"],
                    "state": details["state"],
                    "pincode": details["pincode"],
                    "phone": details["phone"]
                },
                "pricing": {
                    "subtotal": float(details["subtotal"]),
                    "visit_fee": float(details["visit_fee"]),
                    "taxes": float(details["taxes"]),
                    "tip_amount": float(details["tip_amount"]),
                    "total_amount": float(details["total_amount"])
                },
                "professional": {
                    "id": details["professional_id"],
                    "name": details["full_name"],
                    "phone": details["phone_number"],
                    "rating": float(details["rating"]) if isinstance(details["rating"], Decimal) else details["rating"],
                    "photo_url": details["photo_url"]
                },
                "services": []
            }

            order_items = receive_query(session.query(
                OrderItem.service_id, Srv.title, OrderItem.quantity, Srv.price_min, Cgry.icon, OrderItem.order_id
            ).join(Srv, Srv.id == OrderItem.service_id).join( Cgry, Cgry.id == Srv.category_id
                ).filter(OrderItem.order_id == orderId))

            for item in order_items:
                order_arg["services"].append({
                    "service_id": item["service_id"],
                    "title": item["title"],
                    "quantity": item["quantity"],
                    "price": float(item["price_min"]),
                    "category_icon": item["icon"]
                })
        logger.info("order information formatted!")
        return order_arg
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=500, detail="Something went wrong!")


@router.delete("/orders/{orderId}")
def cancel_order(request: Request, orderId: str):
    try:
        context = request.state.context
        logger.info(f"user context: {context}")
        logger.info("order ID: {orderId} to delete")
        return {
            "success": True,
            "order_id": orderId,
            "message": "Order deleted successfully"
        }
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=500, detail="Something went wrong!")
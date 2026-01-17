import re
from decimal import Decimal
from fastapi import APIRouter, Request, HTTPException
from src.logger import logger

from library.db import session_scope, Category as Cat, SubCategory as SubCat, Services as Srv, receive_query

router = APIRouter()

def slugify(text: str) -> str:
    """Convert title to frontend-friendly id"""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s]+", "_", text)

def build_category_response(category_name: str, rows: list[dict]):
    categories_map = {}
    services = []

    for row in rows:
        sub_cat_id = str(row["sub_category_id"])

        # ---------- Build Categories (unique) ----------
        if sub_cat_id not in categories_map:
            categories_map[sub_cat_id] = {
                "id": sub_cat_id,
                "name": row["name"],
                "icon": f'{row["icon"]}'
            }

        # ---------- Build Services ----------
        services.append({
            "id": str(row["service_id"]),
            "category_id": sub_cat_id,
            "title": row["title"],
            "price": float(row["price"]) if isinstance(row["price"], Decimal) else row["price"],
            "duration_minutes": row["duration_minutes"],
            "rating": float(row["rating"]) if isinstance(row["rating"], Decimal) else row["rating"],
            "review_count": row["review_count"]
        })

    return {
        "category": category_name,
        "categories": list(categories_map.values()),
        "services": services
    }

@router.get("/services")
def get_services(request: Request, category: str | None= "electrician"):
    try:
        logger.info(f"Fetching services for category: {category}")
        logger.info(f"user request: {request.state.context}")
        with session_scope() as session:
            data = receive_query(session.query(
                   Cat.id, SubCat.name, SubCat.icon, Srv.id.label('service_id'), Srv.sub_category_id, Srv.title,
                     Srv.price, Srv.duration_minutes,
                   Srv.rating, Srv.review_count).join(
                        SubCat, SubCat.category_id == Cat.id
                        ).join(Srv, Srv.sub_category_id == SubCat.id).filter(
                            Cat.category_name == category,
                            Cat.is_active == True,
                            SubCat.is_active == True,
                            Srv.is_active == True
                        ).all())
            data = build_category_response(category, data)
            logger.info(data)
        # data = {
        #     "category": "electrician",
        #     "categories": [
        #         {
        #         "id": "switch_socket",
        #         "name": "Switch & Socket",
        #         "icon": "switch.png"
        #         },
        #         {
        #         "id": "fan",
        #         "name": "Fan",
        #         "icon": "fan.png"
        #         },
        #         {
        #         "id": "light",
        #         "name": "Light",
        #         "icon": "light.png"
        #         },
        #         {
        #         "id": "wiring",
        #         "name": "Wiring",
        #         "icon": "wiring.png"
        #         },
        #         {
        #         "id": "doorbell_security",
        #         "name": "Doorbell & Security",
        #         "icon": "doorbell.png"
        #         },
        #         {
        #         "id": "mcb_fuse",
        #         "name": "MCB/Fuse",
        #         "icon": "Mcb.png"
        #         },
        #         {
        #         "id": "appliances",
        #         "name": "Appliances",
        #         "icon": "appliance.png"
        #         },
        #         {
        #         "id": "consultation",
        #         "name": "Book a consultation",
        #         "icon": "engineer.png"
        #         }
        #     ],
        #     "services": [
        #         {
        #         "id": "switch_repair",
        #         "category_id": "switch_socket",
        #         "title": "Switch/Socket Repair",
        #         "price": 69,
        #         "duration_minutes": 20,
        #         "rating": 4.8,
        #         "review_count": 980
        #         },
        #         {
        #         "id": "switchboard_repair",
        #         "category_id": "switch_socket",
        #         "title": "Switchboard Repair",
        #         "price": 69,
        #         "duration_minutes": 20,
        #         "rating": 4.8,
        #         "review_count": 980
        #         },
        #         {
        #         "id": "plug_replacement",
        #         "category_id": "switch_socket",
        #         "title": "Plug replacement",
        #         "price": 69,
        #         "duration_minutes": 20,
        #         "rating": 4.8,
        #         "review_count": 980
        #         },
        #         {
        #         "id": "switchbox_installation",
        #         "category_id": "switch_socket",
        #         "title": "New switchbox installation",
        #         "price": 69,
        #         "duration_minutes": 20,
        #         "rating": 4.8,
        #         "review_count": 980
        #         },
        #         {
        #         "id": "fan_installation",
        #         "category_id": "fan",
        #         "title": "Fan Installation/Uninstallation",
        #         "price": 149,
        #         "duration_minutes": 30,
        #         "rating": 4.7,
        #         "review_count": 1250
        #         },
        #         {
        #         "id": "fan_repair",
        #         "category_id": "fan",
        #         "title": "Fan repair",
        #         "price": 149,
        #         "duration_minutes": 30,
        #         "rating": 2.8,
        #         "review_count": 1250
        #         },
        #         {
        #         "id": "exhaust_installation",
        #         "category_id": "fan",
        #         "title": "Exhaust/pedestal/tower fan Installation",
        #         "price": 69,
        #         "duration_minutes": 20,
        #         "rating": 4.8,
        #         "review_count": 980
        #         },
        #         {
        #         "id": "regulator_replacement",
        #         "category_id": "fan",
        #         "title": "fan regulator replacement",
        #         "price": 69,
        #         "duration_minutes": 20,
        #         "rating": 4.8,
        #         "review_count": 980
        #         },
        #         {
        #         "id": "tubelight_installation",
        #         "category_id": "light",
        #         "title": "Tubelight repair & installation",
        #         "price": 69,
        #         "duration_minutes": 20,
        #         "rating": 4.8,
        #         "review_count": 980
        #         },
        #         {
        #         "id": "blub_holder_replacement",
        #         "category_id": "light",
        #         "title": "Buld holder replacement",
        #         "price": 69,
        #         "duration_minutes": 20,
        #         "rating": 4.8,
        #         "review_count": 980
        #         },
        #         {
        #         "id": "blub_holder_replacement",
        #         "category_id": "light",
        #         "title": "Buld holder replacement",
        #         "price": 69,
        #         "duration_minutes": 20,
        #         "rating": 4.8,
        #         "review_count": 980
        #         }
        #     ]
        #     }
        return data
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=500, detail="Something went wrong!")

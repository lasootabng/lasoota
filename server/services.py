import re
from decimal import Decimal
from fastapi import APIRouter, Request, HTTPException
from src.logger import logger

from library.db import session_scope, Catalog as Cat, Category as Cgry, Services as Srv, receive_query

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
            "visit_fee": float(row["visit_fee"]) if isinstance(row["visit_fee"], Decimal) else row["visit_fee"],
            "duration_minutes": row["duration_minutes"],
            "rating": float(row["rating"]) if isinstance(row["rating"], Decimal) else row["rating"],
            "review_count": row["review_count"],
            "variable_pricing": False if isinstance(row["price_max"], type(None)) else True,
            "pricing_note": row["pricing_note"]
        })

    return {
        "category": category_name,
        "categories": list(categories_map.values()),
        "services": services
    }

@router.get("/services")
def get_services(request: Request, catalog: str | None= "electrician"):
    try:
        logger.info(f"Fetching services for category: {catalog}")
        logger.info(f"user request: {request.state.context}")
        with session_scope() as session:
            data = receive_query(session.query(
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
            data = build_category_response(catalog, data)
            logger.info(data)
        return data
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=500, detail="Something went wrong!")

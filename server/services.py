from fastapi import APIRouter, Request, HTTPException
from src.logger import logger

router = APIRouter()

@router.get("/services")
def get_services(request: Request, category: str | None= "electrician"):
    try:
        logger.info(f"Fetching services for category: {category}")
        logger.info(f"user request: {request.state.context}")
        data = {
            "category": "electrician",
            "categories": [
                {
                "id": "switch_socket",
                "name": "Switch & Socket",
                "icon": "switch.png"
                },
                {
                "id": "fan",
                "name": "Fan",
                "icon": "fan.png"
                },
                {
                "id": "light",
                "name": "Light",
                "icon": "light.png"
                },
                {
                "id": "wiring",
                "name": "Wiring",
                "icon": "wiring.png"
                },
                {
                "id": "doorbell_security",
                "name": "Doorbell & Security",
                "icon": "doorbell.png"
                },
                {
                "id": "mcb_fuse",
                "name": "MCB/Fuse",
                "icon": "Mcb.png"
                },
                {
                "id": "appliances",
                "name": "Appliances",
                "icon": "appliance.png"
                },
                {
                "id": "consultation",
                "name": "Book a consultation",
                "icon": "engineer.png"
                }
            ],
            "services": [
                {
                "id": "switch_repair",
                "category_id": "switch_socket",
                "title": "Switch/Socket Repair",
                "price": 69,
                "duration_minutes": 20,
                "rating": 4.8,
                "review_count": 980
                },
                {
                "id": "switchboard_repair",
                "category_id": "switch_socket",
                "title": "Switchboard Repair",
                "price": 69,
                "duration_minutes": 20,
                "rating": 4.8,
                "review_count": 980
                },
                {
                "id": "plug_replacement",
                "category_id": "switch_socket",
                "title": "Plug replacement",
                "price": 69,
                "duration_minutes": 20,
                "rating": 4.8,
                "review_count": 980
                },
                {
                "id": "switchbox_installation",
                "category_id": "switch_socket",
                "title": "New switchbox installation",
                "price": 69,
                "duration_minutes": 20,
                "rating": 4.8,
                "review_count": 980
                },
                {
                "id": "fan_installation",
                "category_id": "fan",
                "title": "Fan Installation/Uninstallation",
                "price": 149,
                "duration_minutes": 30,
                "rating": 4.7,
                "review_count": 1250
                },
                {
                "id": "fan_repair",
                "category_id": "fan",
                "title": "Fan repair",
                "price": 149,
                "duration_minutes": 30,
                "rating": 2.8,
                "review_count": 1250
                },
                {
                "id": "exhaust_installation",
                "category_id": "fan",
                "title": "Exhaust/pedestal/tower fan Installation",
                "price": 69,
                "duration_minutes": 20,
                "rating": 4.8,
                "review_count": 980
                },
                {
                "id": "regulator_replacement",
                "category_id": "fan",
                "title": "fan regulator replacement",
                "price": 69,
                "duration_minutes": 20,
                "rating": 4.8,
                "review_count": 980
                },
                {
                "id": "tubelight_installation",
                "category_id": "light",
                "title": "Tubelight repair & installation",
                "price": 69,
                "duration_minutes": 20,
                "rating": 4.8,
                "review_count": 980
                },
                {
                "id": "blub_holder_replacement",
                "category_id": "light",
                "title": "Buld holder replacement",
                "price": 69,
                "duration_minutes": 20,
                "rating": 4.8,
                "review_count": 980
                }
            ]
            }
        return data
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=500, detail="Something went wrong!")

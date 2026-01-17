from fastapi import APIRouter, Request, HTTPException
from src.logger import logger
from library.db import session_scope, receive_query, ServiceCategory as Cat, SubCategory as SubCat

router = APIRouter()



@router.get("/home")
def home_page(request: Request):
    try:
        mapping = {
            "slides": [],
            "categories": [],
            "footer": {}
        }
        context = request.state.context
        logger.info(context)
        
        with session_scope() as session:
            data = receive_query(session.query(
                Cat.category_name, Cat.category_order, Cat.service_image).filter(Cat.is_active == True).order_by(Cat.category_order).all())
            
            mapping['categories'] = data

        return mapping
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=401, detail="User account is not active")
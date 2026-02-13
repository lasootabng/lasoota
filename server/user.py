from fastapi import APIRouter, Request, HTTPException
from datetime import datetime
from src.logger import logger
# from src.constants import response_formatter
from src.data_model import UserAddress, RemoveAddress, UpdateAddress, UpdateUser
from library.db import session_scope, Users, UserAddress as UA, receive_query

router = APIRouter()

@router.get("/get-user")
def get_user(request: Request):
    try:
        context = request.state.context
        logger.info(f"user info: {context}")
        with session_scope() as session:
            user_data = receive_query(session.query(Users.full_name, Users.email, Users.phone_number, Users.role_type
                                                    ).filter(Users.phone_number == context['user']['phone']).all())
        if user_data:
            user_data = user_data[0]
        else:
            raise HTTPException(status_code=401, detail="UnAuthorized!")
        logger.info(f"users Data: {user_data}")
        return user_data
    except Exception as ex:
        logger.exception(ex)

@router.put("/update-user")
async def register_user(request: Request, user: UpdateUser):

    try:
        context = request.state.context

        logger.info(f"User Context: {context}")

        # check user phone is already registered or not
        with session_scope() as session:
            session.query(Users).filter(Users.id==context['user']['user_id']).update({
                    Users.full_name: user.full_name,
                    Users.email: user.email,
                    # Users.phone_number: user.phone
                })
            session.commit()
            logger.info("user details updated")
        return {"success": True}
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=500, detail="something wents wrong!")
        # return {"success": False}


@router.get("/get-address")
def get_address(request: Request):
    try:
        context = request.state.context
        logger.info(f"user context: {context}")
        with session_scope() as session:
            address_data = receive_query(
                session.query(UA.address_id, UA.flat, UA.society, UA.landmark, UA.city, UA.state, UA.pincode, UA.phone
                                 ).join(Users, UA.user_id == Users.id).filter(Users.phone_number == context['user']['phone']).filter(UA.is_active==True).all())
            logger.info(address_data)
        return address_data
    except Exception as ex:
        logger.exception(ex)


@router.post("/add-address")
def add_address(request: Request, address: UserAddress):
    try:
        context = request.state.context
        logger.info(f"user context: {context['user']['user_id']}")
        logger.info(f"user address: {address}")
        with session_scope() as session:
            query = UA(
                user_id=context['user']['user_id'],
                flat = address.flat,
                society = address.society,
                landmark = address.landmark,
                city = address.city,
                state = address.state,
                pincode = address.pincode,
                phone = address.phone,
                latitude = address.latitude,
                longitude = address.longitude
                # location = f'POINT({address.longitude} {address.latitude})'
            )
            session.add(query)
            session.commit()

        logger.info("Address Added!")
        return {"success": True}
    except Exception as ex:
        logger.exception(ex)
        raise HTTPException(status_code=500, detail="something wents wrong!")
        # return {"success": False}


@router.delete("/delete-address")
def delete_address(request: Request, address: RemoveAddress):
    try:
        context = request.state.context
        logger.info(context)
        logger.info(f"Address id: {address.address_id}")
        with session_scope() as session:
            session.query(UA).filter(UA.address_id==address.address_id).update({
                UA.is_active: False,
                UA.updated_on:datetime.now()
            })
            session.commit()
            logger.info("address updated")
        return {"success": True}
    except Exception as ex:
        logger.exception(ex)
        return {"success": "False"}
    
@router.put("/update-address")
def update_address(request: Request, address: UpdateAddress):
    try:
        logger.info(address.address_id)
        with session_scope() as session:
            session.query(UA).filter(UA.address_id==address.address_id).update({
                UA.flat: address.flat,
                UA.society:address.society,
                UA.landmark:address.landmark,
                UA.phone:address.phone,
                UA.updated_on:datetime.now()
            })
            session.commit()
            logger.info("address updated")
        return {"success": True}
    except Exception as ex:
        logger.exception(ex)
        return {"success": False}
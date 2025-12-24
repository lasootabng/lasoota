from typing import Annotated
from fastapi import APIRouter, Request, Body
from src.data_model import ContactUS
from src.logger import logger
# from src.constants import response_formatter

router = APIRouter()


@router.post("/contact-us")
def contact_us(request: Request, data: Annotated[ContactUS, Body(embed=True)]):
    context = request.state.context
    user_id = context['phone']
    logger.info(f"user request: {user_id} - comment: {data.comment}")
    return {"message": "we will contact you soon!"}

@router.get("/about-us")
def about_us():
    about_html = """
        <div style="width: 95%; margin: 0 auto; font-size: 2.4em;">
            <article style="background: white; padding: 20px; margin: 20px 0">
                <section style="text-align: left; background: #fff; color: #1a71b8; padding: 10px">
                    <h2>About Us</h2>
                </section>
                <section style="margin: 0 0 20px;">
                    <p style="margin: 0 0 1em; font-family: Georgia, Times, serif; text-align:justify; text-justify:inter-word;">
                        Our venture is a digital platform designed to connect local service providers directly with customers. 
                        Established with the motto - <strong>'Empowering local talent, building lasting trust'</strong>, we aim to create 
                        value for both professionals and households. 
                        <br /><br />
                        Whether you are an electrician, plumber, carpenter, or any skilled worker, our platform enables you to 
                        list your services and reach customers in need, without middlemen or hidden costs. Customers can browse, 
                        compare, and hire trusted providers with unmatched convenience. 
                        <br /><br />
                        We firmly believe that trust and transparency are the foundation of profitable and sustainable businesses. 
                        By offering fair pricing, verified listings, and seamless communication, we bring confidence and efficiency 
                        to every service interaction. 
                        <br /><br />
                        We shall continue to innovate and discover efficient ways to create value for our customers, service providers, 
                        and the community - saving time, money, and building stronger local connections.
                    </p>
                </section>
            </article>		
        </div>
    """
    logger.info(f"someone called about us page!")

    return about_html

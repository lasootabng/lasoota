from fastapi import FastAPI
from services import api_router, basic_router
from fastapi.middleware.cors import CORSMiddleware 


app = FastAPI(
    title="freelancer engine",
    description=""" This **freelancer-engine** is like online superhero 🦸‍♂️<br />
    Taking care of all the GPT and AI stuff, so you can focus on making your chat ideas
      come to life 🌱<br />
    So, grab your coding cape and join the fun! Our Chat Service is here to make your development
      journey super exciting and full of learnings 🔭""",
    version="0.0.1",
    contact={
        "name": ":-  Bipul Kumar Singh",
        "email": "bipulsinghkashyap@gmail.com"
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.api_route("/freelance_health", methods=["GET", "POST"], tags=["Freelance Health"])
async def freelance_health():
    return {"status": "ok", "message": "Bihar services API is running!"}


app.include_router(basic_router)
app.include_router(api_router)

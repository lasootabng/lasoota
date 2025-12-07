from fastapi import FastAPI
from services import api_router


app = FastAPI(
    title="freelancer engine",
    description=""" This **freelancer-engine** is like online superhero 🦸‍♂️<br />
    Taking care of all the GPT and AI stuff, so you can focus on making your chat ideas
      come to life 🌱<br />
    So, grab your coding cape and join the fun! Our Chat Service is here to make your development
      journey super exciting and full of learnings 🔭""",
    version="0.1",
    contact={
        "name": ":-  Bipul Kumar Singh",
        "email": "bipulsinghkashyap@gmail.com"
    },
    docs_url="/freelancer-documentation",
    redoc_url=None,
    openapi_url=None
)

@app.api_route("/health", methods=["GET", "POST"], tags=["Health"])
async def health():
    return {"status": "ok", "message": "Bihar services API is running!"}


app.include_router(api_router)

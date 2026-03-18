from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.src.home import home 
from app.src.times import router
from app.src.infra.database import Base, engine
from app.src.models import times 

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(home)
app.include_router(router)
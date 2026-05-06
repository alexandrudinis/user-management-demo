from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.main_router import router
from app.database import Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as necessary
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)  # Assuming 'engine' is defined in your database settings

app.include_router(router)
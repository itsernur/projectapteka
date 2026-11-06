import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import medicines, pharmacies

load_dotenv()

app = FastAPI(
    title="Pharmacy Chain API",
    description="Наличие лекарств в аптеках сети",
    version="0.1.0",
)

# Адреса фронтенда, которым разрешено обращаться к API
origins = [
    o.strip()
    for o in os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:5173").split(",")
    if o.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pharmacies.router)
app.include_router(medicines.router)


@app.get("/", tags=["health"])
def root():
    return {"status": "ok", "docs": "/docs"}

from fastapi import APIRouter, HTTPException, Query

from app.schemas.models import Pharmacy
from app.services import catalog

router = APIRouter(prefix="/api/pharmacies", tags=["pharmacies"])


@router.get("", response_model=list[Pharmacy])
def list_pharmacies(city: str | None = Query(None, description="Фильтр по городу")):
    return catalog.list_pharmacies(city)


@router.get("/{pharmacy_id}", response_model=Pharmacy)
def get_pharmacy(pharmacy_id: int):
    pharmacy = catalog.get_pharmacy(pharmacy_id)
    if pharmacy is None:
        raise HTTPException(status_code=404, detail="Аптека не найдена")
    return pharmacy

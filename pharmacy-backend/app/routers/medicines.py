from fastapi import APIRouter, HTTPException, Query

from app.schemas.models import Medicine, MedicineAvailability
from app.services import catalog

router = APIRouter(prefix="/api/medicines", tags=["medicines"])


@router.get("", response_model=list[Medicine])
def search_medicines(
    search: str | None = Query(None, description="Название или действующее вещество"),
    prescription_required: bool | None = Query(None, description="Только рецептурные / безрецептурные"),
):
    return catalog.search_medicines(search, prescription_required)


@router.get("/{medicine_id}", response_model=Medicine)
def get_medicine(medicine_id: int):
    medicine = catalog.get_medicine(medicine_id)
    if medicine is None:
        raise HTTPException(status_code=404, detail="Препарат не найден")
    return medicine


@router.get("/{medicine_id}/availability", response_model=MedicineAvailability)
def get_availability(
    medicine_id: int,
    city: str | None = Query(None, description="Фильтр по городу"),
    in_stock_only: bool = Query(False, description="Только аптеки, где препарат есть"),
):
    result = catalog.get_availability(medicine_id, city, in_stock_only)
    if result is None:
        raise HTTPException(status_code=404, detail="Препарат не найден")
    return result

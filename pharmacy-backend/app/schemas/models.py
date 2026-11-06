from datetime import datetime

from pydantic import BaseModel, Field


class Pharmacy(BaseModel):
    id: int
    name: str
    city: str
    address: str
    phone: str
    hours: str
    lat: float
    lng: float


class Medicine(BaseModel):
    id: int
    name: str
    inn: str  # МНН, действующее вещество
    form: str
    manufacturer: str
    prescription_required: bool
    description: str


class StockItem(BaseModel):
    pharmacy_id: int
    medicine_id: int
    quantity: int = Field(ge=0)
    price: float = Field(ge=0)


class PharmacyAvailability(BaseModel):
    """Одна аптека и наличие в ней конкретного препарата."""

    pharmacy_id: int
    name: str
    city: str
    address: str
    phone: str
    hours: str
    lat: float
    lng: float
    quantity: int
    price: float
    in_stock: bool
    updated_at: datetime | None = None


class MedicineAvailability(BaseModel):
    medicine: Medicine
    pharmacies: list[PharmacyAvailability]

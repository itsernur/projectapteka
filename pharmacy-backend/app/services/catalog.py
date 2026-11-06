"""Бизнес-логика: поиск препаратов и расчёт наличия по аптекам."""

from app.schemas.models import (
    Medicine,
    MedicineAvailability,
    Pharmacy,
    PharmacyAvailability,
)
from app.storage import files


def _normalize(text: str) -> str:
    return text.casefold().strip()


def search_medicines(
    query: str | None = None,
    prescription_required: bool | None = None,
) -> list[Medicine]:
    """Поиск по названию и действующему веществу, без учёта регистра."""
    result = files.get_medicines()

    if query:
        q = _normalize(query)
        result = [
            m for m in result
            if q in _normalize(m.name) or q in _normalize(m.inn)
        ]

    if prescription_required is not None:
        result = [m for m in result if m.prescription_required == prescription_required]

    return result


def get_medicine(medicine_id: int) -> Medicine | None:
    return next((m for m in files.get_medicines() if m.id == medicine_id), None)


def list_pharmacies(city: str | None = None) -> list[Pharmacy]:
    result = files.get_pharmacies()
    if city:
        c = _normalize(city)
        result = [p for p in result if _normalize(p.city) == c]
    return result


def get_pharmacy(pharmacy_id: int) -> Pharmacy | None:
    return next((p for p in files.get_pharmacies() if p.id == pharmacy_id), None)


def get_availability(
    medicine_id: int,
    city: str | None = None,
    in_stock_only: bool = False,
) -> MedicineAvailability | None:
    """Где и сколько есть препарата. None, если такого препарата нет."""
    medicine = get_medicine(medicine_id)
    if medicine is None:
        return None

    pharmacies = {p.id: p for p in list_pharmacies(city)}
    updated_at = files.get_stock_updated_at()

    rows: list[PharmacyAvailability] = []
    for item in files.get_stock():
        if item.medicine_id != medicine_id:
            continue
        pharmacy = pharmacies.get(item.pharmacy_id)
        if pharmacy is None:
            continue
        if in_stock_only and item.quantity == 0:
            continue
        rows.append(
            PharmacyAvailability(
                pharmacy_id=pharmacy.id,
                name=pharmacy.name,
                city=pharmacy.city,
                address=pharmacy.address,
                phone=pharmacy.phone,
                hours=pharmacy.hours,
                lat=pharmacy.lat,
                lng=pharmacy.lng,
                quantity=item.quantity,
                price=item.price,
                in_stock=item.quantity > 0,
                updated_at=updated_at,
            )
        )

    # Сначала аптеки, где препарат есть, затем по возрастанию цены
    rows.sort(key=lambda r: (not r.in_stock, r.price))
    return MedicineAvailability(medicine=medicine, pharmacies=rows)

"""Слой доступа к данным.

Весь код, который читает файлы из папки data/, находится только здесь.
Остальное приложение работает через эти функции, поэтому позже способ
хранения можно заменить, не переписывая роутеры и сервисы.
"""

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

from app.schemas.models import Medicine, Pharmacy, StockItem

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
PHARMACIES_FILE = DATA_DIR / "pharmacies.json"
MEDICINES_FILE = DATA_DIR / "medicines.json"
STOCK_FILE = DATA_DIR / "stock.csv"


def get_pharmacies() -> list[Pharmacy]:
    with PHARMACIES_FILE.open(encoding="utf-8") as f:
        return [Pharmacy(**item) for item in json.load(f)]


def get_medicines() -> list[Medicine]:
    with MEDICINES_FILE.open(encoding="utf-8") as f:
        return [Medicine(**item) for item in json.load(f)]


def get_stock() -> list[StockItem]:
    with STOCK_FILE.open(encoding="utf-8", newline="") as f:
        return [
            StockItem(
                pharmacy_id=int(row["pharmacy_id"]),
                medicine_id=int(row["medicine_id"]),
                quantity=int(row["quantity"]),
                price=float(row["price"]),
            )
            for row in csv.DictReader(f)
        ]


def get_stock_updated_at() -> datetime | None:
    """Время последнего изменения файла остатков."""
    if not STOCK_FILE.exists():
        return None
    return datetime.fromtimestamp(STOCK_FILE.stat().st_mtime, tz=timezone.utc)

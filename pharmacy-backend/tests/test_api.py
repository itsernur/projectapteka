"""Тесты HTTP-слоя. Нужен пакет httpx: pip install httpx"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_pharmacies_list():
    r = client.get("/api/pharmacies")
    assert r.status_code == 200
    assert len(r.json()) == 3


def test_medicine_not_found():
    r = client.get("/api/medicines/99999")
    assert r.status_code == 404


def test_availability_endpoint():
    r = client.get("/api/medicines/101/availability")
    assert r.status_code == 200
    body = r.json()
    assert body["medicine"]["id"] == 101
    assert len(body["pharmacies"]) == 3

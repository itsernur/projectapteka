"""Тесты бизнес-логики. Запуск: pytest"""

from app.services import catalog


def test_search_by_name_case_insensitive():
    result = catalog.search_medicines("ПАРАЦЕТАМОЛ")
    assert [m.id for m in result] == [101]


def test_search_by_inn():
    result = catalog.search_medicines("ацетилсалициловая")
    assert [m.id for m in result] == [107]


def test_search_prescription_filter():
    result = catalog.search_medicines(prescription_required=True)
    assert {m.id for m in result} == {103, 108}


def test_pharmacies_city_filter():
    result = catalog.list_pharmacies("алматы")
    assert {p.id for p in result} == {1, 2}


def test_availability_sorted_by_price():
    result = catalog.get_availability(101)
    assert result is not None
    assert [r.pharmacy_id for r in result.pharmacies] == [3, 1, 2]  # по возрастанию цены
    assert all(r.in_stock for r in result.pharmacies)


def test_availability_in_stock_only():
    result = catalog.get_availability(102, in_stock_only=True)
    assert [r.pharmacy_id for r in result.pharmacies] == [2]


def test_availability_unknown_medicine():
    assert catalog.get_availability(99999) is None


def test_availability_city_filter():
    result = catalog.get_availability(101, city="Астана")
    assert [r.pharmacy_id for r in result.pharmacies] == [3]

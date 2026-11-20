"""API tests — run with: pytest -q"""
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_create_and_read_round_trip():
    r = client.post(
        "/readings",
        json={"sensor_id": "temp-01", "value": 21.5, "unit": "C"},
    )
    assert r.status_code == 201
    created = r.json()
    assert created["sensor_id"] == "temp-01"
    assert created["id"] > 0

    r = client.get(f"/readings/{created['id']}")
    assert r.status_code == 200
    assert r.json()["value"] == 21.5


def test_get_missing_returns_404():
    r = client.get("/readings/999999")
    assert r.status_code == 404


def test_filter_by_sensor_id():
    r = client.get("/readings", params={"sensor_id": "temp-01"})
    assert r.status_code == 200
    readings = r.json()
    assert len(readings) > 0
    assert all(x["sensor_id"] == "temp-01" for x in readings)


def test_filter_by_min_value():
    r = client.get("/readings", params={"min_value": 20})
    assert r.status_code == 200
    readings = r.json()
    assert len(readings) > 0
    assert all(x["value"] >= 20 for x in readings)


def test_filter_by_max_value():
    r = client.get("/readings", params={"max_value": 20})
    assert r.status_code == 200
    readings = r.json()
    assert len(readings) > 0
    assert all(x["value"] <= 20 for x in readings)


def test_filter_combined_sensor_and_min_value():
    r = client.get("/readings", params={"sensor_id": "temp-01", "min_value": 20})
    assert r.status_code == 200
    readings = r.json()
    assert len(readings) > 0
    assert all(x["sensor_id"] == "temp-01" and x["value"] >= 20 for x in readings)


def test_filter_unknown_sensor_returns_empty_list():
    r = client.get("/readings", params={"sensor_id": "nope"})
    assert r.status_code == 200
    assert r.json() == []


def test_create_missing_value_returns_422():
    r = client.post("/readings", json={"sensor_id": "temp-01", "unit": "C"})
    assert r.status_code == 422


def test_create_missing_sensor_id_returns_422():
    r = client.post("/readings", json={"value": 22.0, "unit": "C"})
    assert r.status_code == 422


def test_create_value_wrong_type_returns_422():
    r = client.post("/readings", json={"sensor_id": "temp-01", "value": "abc", "unit": "C"})
    assert r.status_code == 422


def test_create_sensor_id_too_short_returns_422():
    r = client.post("/readings", json={"sensor_id": "ab", "value": 22.0, "unit": "C"})
    assert r.status_code == 422


def test_create_sensor_id_too_long_returns_422():
    r = client.post("/readings", json={"sensor_id": "temperature-sensor-01", "value": 22.0, "unit": "C"})
    assert r.status_code == 422


def test_create_sensor_id_bad_characters_returns_422():
    for bad_id in ["Temp-01", "temp 01", "temp-01 "]:
        r = client.post("/readings", json={"sensor_id": bad_id, "value": 22.0, "unit": "C"})
        assert r.status_code == 422


def test_get_non_integer_id_returns_422():
    r = client.get("/readings/abc")
    assert r.status_code == 422


def test_get_bad_min_value_returns_422():
    r = client.get("/readings", params={"min_value": "abc"})
    assert r.status_code == 422


def test_delete_missing_returns_404():
    r = client.delete("/readings/999999")
    assert r.status_code == 404


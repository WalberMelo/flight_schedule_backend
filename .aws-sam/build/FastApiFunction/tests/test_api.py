from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

mock_flights = [
        {
            "flight_date": "2025-06-09",
            "flight_status": "scheduled",
            "departure": {
                "airport": "Hyderabad Airport",
                "timezone": "Asia/Kolkata",
                "iata": "HYD",
                "icao": "VOHS",
                "terminal": None,
                "gate": "26B",
                "baggage": None,
                "delay": None,
                "scheduled": "2025-06-09T01:10:00+00:00",
                "estimated": "2025-06-09T01:10:00+00:00",
                "actual": None,
                "estimated_runway": None,
                "actual_runway": None,
            },
            "arrival": {
                "airport": "Suvarnabhumi International",
                "timezone": "Asia/Bangkok",
                "iata": "BKK",
                "icao": "VTBS",
                "terminal": None,
                "gate": None,
                "baggage": None,
                "delay": None,
                "scheduled": "2025-06-09T06:15:00+00:00",
                "estimated": None,
                "actual": None,
                "estimated_runway": None,
                "actual_runway": None,
            },
            "airline": {
                "name": "ANA",
                "iata": "NH",
                "icao": "ANA",
            },
            "flight": {
                "number": "5988",
                "iata": "NH5988",
                "icao": "ANA5988",
                "codeshared": {
                    "airline_name": "thai airways international",
                    "airline_iata": "tg",
                    "airline_icao": "tha",
                    "flight_number": "330",
                    "flight_iata": "tg330",
                    "flight_icao": "tha330",
                },
            },
            "aircraft": None,
            "live": None,
        },
    ]

def test_get_flights_mock(monkeypatch):
    """Test the /api/flights endpoint with mocked flight data"""

    async def mock_fetch(*args, **kwargs):
         return {
            "data": mock_flights,
            "pagination": {
                "limit": 10,
                "offset": 0,
                "count": len(mock_flights),
                "total": 1
            },
         }

    monkeypatch.setattr("app.routers.flights.fetch_flights", mock_fetch)

    response = client.get("/api/flights?city=Barcelona&limit=10&offset=0")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) == 1
    assert data["data"][0]["flight"]["number"] == "5988"

def test_get_flights_empty_response(monkeypatch):
    """Test the /api/flights endpoint with an empty response"""
    
    async def mock_fetch_empty(*args, **kwargs):
          return {
            "data": [],
            "pagination": {
                "limit": 10,
                "offset": 0,
                "count": 0,
                "total": 0
            }
        }

    monkeypatch.setattr("app.routers.flights.fetch_flights",mock_fetch_empty)

    response = client.get("/api/flights?limit=10&offset=0")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) == 0

def test_get_flights_invalid_parameters():
    """Test the /api/flights endpoint with invalid parameters"""
    
    # Test with invalid limit (negative)
    response = client.get("/api/flights?limit=-5&offset=0")
    assert response.status_code == 422  
    
    # Test with invalid limit (too large)
    response = client.get("/api/flights?limit=200&offset=0")
    assert response.status_code == 422  
    
    # Test with invalid offset (negative)
    response = client.get("/api/flights?limit=10&offset=-5")
    assert response.status_code == 422 
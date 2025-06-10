
import httpx
from app.core.config import settings

async def fetch_flights(city: str | None, limit: int, offset: int):
    url = "http://api.aviationstack.com/v1/flights"
    params = {
        "access_key": settings.AVIATIONSTACK_KEY,
        "dep_city": city,
        "limit": limit,
        "offset": offset
    }
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        data = resp.json()
        
        return {
            "pagination": data.get("pagination", {}),
            "data": data.get("data", [])
        }
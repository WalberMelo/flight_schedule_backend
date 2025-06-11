
import httpx
from app.core.config import settings
from app.utils.secrets import get_secrets

async def fetch_flights(city: str | None, limit: int, offset: int):
    aviationstack_key = get_secrets()[1]

    url = "http://api.aviationstack.com/v1/flights"
    params = {
        "access_key": aviationstack_key,
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
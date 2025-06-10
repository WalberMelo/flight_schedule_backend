from fastapi import APIRouter, Depends
from typing import Annotated
from app.models.schema import FlightFilter, FlightsResponse, FlightData
from app.services.flight_service import fetch_flights

router = APIRouter()

@router.get( "/flights",
    response_model=FlightsResponse,  
    summary="Get a list of flights by city",
    tags=["flights"],
)
async def get_flights(filters: Annotated[FlightFilter, Depends()]):
    result = await fetch_flights(filters.city, filters.limit, filters.offset)
    flights = [FlightData(**flight) for flight in result["data"]]

    return FlightsResponse(
        data=flights,
        pagination=result["pagination"]
    )
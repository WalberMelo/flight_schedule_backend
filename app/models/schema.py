
from typing import Optional, Union
from pydantic import BaseModel, Field


class FlightFilter(BaseModel):
    city: Optional[str] | None = Field(None, description="Departure city (optional, not used in free API)")
    limit: int = Field(10, gt=0, le=100)
    offset: int = Field(0, ge=0)


class AirportInfo(BaseModel):
    airport: Optional[str] = Field(None, description="Name of the airport")
    timezone: Optional[str] = Field(None, description="Timezone of the airport")
    iata: Optional[str] = Field(None, description="IATA code")
    icao: Optional[str] = Field(None, description="ICAO code")
    terminal: Optional[str] = Field(None, description="Terminal")
    gate: Optional[str] = Field(None, description="Gate")
    baggage: Optional[str] = Field(None, description="Baggage information")
    delay: Optional[int] = Field(None, description="Delay in minutes")
    scheduled: Optional[str] = Field(None, description="Scheduled time (ISO8601)")
    estimated: Optional[str] = Field(None, description="Estimated time (ISO8601)")
    actual: Optional[str] = Field(None, description="Actual time (ISO8601)")
    estimated_runway: Optional[str] = Field(None, description="Estimated runway time (ISO8601)")
    actual_runway: Optional[str] = Field(None, description="Actual runway time (ISO8601)")

class AirlineInfo(BaseModel):
    name: Optional[str] = Field(None, description="Airline name")
    iata: Optional[str] = Field(None, description="IATA code")
    icao: Optional[str] = Field(None, description="ICAO code")

class FlightInfo(BaseModel):
    number: Optional[str] = Field(None, description="Flight number")
    iata: Optional[str] = Field(None, description="IATA code")
    icao: Optional[str] = Field(None, description="ICAO code")
    codeshared: Optional[Union[str, dict]] = Field(None, description="Codeshared flight number or info")

class FlightData(BaseModel):
    flight_date: str = Field(..., description="Date of the flight")
    flight_status: str = Field(..., description="Status of the flight (e.g., scheduled, cancelled)")
    departure: AirportInfo = Field(..., description="Departure information")
    arrival: AirportInfo = Field(..., description="Arrival information")
    airline: AirlineInfo = Field(..., description="Airline information")
    flight: FlightInfo = Field(..., description="Flight information")
    aircraft: Optional[dict] = Field(None, description="Aircraft information (can be None or dict)")
    live: Optional[dict] = Field(None, description="Live flight data (if available)")

class PaginationInfo(BaseModel):
    limit: int
    offset: int
    count: int
    total: int

class FlightsResponse(BaseModel):
    data: list[FlightData] = Field(..., description="List of flights")
    pagination: PaginationInfo


class LogAnalysisRequest(BaseModel):
    log_text: str

class LogAnalysisResponse(BaseModel):
    summary: str
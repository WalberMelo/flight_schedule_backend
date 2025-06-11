from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.schema import LogAnalysisRequest, LogAnalysisResponse
from app.services.log_analysis import analyze_log



router = APIRouter()


@router.post("/analyze", response_model=LogAnalysisResponse)
async def analyze_log_endpoint(request: LogAnalysisRequest):
    try:
        return await analyze_log(request) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
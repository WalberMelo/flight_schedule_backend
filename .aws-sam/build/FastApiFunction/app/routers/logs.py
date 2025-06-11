# app/routers/logs.py
from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/logs")
def get_logs():
    df = pd.read_csv("app/data/Aircraft_Annotation_DataFile.csv")
    logs = df.head(10).to_dict(orient="records")
    return {"logs": logs}

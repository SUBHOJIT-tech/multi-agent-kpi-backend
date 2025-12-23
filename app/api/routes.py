from fastapi import APIRouter, UploadFile
import pandas as pd
from app.services.kpi_engine import KPIEngine

router = APIRouter()

@router.post("/analyze")
async def analyze_kpi(file: UploadFile):
    df = pd.read_csv(file.file)
    engine = KPIEngine()
    results = engine.run(df)
    return {"results": results}

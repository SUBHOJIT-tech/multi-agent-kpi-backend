from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
import io

router = APIRouter()

@router.post("/analyze")
async def analyze_kpi(file: UploadFile = File(...)):
    try:
        # Read CSV safely
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        # Simple demo KPI logic (robust)
        results = []

        results.append({
            "agent": "Performance Agent",
            "metric": "Row Count",
            "value": len(df)
        })

        results.append({
            "agent": "Risk Agent",
            "metric": "Column Count",
            "value": len(df.columns)
        })

        results.append({
            "agent": "Recommendation Agent",
            "metric": "Missing Values",
            "value": int(df.isna().sum().sum())
        })

        return {"results": results}

    except Exception as e:
        # Explicit error so frontend doesn't hang
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )

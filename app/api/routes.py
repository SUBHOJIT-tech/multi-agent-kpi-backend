from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
import io

router = APIRouter()

@router.post("/analyze")
async def analyze_kpi(file: UploadFile = File(...)):
    try:
        # Read raw bytes
        raw = await file.read()

        # Try decoding safely
        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError:
            content = raw.decode("latin-1")

        # Load CSV
        df = pd.read_csv(io.StringIO(content))

        # Simple, safe KPI outputs (numeric)
        results = [
            {
                "agent": "Performance Agent",
                "metric": "Row Count",
                "value": int(len(df)),
            },
            {
                "agent": "Risk Agent",
                "metric": "Column Count",
                "value": int(len(df.columns)),
            },
            {
                "agent": "Recommendation Agent",
                "metric": "Missing Values",
                "value": int(df.isna().sum().sum()),
            },
        ]

        return {"results": results}

    except Exception as e:
        # Log exact error to Render logs
        print("ANALYZE ERROR:", str(e))
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(e)}"
        )

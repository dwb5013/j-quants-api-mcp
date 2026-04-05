import json

import numpy as np
import pandas as pd


def df_to_response(df: pd.DataFrame, method: str) -> str:
    total_rows = len(df)

    # Convert datetime columns to ISO strings
    for col in df.select_dtypes(include=["datetime64", "datetimetz"]).columns:
        df[col] = df[col].dt.strftime("%Y-%m-%dT%H:%M:%S")

    # Replace NaN/NaT with None for clean JSON
    df = df.replace({np.nan: None, pd.NaT: None})

    data = df.to_dict(orient="records")

    result = {
        "data": data,
        "total_rows": total_rows,
        "returned_rows": total_rows,
        "columns": list(df.columns),
        "method": method,
    }
    return json.dumps(result, ensure_ascii=False, default=str)

import pandas as pd
import os, json
from pathlib import Path


def get_data() -> pd.DataFrame:
    dir_path: Path = Path(
        r"C:\Users\mohamed\Desktop\Programming Projects\Egypts Unemployment Rates\Data\json"
    )
    data: list[dict] = []

    for file in dir_path.iterdir():
        with open(file, "r") as file:
            data.append(json.load(file))

    df: pd.DataFrame = pd.DataFrame(data)

    return df


get_data().to_csv(
    r"C:\Users\mohamed\Desktop\Programming Projects\Egypts Unemployment Rates\Data\csv\csv_data.csv"
)

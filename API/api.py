import requests
import json


def get_unemployment_years(start_year: int, end_year: int) -> None:
    year: int = start_year
    while year <= end_year:
        url: str = (
            f"https://api.api-ninjas.com/v1/unemployment?country=Egypt&year={year}&X-Api-Key=CZWDH6Dgfi5qDcLgt7XJg3G1NUl4PFc1IAj8011x"
        )
        request = requests.get(url=url)
        data = request.json()

        with open(
            rf"C:\Users\mohamed\Desktop\Programming Projects\Egypts Unemployment Rates\Data\json\{year}.json",
            "w",
        ) as file:
            json.dump(data, file)
        year += 1


# get_unemployment_years(2000 , 2026)

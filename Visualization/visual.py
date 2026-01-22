import matplotlib.pyplot as plt
import pandas as pd


def show_data(data: pd.DataFrame) -> None:
    plt.plot(data["year"], data["unemployment_rate"])
    plt.xlabel("Years")
    plt.ylabel("Unemployment Rates")
    plt.show()

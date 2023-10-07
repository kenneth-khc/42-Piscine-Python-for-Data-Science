import pandas as pd # noqa
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Program to display life projection of each country in the year 1900"""

    try:
        df1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        df2 = load("life_expectancy_years.csv")
        if df1 is None or df2 is None:
            raise AssertionError("Failed to load from csv.")
    except AssertionError as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)
        return None

    income_1900_series = df1["1900"]
    life_expectancy_1900_series = df2["1900"]

    income_1900_series = income_1900_series.apply(clean_data)

    plt.scatter(income_1900_series, life_expectancy_1900_series)
    style_plot()
    plt.show()


def clean_data(data):
    """Clean data by removing the "k" suffix and multiplying 1000"""

    if isinstance(data, str) and data.endswith("k"):
        data = data.replace("k", "")
        data = float(data) * 1000

    return float(data)


def style_plot():
    """Style scatter plot by applying labels and ticks"""

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    plt.xscale("log")
    xlabels = ["300", "1k", "10k"]
    xticks = 300, 1000, 10000
    plt.xticks(xticks, xlabels)


if __name__ == "__main__":
    main()

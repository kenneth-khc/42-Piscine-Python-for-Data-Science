import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def main():
    try:
        df = load("population_total.csv")
        if df is None:
            raise AssertionError("Failed to load from csv.")
        France = get_country_data(df, "France")
        Belgium = get_country_data(df, "Belgium")

    except (AssertionError, ValueError) as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)
        return None

    style_plot(France, Belgium)


def get_country_data(dataframe, country: str) -> None:
    """Get a series from the dataframe given.

    From the dataframe, look for the country we are dealing with.
    We are only concerned up to the year "2050" so we will use
    iloc to locate up to that point and return it as a series.

    The original data has the population as strings, so it is
    necessary to remove the suffix "M" from e.g. "90M" and then
    convert it to a numeric type.
    """

    filtered_df = dataframe[dataframe["country"] == country]

    if filtered_df.empty:
        raise ValueError(f"{country} not found in dataframe.")

    stop_index = filtered_df.columns.get_loc("2050")
    series = filtered_df.iloc[0, 1:stop_index + 1]

    series = series.str.replace("M", "")
    series = pd.to_numeric(series)

    return series


def style_plot(country1: Series, country2: Series) -> None:
    """Style the plot to be displayed."""

    country1.plot(color="green")
    country2.plot(color="cornflowerblue")
    plt.title("Population Projections")

    plt.xlabel("Year")
    xticks = np.arange(0, 280, 40)
    xlabels = ["1800", "1840", "1880", "1920", "1960", "2000", "2040"]
    plt.xticks(xticks, xlabels)

    plt.ylabel("Population")
    yticks = np.arange(20, 80, 20)
    ylabels = ["20M", "40M", "60M"]
    plt.yticks(yticks, ylabels)

    plt.legend(["France", "Belgium"], loc="lower right", reverse=True)
    plt.show()


if __name__ == "__main__":
    main()

import pandas  # noqa
import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


def main():
    """Loads a csv file and displays information of the country of 42KL"""

    try:
        df = load("life_expectancy_years.csv")
        if df is None:
            raise Exception("Failed to load from csv.")

        Malaysia = df[df["country"] == "Malaysia"]

        malaysia_data = Malaysia.iloc[0, 1:]
        if malaysia_data.empty:
            raise Exception("No data found for Malaysia in the DataFrame")

    except (IndexError, AttributeError, Exception) as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)
        return None

    malaysia_data.plot(title="Malaysia Life expectancy Projections")
    ticks = np.arange(0, 320, 40)
    labels = ["1800", "1840", "1880", "1920", "1960", "2000", "2040", "2080"]
    plt.xticks(ticks, labels)
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()

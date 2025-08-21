
from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def show_graph(df: pd.DataFrame | None, country: str):
    """
    Display a line graph of life expectancy over time for a given country.

    Args:
        df: DataFrame with country data (first column) and years (columns)
        country: Name of the country to display

    Returns:
        None: Shows the graph using matplotlib
    """
    if df is None:
        print("No data to display")
        return

    country_row = df[df['country'] == country]

    if country_row.empty:
        print(f"Country '{country}' not found in the dataset")
        return

    years = df.columns[1:].astype(int)
    life_expectancy = country_row.iloc[0, 1:].values

    # plt.figure(figsize=(12, 6))
    plt.plot(years.tolist(), life_expectancy.tolist(),
             linewidth=2, color='blue')

    plt.title(f"{country} Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.tight_layout()
    plt.show()


def main():
    """
    Load life expectancy data and display graph for United Arab Emirates.
    """
    try:
        df = load("../life_expectancy_years.csv")
        if df is not None:
            show_graph(df, "United Arab Emirates")
        else:
            print("Failed to load data")

    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

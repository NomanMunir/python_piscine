
from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def convert_population(value):
    """
    Convert population string (e.g., '3.28M') to numeric value.

    Args:
        value: Population value as string with 'M' suffix

    Returns:
        float: Population as numeric value in millions
    """
    if isinstance(value, str) and value.endswith('M'):
        return float(value[:-1])
    return float(value)


def show_population_comparison(df: pd.DataFrame | None,
                               country1: str, country2: str):
    """
    Display a comparison graph of population over time for two countries.

    Args:
        df: DataFrame with country data (first column) and years (columns)
        country1: Name of the first country to display
        country2: Name of the second country to display

    Returns:
        None: Shows the graph using matplotlib
    """
    if df is None:
        print("No data to display")
        return

    country1_row = df[df['country'] == country1]
    country2_row = df[df['country'] == country2]

    if country1_row.empty:
        print(f"Country '{country1}' not found in the dataset")
        return

    if country2_row.empty:
        print(f"Country '{country2}' not found in the dataset")
        return

    years = df.columns[1:].astype(int)
    years_filtered = years[(years >= 1800) & (years <= 2050)]

    year_indices = [i for i, year in enumerate(years) if 1800 <= year <= 2050]

    pop1_raw = country1_row.iloc[0, 1:].values
    pop2_raw = country2_row.iloc[0, 1:].values

    pop1_filtered = [convert_population(pop1_raw[i]) for i in year_indices]
    pop2_filtered = [convert_population(pop2_raw[i]) for i in year_indices]

    plt.plot(years_filtered.tolist(), pop1_filtered,
             linewidth=2, label=country1, color='green')
    plt.plot(years_filtered.tolist(), pop2_filtered,
             linewidth=2, label=country2, color='blue')

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    """
    Load population data and display comparison graph for Belgium and France.
    """
    try:
        df = load("../population_total.csv")
        if df is not None:
            # print(f"Loaded dataset with shape: {df.shape}")
            # print("Sample countries:", df['country'].head().tolist())
            show_population_comparison(df, "Belgium", "France")
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

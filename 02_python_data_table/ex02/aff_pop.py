from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def convert_population(value):
    """
    Convert population string to numeric value.

    Handles different suffixes:
    - 'k' or 'K' = thousands (multiply by 1,000)
    - 'M' = millions (multiply by 1,000,000)
    - 'B' = billions (multiply by 1,000,000,000)

    Args:
        value: Population value as string with suffix

    Returns:
        float: Population as numeric value in millions
    """
    if isinstance(value, str):
        value = value.strip()  # Remove any whitespace

        if value.endswith('k') or value.endswith('K'):
            return float(value[:-1]) / 1000
        elif value.endswith('M') or value.endswith('m'):
            return float(value[:-1])
        elif value.endswith('B') or value.endswith('b'):
            return float(value[:-1]) * 1000
        else:
            # Plain number - convert actual population to millions
            return float(value) / 1000000

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

    plt.figure(figsize=(12, 6))
    plt.plot(years_filtered.tolist(), pop1_filtered,
             linewidth=2, label=country1, color='blue')
    plt.plot(years_filtered.tolist(), pop2_filtered,
             linewidth=2, label=country2, color='green')

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    def format_millions(x, pos):
        """Format function to add 'M' suffix to y-axis labels"""
        if x == 0:
            return '0'
        return f'{x:.0f}M'

    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_millions))

    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.show()


def main():
    """
    Load population data and display comparison graph for Belgium and France.
    """
    try:
        df = load("../population_total.csv")
        if df is not None:
            show_population_comparison(df, "Belgium", "Andorra")
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

from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def create_scatter_plot(
    life_df: pd.DataFrame, income_df: pd.DataFrame, year: int
):
    """Create a scatter plot of life expectancy vs GDP per capita for a year.

    Args:
        life_df: DataFrame with life expectancy data
        income_df: DataFrame with GDP per capita data
        year: Year to display (e.g., 1900)
    """
    if life_df is None or income_df is None:
        print("No data to display")
        return

    year_str = str(year)
    if year_str not in life_df.columns:
        print(f"Year {year} not found in life expectancy data")
        return

    if year_str not in income_df.columns:
        print(f"Year {year} not found in income data")
        return

    life_data = life_df[["country", year_str]].dropna()
    income_data = income_df[["country", year_str]].dropna()

    merged_data = pd.merge(
        life_data, income_data, on="country", suffixes=("_life", "_income")
    )

    if merged_data.empty:
        print(f"No matching data found for year {year}")
        return

    gdp_values = merged_data[f"{year_str}_income"]
    life_values = merged_data[f"{year_str}_life"]

    plt.figure(figsize=(10, 6))
    plt.scatter(gdp_values, life_values, alpha=0.7, s=50)

    plt.title(f"{year}")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    plt.xscale("log")

    plt.gca().set_xticks([300, 1000, 10000])
    plt.gca().set_xticklabels(["300", "1k", "10k"])

    plt.tight_layout()
    plt.show()


def main():
    """Load life expectancy and GDP data, then display scatter plot for
    1900."""
    try:
        life_df = load("../life_expectancy_years.csv")
        income_df = load(
            "../income_per_person_gdppercapita_ppp_" "inflation_adjusted.csv"
        )

        if life_df is not None and income_df is not None:
            create_scatter_plot(life_df, income_df, 1900)
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

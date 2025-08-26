import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV file and return a pandas DataFrame.

    Args:
        path (str): Path to the CSV file to load

    Returns:
        pd.DataFrame | None: DataFrame if successful, None if error occurs
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except KeyboardInterrupt:
        return None
    except EOFError:
        return None
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

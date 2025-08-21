#!/usr/bin/env python3
"""
Simple tester for load_csv.py
"""

from load_csv import load


def main():
    """Main test function"""
    try:
        test_files = [
            "../life_expectancy_years.csv",
        ]

        for file_path in test_files:
            print(f"\nTesting: {file_path}")
            print("-" * 40)
            result = load(file_path)
            if result is not None:
                print(f"Success! Shape: {result.shape}")
                print(result.head(2))
            else:
                print("Failed to load (returned None)")
            print("-" * 40)

    except KeyboardInterrupt:
        pass
    except EOFError:
        pass
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

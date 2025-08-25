from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate statistics (mean, median, quartile, std, var) for given numbers.
    
    Args:
        *args: Variable number of numeric arguments
        **kwargs: Statistics to calculate (mean, median, quartile, std, var)
    
    Returns:
        None: Prints results or ERROR for invalid inputs
    """
    if not args:
        for key in kwargs.values():
            print("ERROR")
        return
    
    try:
        numbers = sorted(args)
        n = len(numbers)
        
        for key, stat_type in kwargs.items():
            if stat_type == "mean":
                result = sum(numbers) / n
                print(f"mean : {result}")
            elif stat_type == "median":
                if n % 2 == 0:
                    result = (numbers[n//2 - 1] + numbers[n//2]) / 2
                else:
                    result = numbers[n//2]
                print(f"median : {result}")
            elif stat_type == "quartile":
                q1_pos = (n - 1) * 0.25
                q3_pos = (n - 1) * 0.75
                
                def get_quartile_value(pos):
                    """Calculate quartile value using linear interpolation."""
                    lower = int(pos)
                    upper = lower + 1
                    if upper >= n:
                        return float(numbers[lower])
                    weight = pos - lower
                    return float(numbers[lower] * (1 - weight) + 
                               numbers[upper] * weight)
                
                q1 = get_quartile_value(q1_pos)
                q3 = get_quartile_value(q3_pos)
                print(f"quartile : [{q1}, {q3}]")
            elif stat_type == "std":
                mean = sum(numbers) / n
                variance = sum((x - mean) ** 2 for x in numbers) / n
                result = variance ** 0.5
                print(f"std : {result}")
            elif stat_type == "var":
                mean = sum(numbers) / n
                result = sum((x - mean) ** 2 for x in numbers) / n
                print(f"var : {result}")
    except Exception:
        for key in kwargs.values():
            print("ERROR")


def main():
    """Main function for testing."""
    # Test cases from the requirements
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")

if __name__ == "__main__":
    main()

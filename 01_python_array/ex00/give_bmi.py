
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for each person.
    The BMI is calculated using the formula:
    BMI = weight / (height^2)
    :param height: List of heights in meters.
    :param weight: List of weights in kilograms.
    :return: List of BMI values.
    """
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Height and weight must be lists.")
        if len(height) != len(weight):
            raise ValueError(
                "Lists of height and weight must have the same length.")
        bmi_values = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) \
                    or not isinstance(w, (int, float)):
                raise TypeError(
                    "Height and weight must be integers or floats.")
            if h <= 0 or w <= 0:
                raise ValueError("Height and weight values must be positive.")
            bmi = w / (h ** 2)
            bmi_values.append(bmi)
        return bmi_values
    except Exception as error:
        print("Error:", error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if each BMI value is above a certain limit.
    :param bmi: List of BMI values.
    :param limit: The limit to compare against.
    :return: List of booleans indicating if each BMI is above the limit.
    """
    try:
        if not isinstance(bmi, list):
            raise TypeError("BMI must be list.")
        if not isinstance(limit, int):
            raise TypeError("Limit must be int.")
        limits = []
        for value in bmi:
            if not isinstance(value, (int, float)):
                raise TypeError("BMI values must be ints or floats.")
            limits.append(value > limit)
        return limits
    except Exception as e:
        print(f"Error: {e}")
        return []

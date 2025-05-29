
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

    return [w / (h**2) for w, h in zip(weight, height)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if each BMI value is above a certain limit.
    :param bmi: List of BMI values.
    :param limit: The limit to compare against.
    :return: List of booleans indicating if each BMI is above the limit.
    """
    return [b > limit for b in bmi]

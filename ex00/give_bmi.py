def validate_lists(height: list, weight: list) -> None:
    """Validate the lists by checking if they have the same elements,
if the arguments are ints or floats and if they are positive."""
    if len(height) != len(weight):
        raise TypeError("Lists do not have the same number of elements.")
    for i in height:
        if not isinstance(i, (int, float)):
            raise TypeError("Height should only be ints or floats.")
        if i <= 0:
            raise ValueError("Height should be positive.")
    for j in weight:
        if not isinstance(j, (int, float)):
            raise TypeError("Weight should only be ints or floats.")
        if j <= 0:
            raise ValueError("Weight should be positive.")


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """Calculate the bmi by dividing weight in kilograms by
height in meters squared."""
    try:
        validate_lists(height, weight)
    except (TypeError, ValueError) as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)
        return None
    else:
        bmi_list = [w / h ** 2 for h, w in zip(height, weight)]
        return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Checks the bmi against a limit and returns a list of booleans
for each bmi that is greater than the limit."""
    try:
        limit = int(limit)
        if len(bmi) == 0:
            raise ValueError("List is empty!")
    except (TypeError, ValueError) as e:
        error_message = f"Error: {e}" if e else "Error."
        print(error_message)
    else:
        result = [i > limit for i in bmi]
        return result

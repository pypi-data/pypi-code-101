
def set_values(value, rounding_value):
    """
    Rounding may lead to values not being the right length when converted to strings. This formats them

    :param value: Value to turn into a string
    :type value: float | int

    :param rounding_value: Rounding value target
    :type rounding_value: int

    :return: string representation of the rounded 'value', where rounding is set by rounding_value
    :rtype: str
    """
    set_rounding = round(float(value), rounding_value)

    # If we have zero, then it will always be 0.0 and not respect rounding, so we need to handle zero separately
    if set_rounding == 0:
        return " 0." + "".join(["0" for _ in range(rounding_value)])

    # If the value is less than zero, we can just create a string value of it and then add three to represent the '-0.'
    elif set_rounding < 0:
        set_rounding = str(set_rounding)
        rounding_value += 3

    # If the value is above zero we need to add a space, so that it will be in line with negative values
    else:
        set_rounding = f" {set_rounding}"
        rounding_value += 3

    # If the value does not equal to expected, post-pend additional zeros to make them equal
    if len(set_rounding) == rounding_value:
        return set_rounding
    else:
        return set_rounding + "".join(["0" for _ in range(rounding_value - len(set_rounding))])


def is_valid(number, rule):
    """Return True if the number respects the given rule else False"""
    if (number in range(rule[0][0], rule[0][1] + 1)) or (
        number in range(rule[1][0], rule[1][1] + 1)
    ):
        return True
    return False

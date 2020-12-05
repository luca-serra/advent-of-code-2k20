def hgt(x):
    """Return True if the 'hgt' format is valid, return False otherwise"""
    res = False
    if x.endswith("cm"):
        height = x.replace("cm", "/").split("/")[0]
        if height.isdigit():
            if 150 <= int(height) <= 193:
                res = True
    if x.endswith("in"):
        height = x.replace("in", "/").split("/")[0]
        if height.isdigit():
            if 59 <= int(height) <= 76:
                res = True
    return res

def closest_greater_number(integer, threshold):
    """Return the closest multiple of integer, greater than threshold"""
    res = integer
    while res < threshold:
        res += integer

    return res


def compute_earliest_buses(threshold, bus_ids):
    res = []
    for bus_id in bus_ids:
        if bus_id != "x":
            res.append(closest_greater_number(bus_id, threshold))
        else:
            res.append(bus_id)
    return res


def lcm(*n):
    """Computes the least common multiple of several integers"""

    def _gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    p = abs(n[0] * n[1]) // _gcd(n[0], n[1])
    for x in n[2:]:
        p = abs(p * x) // _gcd(p, x)
    return p

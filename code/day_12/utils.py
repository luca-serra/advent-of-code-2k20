def manhattan_distance(N, E):
    """
    Compute Manhattan distance given the North and East coordinates.
    A value of n in the South would be -n in the North.
    A value of m in the West would be -m in the East.
    """
    return int(abs(N) + abs(E))

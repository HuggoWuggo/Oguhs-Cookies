def inrange(points: list[tuple[int | float, int | float]] = None, radius: int | float = 0) -> bool | None:
    """
    A function that checks if two coordinates are within a specified radius.
    Returns None if points or radius aren't specified, otherwise returns
    whether the coordinates are within the radius as a bool

    :param points: The input list of coordinates as two tuples. Required
    :param radius: The radius the coordinates should be within. Required
    """

    if not points or radius == 0:
        print('Missing Parameters Of points Or radius')
        return None

    if abs(points[1][0] - points[0][0]) <= radius >= abs(points[1][1] - points[0][1]):
        return True
    else:
        return False

def offset(points: list[tuple[int | float, int | float]]) -> tuple[int | float, int | float] | None:
    """
    A function that evaluates the distance between two coordinates in the x and y axes.
    Returns None if points aren't specified, otherwise returns the distance between the
    coordinates in the x and y axes as a tuple

    :param points: The input list of coordinates as two tuples. Required
    """

    if not points:
        print('Missing Parameter Of points')
        return None

    axes_offset: tuple[int | float, int | float] = (abs(points[1][0] - points[0][0]), abs(points[1][1] - points[0][1]))

    return axes_offset

def diff(points: list[tuple[int | float, int | float]]) -> float | None:
    """
    A function that evaluates the distance between two coordinates. Returns None if
    points aren't specified, otherwise returns the distance between the coordinates
    as a float

    :param points: The input list of coordinates as two tuples. Required
    """

    if not points:
        print('Missing Parameter Of points')
        return None

    difference: float = ((points[1][0] - points[0][0]) ** 2 + (points[1][1] - points[0][1]) ** 2) ** 0.5

    return difference

def bisector(points: list[tuple[int | float, int | float]]) -> tuple[int | float, int | float] | None:
    """
    A function that evaluates the coordinates for the midpoint of a line. Returns None if
    points aren't specified, otherwise returns the coordinates of the midpoint as a tuple

    :param points: The input list of coordinates as two tuples. Required
    """

    if not points:
        print('Missing Parameter Of points')
        return None

    midpoint: tuple[int | float, int | float] = (points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2

    return midpoint

def gradient(points: list[tuple[int | float, int | float]]) -> float | None:
    """
    A function that evaluates the gradient of a line. Returns None if
    points aren't specified, otherwise returns the gradient as a float

    :param points: The input list of coordinates as two tuples. Required
    """

    if not points:
        print('Missing Parameter Of points')
        return None

    return (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])

def isparallel(lines: tuple[list[tuple[int | float, int | float]], list[tuple[int | float, int | float]]]) -> bool | None:
    """
    A function that checks if two lines are parallel. Returns None if
    lines aren't specified, otherwise returns a bool

    :param lines: The input list of lines as two tuples of coordinates. Required
    """

    if len(lines) < 2:
        print('Missing Parameter Of lines')
        return None

    if gradient(lines[0]) == gradient(lines[1]):
        return True
    else:
        return False

def isperpendicular(lines: tuple[list[tuple[int | float, int | float]], list[tuple[int | float, int | float]]]) -> bool | None:
    """
    A function that checks if two lines are perpendicular. Returns None if
    lines aren't specified, otherwise returns a bool

    :param lines: The input list of lines as two tuples of coordinates. Required
    """

    if len(lines) < 2:
        print('Missing Parameter Of lines')
        return None

    if gradient(lines[0]) * gradient(lines[1]) == -1:
        return True
    else:
        return False
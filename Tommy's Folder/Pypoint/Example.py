import Pypoint

# These are the points we will use
points = (5, 10), (12, 15)

# Using the Pypoint.diff function add
# arguments of the points and the
# distance to check
in_range = Pypoint.diff(points, 15)

# If both points are within the distance
# of each other, the function returns True
# otherwise it returns False

print(in_range)
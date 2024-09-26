# To use this module, put the file 'Pypoint.py'
# Into the directory
# 'C:\Users\%username%\AppData\Local\Packages\
# PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\
# LocalCache\local-packages\Python311\site-packages'

import Pypoint

# These are the points we will use
points = (5, 10), (12, 15)

# Using the Pypoint.inrange function add
# arguments of the points and the
# distance to check
in_range = Pypoint.inrange(points, 15)

# If both points are within the distance
# of each other, the function returns True
# otherwise it returns False

print(in_range)

# Using the Pypoint.diff function add
# arguments of the points
difference = Pypoint.diff(points)

# This function returns the distance
# between the two points inputted

print(difference)
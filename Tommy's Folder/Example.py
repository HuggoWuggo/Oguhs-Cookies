# To use this module, put the file 'Graphene.py'
# Into the directory
# 'C:\Users\%username%\AppData\Local\Packages\
# PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\
# LocalCache\local-packages\Python311\site-packages'

import Graphene

#This is the data set that will be graphed
data = [5, 3, 1, 3, 5]

#Using the 'Graph' function, add 3 arguments of
#the data set
#if connecting lines whould be drawn
#and the size of the points
Graphene.graph(data, False, 10)

#The first parameter is required
#The second parameter defults to True
#The third parameter defults to 15
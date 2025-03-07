import matplotlib.pyplot as plt
import numpy as np

xcoordinates = np.array([1,2,3,4,5,6])
ycoordinates = np.array([1,4,9,16,25,36])

plt.title("This is a graph ")

plt.plot(xcoordinates , ycoordinates)

plt.plot(xcoordinates ,ycoordinates , marker = 'o')
plt.plot(ycoordinates ,xcoordinates , marker = 'x')
plt.xlabel("Line 1 ")
plt.ylabel("Line 2")
plt.show()

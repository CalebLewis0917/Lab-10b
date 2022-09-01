# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab10b_Act1
# Date:         11 14 2021

import numpy as np
import matplotlib.pyplot as plt

# Initialize Variables
v = np.array([(1),(0)])
M = np.array([(1.00583,-.087156),(.087156,1.00583)])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Spiral")
p = v
# Plot Points
for i in range(250):
    p = p.dot(M)
    plt.plot(p[0],p[1],'ro')
    print(p[0],p[1])
plt.show()
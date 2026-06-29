#section 3.4 linear transformations
#there is no programming in this section, so this is a good way to show students 
#how a linear transformation can be represented as a matrix

import numpy as np

#exercise 1 from the book

#linear transformation T: R^3 → R^2
#given by rule: T(x, y, z) = (x + y - 2z, -y + z)
def T(x,y,z):
    return np.array([x + y - 2*z, -y + z])

#sample vectors
v1 = np.array([1, 2, 3])
v2 = np.array([1, 0, -2])

#exercise 1: is T linear?
def check_linearity(v1, v2, a, b):
    left_side = T(*(a*v1 + b*v2))
    right_side = a*T(*v1) + b*T(*v2)
    print("Is T linear?", np.allclose(left_side, right_side))

check_linearity(v1, v2, a=2, b=3)


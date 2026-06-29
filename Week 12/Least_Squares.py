import numpy as np

# For each of the following, solve the least squares problem
# J = ||A @ x - b||**2

### Exercise 1 ###
A = np.array([[4,-4,-1,1],
              [1,2,5,-3],
              [0,-1,-3,3],
              [2,-2,1,0],
              [0,1,0,-1]])

b = np.array([1,2,3,5,8])

x = np.linalg.lstsq(A,b,rcond=None)[0]

print(np.round(x,3))
#solution: x = [4.365,3.893,-1.856,-0.013]
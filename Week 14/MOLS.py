import numpy as np

#Use NumPy to construct and analyze multi-objective regression models

def multi_lstsq(As, bs, lambdas):
    k = len(lambdas)
    A = np.concatenate([np.sqrt(lambdas[i])*np.array(As[i]) for i in range(k)])
    b = np.concatenate([np.sqrt(lambdas[i])*np.array(bs[i]) for i in range(k)])
    return np.linalg.lstsq(A,b, rcond=None)[0]

# For each of the following, solve the multi-objective least squares problem
# J = lambda_1J_1 + lambda_2J_2 + ... + lambda_kJ_k
# where J_i = ||A_i @ x - b_i||**2


### Exercise 1 ###
# J_1
A1 = np.array([[6, 10],
               [12, 8],
               [14, 11]])
b1 = np.array([5, 11, 4])
lambda1 = 1

# J_2
A2 = np.array([[6, 50],
               [2, 15]])
b2 = np.array([7/3, 5])
lambda2 = 36

x = multi_lstsq([A1, A2], [b1, b2], [lambda1, lambda2])
print(x)
#solution: [ 0.66918127 -0.01092971]
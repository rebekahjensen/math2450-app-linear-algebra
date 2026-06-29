#1.4 PYTHON PROGRAMMING

#norm function on vectors
import numpy as np

def vector_norm(vector):
    vector_sum = 0
    for i in x:
        vector_sum += i ** 2
    return np.sqrt(vector_sum)

x = np.array([1,2,5,12])
print(vector_norm(x))
#output norm of x = 13.19090595827292

#norm of a vector is already implemened in linalg in numpy:
#np.linalg.norm(x) - use this!!!

####

#EXAMPLE 1.4.13
#but there is no pre-loaded to find distance between 2 vectors
#to find dist(u, v) = norm of (u-v):
import numpy as np

x = np.array([2,-1,2])
print(np.linalg.norm(x))

u = np.array([1.8, 2.0, -3.7, 4.7])
v = np.array([0.6, 2.1, 1.9, -1.4])
w = np.array([2.0, 1.9, -4.0, 4.6])
print(np.linalg.norm(u-v))
print(np.linalg.norm(u-w))
print(np.linalg.norm(v-w))

#also see np.mean(x) and np.std(x), x is a vector
#how do we find RMS (root-mean-square)?
rms = lambda v : np.linalg.norm(v)/np.sqrt(len(v))
#or (this one is better)
rms = lambda v : np.sqrt(np.mean(v**2))


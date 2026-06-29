import numpy as np
import matplotlib.pyplot as plt

#2.4 textbook

### EXERCISE 1 ##########################
# interpolate the function f(x) = a_0 + a_1x + a_2x^2 + a_3x^3 + a_4x^4 + a_5x^5 through the given points.
points = np.array([[-2,231],[-1,19],[0,5],[1,9],[2,19],[3,-169]]) #6 points
x = points[:,0]
y = points[:,1]

#vandermonde matrix A - for polynomials 
V = np.vander(x, increasing = True)
# print("V = ", V)

c = np.linalg.solve(V, y) #coefficients

f = np.poly1d((c[::-1]))
print("Interpolating polynomial: ", f)
#passes thru all 6 points

### VERIFICATION 1 ############################
plt.ion()
t = np.linspace(-3,4,num = 100)
plt.axis([-3,4,-200,300])
plt.scatter(x,y)
plt.plot(t,f(t), 'r')
plt.show(block=True)

### EXERCISE 2 ##########################
# interpolate the function f(x) = (a_0 + a_1x + a_2x^2) / (1 + b_1x + b_2x^2) through the given points.
points = np.array([[-2,12/11],[-1,3/2],[0,2],[1,0],[2,0]]) #non-linear, need to fix 
x = points[:,0]
y = points[:,1]

n = 2 
#matrix A
A = np.column_stack([np.ones_like(x), x, x**2, -y*x, -y*x**2])

b = y
f = np.linalg.solve(A, b)
a0, a1, a2, b1, b2 = f #running into issues w this 

#polyval/poly1d
numer = np.array([a2, a1, a0])     
denom = np.array([b2, b1, 1.0])         

print("Numerator:" ,np.poly1d(numer), "/\n", "Denominator: ", np.poly1d(denom))

# ### VERIFICATION 2 ############################
t = np.linspace(-3,4,num=200)
plt.axis([-3,4,-10,10])
plt.scatter(x, y)
plt.plot(t, np.polyval(numer, t) / np.polyval(denom, t), 'r')
plt.show(block=True)

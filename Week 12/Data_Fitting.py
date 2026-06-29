import numpy as np
import matplotlib.pyplot as plt

### EXERCISE 1 ##########################
#interpolate the function thru given points

points = np.array([[-2,231],[-1,19],[0,5],[1,9],[2,19],[3,-169],
                   [-1.5,100],[-0.5,20],[0.5,12],[2.5,0],[3.5,-25]])
x = points[:,0]
y = points[:,1]

A = np.vander(x, 6)
f = np.linalg.lstsq(A, y, rcond=None)[0]

print(np.poly1d(f))


#Graph Scatterplot
# plt.ion()
t = np.linspace(-3,4,num = 100)
plt.axis([-3,4,-200,300]) 
plt.scatter(x,y)
plt.plot(t, np.poly1d(f)(t), 'r')
plt.show()


### EXERCISE 2 ##########################
points = np.array([[-2,12/11],[-1,3/2],[0,2],[1,0],[2,0],
                   [-1.5,10/3],[-0.5,20/15],[0.5,-12/5],[2.5,-11/3],[3.5,-25/7]])
x = points[:,0]
y = points[:,1]

n = 2

A = np.column_stack([x**2, x, np.ones_like(x), -y*x**2, -y*x])
f = np.linalg.lstsq(A,y,rcond=None)[0]
numer = f[:n+1]
denom = np.concatenate((f[n+1:], [1]))

print(np.poly1d(numer), "/\n", np.poly1d(denom))

#Graph Scatterplot
plt.axis([-3,4,-10,10])
plt.scatter(x,y)
plt.plot(t, np.polyval(numer,t) / np.polyval(denom,t), 'r')
plt.show()


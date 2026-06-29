import numpy as np
import matplotlib.pyplot as plt

#use numpy to fit models to data with regularization

def data_fit_regular(X, y, lamb):
    m,n = X.shape
    A = np.concatenate((np.array(X),np.sqrt(lamb)*np.identity(n)))
    b = np.concatenate((np.array(y),np.zeros(n)))
    return np.linalg.lstsq(A,b, rcond=None)[0]

#Exercise 1
#interpolate  
lamb = 0.1
points = np.array([[-2, 231],[-1, 19],[0,5],[1,9],[2,19],[3,-169],[-1.5,100],[-0.5,20],[0.5,12],[2.5,0],[3.5,-25]])
x = points[:,0]
y = points[:,1]

A = np.vander(x,6)
f = data_fit_regular(A,y,lamb)
print(f)

t = np.linspace(-2.5,4,num = 100)
plt.axis([-2.5,4,-200,250])
plt.scatter(x,y)
plt.plot(t,np.poly1d(f)(t), 'r')
plt.show()
#solution f = [  2.501358  -4.385186 -32.736087  47.377769  36.467654  -5.53939 ]

#Exercise 2
lamb = 0.25
points = np.array([[-2,12/11],[-1,3/2],[0,2],[1,0],[2,0],[-1.5,10/3],[-0.5,20/15],[0.5,-12/5],[2.5,-11/3],[3.5,-25/7]])
x = points[:,0]
y = points[:,1]

A = np.column_stack((x**2, x, np.ones_like(x), -y*x**2, -y*x))
f = data_fit_regular(A,y,lamb)

print(f)
t = np.linspace(-2.5,4,num = 100)
plt.axis([-2.5,4,-5,5])
plt.scatter(x,y)
plt.plot(t,np.poly1d(f)(t), 'r')
plt.show()
#solution f = [ 0.154071 -0.666179  0.366036 -0.080108 -0.051465]
import numpy as np

### EXERCISE 1#
#Compute the inner product of the vectors x and y below.
x = np.array([ 5.68926168, 6.48028365, 5.64919868, 4.64594575, 9.70900398, 8.2673083, 1.48566455, 9.48149181, 0.30697194, 8.19313516])
y= np.array([ 4.12159476, -0.90500151, -1.24963052, -4.18992406, 5.47895589, 6.658136, -4.20026454, -7.38517255, -2.03795684, -6.02101768])
print("x =", x)
print("y =", y)

print("x@y =", x @ y ) #compute dot product here, use @
#solution = -26.920583159552294
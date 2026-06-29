import numpy as np

#all scalars are floats
#vectors are np.arrays

### EXERCISE 1#

#Compute the norm of the vectors x and y below.
x = np.array([ 5.68926168, 6.48028365, 5.64919868, 4.64594575, 9.70900398, 8.2673083, 1.48566455, 9.48149181, 0.30697194, 8.19313516])
y= np.array([ 4.12159476, -0.90500151, -1.24963052, -4.18992406, 5.47895589, 6.658136, -4.20026454, -7.38517255, -2.03795684, -6.02101768])
print("x =", x)
print("y =", y)


#use sublibrary linalg in numpy (np.linalg.norm(x))
print("|x| =",(np.linalg.norm(x)) ) #compute the number here.
#solution = 21.20850675359146
print("|y| =",(np.linalg.norm(y))) #compute the number here.
#solution = 14.96202732208226

### EXERCISE 2#

#compute the mean, the RMS, and standard deviation for the vectors below.
x = np.array([67.62205015, 18.85856747, 89.87482278, 33.23317543, 67.85376642, -7.76168227, 32.4542289, -5.69862975, 71.17102728, 22.10567789, 6.15236876, 80.30186233, 63.52505289, 46.06165362, 18.30431459, 82.95936131, 31.25160879, 34.81357958, 24.1450134, 56.96792735, 50.38486339, 62.0442239, 5.38461851, 19.41416245, 41.11320126, -5.09183741, 90.80877811, 72.99345778, 99.17639035, 72.66443221]) 

print("avg(x) = ", (np.mean(x)) ) #compute the stats here.

rms = lambda v: np.sqrt(np.mean(x**2)) #there is no preloaded rms function, use this one
print("rms(x) = ", rms(x))

print("std(x) = ", (np.std(x)) ) 
#avg(x) = 44.769601249, rms(x) = 54.3116465166349, std(x) = 30.747971499815034
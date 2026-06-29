#let's visualize 2.9
#this program shows orthogonality and the orthogonal projection from 2.9
#it takes two vectors, checks if they are orthogonal, and computes the projection if not orthogonal
#this is useful because it helps students see the theory in action and they can run this program themselves
#the point of this contribution is to help students see how simple it is to check two vectors for orthogonalit
#it's nice to see a program in each section of the book so students can try to apply it, so adding a simple program like this adds that
#easy way to visualize the concept (I like print statements)

#this program should be placed before example 2.9.4 or 2.9.3, right after the textbook discusses orthogonality in vectors

import numpy as np

#define 2 vectors
a = np.array([2,1,1])
b = np.array([1,7,3])

#check for orthogonality
dot_product = np.dot(a,b)
if dot_product == 0: #dot product = 0 when two vectors are orthogonal
    print("a and b are orthogonal.")
else:
    print(f"Not orthogonal, the dot product is {dot_product}")

#find the projection of 2 vectors, when not orthogonal
projection = (np.dot(a,b) / np.dot(a,a) * a)
print(f"The projection of a and b is {projection}")



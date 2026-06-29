import numpy as np

A = np.array([[0,0,0,1,1,1],[0,1,1,0,1,1],[1,0,1,0,0,1]])

def detect_A(w):
    w = np.array(w)
    B = A.dot(w) % 2
    return not np.all(B == 0)


Words = np.array([[1,1,1,0,0,0],[1,1,0,1,1,0],[1,1,1,1,0,1]])
for w in Words:
    print(f"{w} has error? {detect_A(w)}.")
print("\n")
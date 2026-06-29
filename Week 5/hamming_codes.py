import numpy as np
#(0,1)

### TASK 1 #########
def Hamming_dist(x,y):
    #how many spots differ? add up
    x = np.array(x) #([1,0,1,0,1])
    y = np.array(y) #([1,1,0,1,0])
    return np.sum(x ^ y) #xor add


def Hamming_norm(x):
    #number of 1s in x
    x = np.array(x)
    return np.sum(x) #count the 1s

Words = np.array([[1,0,1,0,1],[1,1,0,1,0],[0,0,0,1,1]])

#Compute Hamming Distances
#already done for me :)
for i in range(len(Words)):
    for j in range(i+1,len(Words)):
        print(f"Hamming distance between {Words[i]} and {Words[j]} is {Hamming_dist(Words[i], Words[j])}.")
        
#Compute Hamming Norms
for w in Words:
    print(f"Hamming norm of {w} is {Hamming_norm(w)}.")
print("\n")

#expected: 4,3,3 ; 3,3,2 (from book)

### TASK 2 #########
#function to detect/correct transmitted boolean 5-vectors

C = np.array([[0,0,0,0,0],[1,1,1,1,0],[1,0,1,0,1],[0,1,0,1,1]])

def decode_C(w):
    closest = Hamming_dist(w,C[0]) #start w/ first codeword
    decoded = C[0] #first

    for c in C[1:]: #cont
        dist = Hamming_dist(w,c)
        if dist < closest:
            closest = dist #update
            decoded = c
    return decoded
        
Words = np.array([[0,1,0,1,1],[1,1,1,0,0],[1,0,0,0,1]])

for w in Words:
    print(f"{w} decodes as {decode_C(w)}.")
print("\n")

#verify w/ (0,1,0,1,1),(1,1,1,0,0),(1,0,0,0,1)
import numpy as np

#create canonical parity check & generator matrices
#encode linear codes

### TASK 1 ###
def linear_code(A):
    #will output canonical parity check matrix
    #and generator matrix associated to A

    A = np.array(A)
    n, r = A.shape
    H = np.concatenate((A.T, np.identity(r, dtype = int)), axis = 1)
    G = np.concatenate((np.identity(n, dtype = int), A), axis = 1)

    return H, G


### TASK 2 ###
def linear_encode(G,message):
    #will output the encoded message for
    #the linear code associated to generator matrix G

    G = np.array(G, dtype = int)
    message = np.array(message, dtype = int)
    encoded_msg = (message @ G) % 2

    return encoded_msg


### VERIFICATION ############################
### TASK 1 ###
A = np.array([[0,1,1],[1,1,0],[1,0,1]])
H,G = linear_code(A)
print(H,"\n",G,"\n")

### TASK 2 ###
A = np.array([[1,1],[1,0]])#,[1,1]])
H,G = linear_code(A)

for w in [[0,0],[0,1],[1,0],[1,1]]:
    print(linear_encode(G,w))
print("\n")
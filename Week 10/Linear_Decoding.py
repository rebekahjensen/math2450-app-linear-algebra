import numpy as np

def linear_code(A):
    A = np.array(A)
    n, r = A.shape
    H = np.concatenate((A.T, np.identity(r, dtype = int)), axis = 1)
    G = np.concatenate((np.identity(n, dtype = int), A), axis = 1)

    return H, G


def linear_decode(H,message):
    #similar to encode
    H = np.array(H, dtype = int)
    message = np.array(message, dtype = int)
    syndrome = (H @ message) % 2

    if np.all(syndrome == 0):
        print("No errors found.")
        return message[:H.shape[1] - H.shape[0] // 2] if len(message) > 5 else message[:5]
    
    for i in range(H.shape[1]):
        if np.array_equal(syndrome, H[:, i]):
            message[i] = (message[i] + 1) % 2  
            print("Corrected message: ", message)
            return message[:5]
        
    return "Error uncorrectable"


### VERIFICATION ############################
A = np.array([[1,1,1,0,0],
              [1,0,1,1,1],
              [1,1,0,1,0],
              [0,0,1,1,1],
              [0,1,0,0,1]])
H,G = linear_code(A)
words = [[1,0,0,1,0,1,1,1,0,0],
         [0,1,1,0,1,0,0,1,0,0],
         [1,1,0,0,0,0,0,0,1,1],
         [1,1,0,0,1,0,1,0,1,0],
         [1,1,1,0,1,1,1,0,0,0]]
for w in words:
    print(linear_decode(H,w))
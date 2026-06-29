import numpy as np

def row_scaling(coefficient_matrix, augmented_matrix, scalar, i):
    A = coefficient_matrix.astype(float)
    A[i] = scalar*coefficient_matrix[i]
    b = augmented_matrix.astype(float)
    b[i] = scalar*augmented_matrix[i]    
    
    return A,b


def row_replacement(coefficient_matrix, augmented_matrix, scalar, i, j):
    A = coefficient_matrix.astype(float)
    A[i] = coefficient_matrix[i] + scalar*coefficient_matrix[j]
    b = augmented_matrix.astype(float)
    b[i] = augmented_matrix[i] + scalar*augmented_matrix[j]    
    
    return A,b


def row_interchange(coefficient_matrix, augmented_matrix, i, j):
    idx = np.arange(len(coefficient_matrix))
    idx[i] = j
    idx[j] = i  
    
    return coefficient_matrix[idx],augmented_matrix[idx]


def zero_below(coefficient_matrix, constant_matrix, pivot):
    A = coefficient_matrix.astype(float)
    b = constant_matrix.astype(float)
    if abs(A[pivot]) < 1e-6:
        for k in range(pivot[0]+1,len(A)):
            if abs(A[k,pivot[1]]) > 1e-6:
                A,b = row_interchange(A,b,k,pivot[0])
                break
    for k in range(pivot[0]+1, len(A)): 
        A,b = row_replacement(A,b,-A[k,pivot[1]]/A[pivot],k,pivot[0])
    return A,b


def zero_above(coefficient_matrix, constant_matrix, pivot):
    A = coefficient_matrix.astype(float)
    b = constant_matrix.astype(float)
    A, b = row_scaling(A,b,1/A[pivot],pivot[0])
    for k in range(pivot[0]): 
        A, b = row_replacement(A,b,-A[k,pivot[1]],k,pivot[0])
    return A,b


def forward_phase(coefficient_matrix, constant_matrix):
    A = coefficient_matrix.astype(float)
    b = constant_matrix.astype(float)
    pivots = []
    if np.linalg.norm(A) < 1e-6: #checks for zero matrix
        return A,b,pivots
    i = 0
    for j in range(i,A.shape[1]):
        if np.linalg.norm(A[i:,j]) < 1e-6: #checks for zero column
            continue
        else:
            A,b = zero_below(A,b,(i,j))
            pivots.append((i,j))
            i += 1      
    return A,b,pivots


def backward_phase(coefficient_matrix, constant_matrix, pivots):
    A = coefficient_matrix.astype(float)
    b = constant_matrix.astype(float)
    for pivot in pivots[::-1]:
        A,b = zero_above(A,b,pivot)     
    return A,b


def Null(matrix): #write function to calculate a basis for nul(A)
    A = matrix.astype(float) 
    m, n = A.shape

    #find RREF
    b_vector = np.zeros((m))
    A1, b1, pivots = forward_phase(A, b_vector)
    RREF, b2 = backward_phase(A1, b1, pivots)

    #find pivot and free columns
    pivot_cols = [j for i, j in pivots]
    free_cols = [j for j in range(n) if j not in pivot_cols]

    if len(free_cols) == 0:
        return np.zeros((n, 1)) 
    
    basis_vectors = []
    for free in free_cols:
        v = np.zeros(n)
        v[free] = 1

        for i, j in pivots: #pos of leading ones
            v[j] = -RREF[i, free] #pivot column i

        basis_vectors.append(v)

    return np.array(basis_vectors).T #null from RREF of A 

   
### VERIFY ############################
A = np.array([[6,5,4,3,2,1],
              [5,4,3,2,1,6],
              [2,4,6,8,2,4],
              [0,1,0,1,2,6]])
print(np.round(Null(A),12))
print(Null(np.zeros((4,5))),"\n")
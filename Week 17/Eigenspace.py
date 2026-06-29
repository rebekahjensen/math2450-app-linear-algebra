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
        for k in range(pivot[0],len(A)):
            if abs(A[k,pivot[1]]) > 1e-6:
                A,b = row_interchange(A,b,k,pivot[0])
                break
    for k in range(pivot[0]+1, len(A)): 
        A,b = row_replacement(A,b,-A[k,pivot[1]]/A[pivot],k,pivot[0])
    return A,b


def zero_above(coefficient_matrix, constant_matrix, pivot):
    A = coefficient_matrix.astype(float)
    b = constant_matrix.astype(float)
    A,b = row_scaling(A,b,1/A[pivot],pivot[0])
    for k in range(pivot[0]): 
        A,b = row_replacement(A,b,-A[k,pivot[1]],k,pivot[0])
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

def RREF(coefficient_matrix, constant_matrix):
    A,b,pivots = forward_phase(coefficient_matrix,constant_matrix)
    return backward_phase(A,b,pivots)


def Null(matrix,tol=1e-8):
    #returns null, that is, returns a basis for the null space of matrix

    A = matrix.astype(float)
    m,n = A.shape

    zeros = np.zeros((m,1))
    R,_ = RREF(A,zeros)

    R[np.abs(R) < tol] = 0.0

    pivot_cols = []
    for i in range(m):
        row = R[i]
        nz = np.where(np.abs(row) > tol)[0]
        if nz.size > 0:
            pivot_cols.append(int(nz[0]))
    pivot_cols = list(dict.fromkeys(pivot_cols))
    free_cols = [j for j in range(n) if j not in pivot_cols]

    if not free_cols:
        return np.zeros((n,0))
    
    basis = []
    for free_col in free_cols:
        v = np.zeros(n)
        v[free_col] = 1.0

        for row_idx, pc in enumerate(pivot_cols):
            s = 0.0
            for j in free_cols:
                s += -R[row_idx,j]*1.0
            v[pc] = -s
        basis.append(v)

    return np.array(basis).T


def Eigenspace(matrix,eigenvalue, tol=1e-8):
    #returns eigenspace, that is, 
    #returns a basis for the eigenspace of matrix with respect to eigenvalue

    A = matrix.astype(float)
    n = A.shape[0]
    return Null(A - eigenvalue*np.identity(n), tol=tol)


def Diagonalize(matrix,eigenvalues):
    #returns diagonalization, that is, 
    #returns three matrices P, D, P^-1 such that matrix = PDP^-1 and D is diagonal
    #If a diagonalization is not possible, it will report the error, "No diagonalization possible."

    A = matrix.astype(float)
    n = A.shape[0]

    vals = np.unique(np.round(eigenvalues, 6))
    eigvecs = []
    diag_entries = []

    for lam in vals:
        E = Eigenspace(A, lam, tol=1e-8)  
        if E.size == 0:
            continue
        for j in range(E.shape[1]):
            eigvecs.append(E[:, j])
            diag_entries.append(lam)

    if len(eigvecs) != n:
        return "No diagonalization."

    P = np.column_stack(eigvecs)
    D = np.diag(diag_entries)
    P_inv = np.linalg.inv(P)

    return P, D, P_inv


### VERIFY ############################
print("Task 1")
A = np.array([[17,5,5],
              [-41,-12,-14],
              [-19,-6,-4]])
lambdas = np.round(np.linalg.eigvals(A),6)
for lamb in set(lambdas):
    print(lamb, Eigenspace(A,lamb))
print("\n")  

B = np.array([[6,10,0,-4],
              [3,5,0,-2],
              [12,24,-1,-8],
              [15,30,0,-11]])
lambdas = np.round(np.linalg.eigvals(B),6)
for lamb in set(lambdas):
    print(lamb, Eigenspace(B,lamb))
print("\n")  

print("Task 2")
C = np.array([[8,20,10],
              [5,-12,5],
              [5,10,3]])

lambdas = np.round(np.linalg.eigvals(C),6)
print(Diagonalize(C,lambdas))            
import numpy as np

#implement zero below on an augemented matrix
#implement zero above on an augmented matrix

def row_scaling(coefficient_matrix, augmented_matrix, scalar, i):
    #A | b, copy to avoid altering
    scaled_coefficient_matrix = coefficient_matrix.astype(float).copy()
    scaled_augmented_matrix = augmented_matrix.astype(float).copy()

    scaled_coefficient_matrix[i,:] *= scalar
    scaled_augmented_matrix[i] *= scalar

    scaled_constant_matrix = scaled_augmented_matrix
    return scaled_coefficient_matrix, scaled_constant_matrix 


def row_replacement(coefficient_matrix, augmented_matrix, scalar, i, j):
    replaced_coefficient_matrix = coefficient_matrix.astype(float).copy()
    replaced_constant_matrix = augmented_matrix.astype(float).copy()
    replaced_coefficient_matrix[i,:] += scalar * replaced_coefficient_matrix[j,:]
    replaced_constant_matrix[i] += scalar * replaced_constant_matrix[j]

    return replaced_coefficient_matrix, replaced_constant_matrix


def row_interchange(coefficient_matrix, augmented_matrix, i, j):
    interchanged_coefficient_matrix = coefficient_matrix.copy()
    interchanged_constant_matrix = augmented_matrix.copy()
    interchanged_coefficient_matrix[[i,j], :] = interchanged_coefficient_matrix[[j,i], :]

    interchanged_constant_matrix[[i,j]] = interchanged_constant_matrix[[j,i]]

    return interchanged_coefficient_matrix, interchanged_constant_matrix


########### NEW CODE #####################
def zero_below(coefficient_matrix, constant_matrix, pivot):
    #coefficient matrix = A
    #constant_matrix = b,  [A | b]
    #pivot point (i,j)

    A = coefficient_matrix.astype(float)
    b = constant_matrix.astype(float)
    i, j = pivot
    pivot_value = A[i,j]

    #python hint, check for exact 0
    conditional = 1e-6

    if abs(pivot_value) < conditional: #abs numpy
        for k in range(i + 1, len(A)):
            if abs(A[k,j]) > conditional:
                A, b = row_interchange(A,b,i,k)
                pivot_value = A[i,j]
                break

        for k in range(i + 1, len(A)):
            if abs(A[k,j]) > conditional:
                scalar = -A[k, j] / pivot_value
                A,b = row_replacement(A, b, scalar, k, i)
            
        return A, b    



def zero_above(coefficient_matrix, constant_matrix, pivot):
    #write your code here

    A = coefficient_matrix.astype(float)
    b = constant_matrix.astype(float)
    i, j = pivot
    pivot_value = A[i,j]

    conditional = 1e-6

    if abs(pivot_value) > conditional:
        A, b = row_scaling(A,b,1 / pivot_value, i)

        for k in range(i):
            if abs(A[k,j]) > conditional:
                scalar = -A[k,j]
                A,b = row_replacement(A,b,scalar,k,i)

        return A,b



### VERIFICATION ############################
aug_matrix = lambda A,B : np.array([np.concatenate((A[i],B.reshape(len(A),-1)[i])) for i in range(len(A))])

A = np.array([[0,2,3],[5,6,7], [9,10,11]])
b = np.array([4, 8, 12])
Ab = aug_matrix(A, b)
print(Ab, "\n")

#row reduce below using (1,1) pivot
A, b = zero_below(A,b,(0,0))
print(aug_matrix(A, b), "\n")

#row reduce below using (3,3) pivot
A, b = zero_above(A, b,(2,2))
print(aug_matrix(A, b))
import numpy as np

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

### VERIFICATION ############################
aug_matrix = lambda A,B : np.array([np.concatenate((A[i],B.reshape(len(A),-1)[i])) for i in range(len(A))])

A = np.array([[1,2,3],[5,6,7], [9,10,11]])
b = np.array([4, 8, 12])
Ab = aug_matrix(A, b)
print(Ab, "\n")

#scale Row 2 by 3
scaled_A, scaled_b = row_scaling(A,b,3,1) 
print(aug_matrix(scaled_A, scaled_b), "\n")

#replace Row 3 with Row 3 - 9*Row 1
replaced_A, replaced_b = row_replacement(A,b,-9,2,0)
print(aug_matrix(replaced_A, replaced_b), "\n")

#interchange Row 2 and Row 3
interchanged_A, interchanged_b = row_interchange(A,b,1,2)
print(aug_matrix(interchanged_A, interchanged_b), "\n")
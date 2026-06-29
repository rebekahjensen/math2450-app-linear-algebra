import numpy as np

#compute the adjacency matrix of illustrated graph
#analyze random walks beginning at vertex A
#analyze random walks beginning at vertex B


### Task 1 ################
print("~Task 1~")
A = np.zeros((6, 6), dtype = int) 
edges = [(0, 1), (0, 4), (0, 5), (1, 2), (1, 3), (1, 5), (2, 3), (2, 4), (3, 4), (4, 5)]
for i, j in edges:
    A[i, j] = 1
    A[j, i] = 1

print(f"Adjacency Matrix\n {A}\n")


### Task 2 ###############################
print("~Task 2~")
k=100
degrees = np.sum(A, axis = 1)
T = A/degrees[:, None]
print(f"Transition Matrix\n {T}\n")
print() #What is the relationship between these two matrices?

print("Starting at vertex A")
X = np.zeros((k+1,6))
X[0] = np.array([1,0,0,0,0,0])

for t in range(k):
    X[t+1] = X[t] @ T

#Create a linear dynamical system X such that X[t] is the 6-vector of probabilities that a person following a random walk will be at vertex A after t steps.

print(f"x_3 = {X[3]}\nx_10 = {X[10]}\nx_100 = {X[100]}")
print() #What pattern do you see emerging? 


### Task 3 ###############################
print("~Task 3~")
print("Starting at vertex B")

X = np.zeros((k+1,6))
X[0] = np.array([0,1,0,0,0,0])
for t in range(k):
    X[t+1] = X[t] @ T  


print(f"x_3 = {X[3]}\nx_10 = {X[10]}\nx_100 = {X[100]}")
print() #What pattern do you see emerging?) 

#What happens if another vertex is the starting location? 
print("The distribution will still converge to the same steady-state distribution.")
#Make a conjecture about X[t] as t -> infinity. 
print("As t approaches infinity, X[t] converges to a steady-state distribution regardless of the starting vertex.")
#How could this information had been gleaned from the original graph in retrospect?
print("Overtime the random walk will evenly distribute across all vertices.")
print() 
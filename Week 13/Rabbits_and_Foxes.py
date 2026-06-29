import numpy as np

T= 20 # number of years 
A = np.array([[1.9, -8],    #transition matrix for predator-prey model
              [0.1,0.1]])

X = np.zeros((2,T+1,2))     #Initialization of 2 dynamical systems: X[0] and X[1]
                            #X[0] is simulation without new hunting tags
                            #X[1] is simulation with new hunting tags
X[0,0] = np.array([100,12]) #initial state: rabbits, foxes by thousands
X[1,0] = X[0,0]

#construct the dynamical systems X[0] without tags and X[1] with tags here

for t in range(T):
    #without new hunting tags
    X[0,t+1] = A @ X[0,t]

    #with new hunting tags
    hunting_effect = np.array([0, -0.1])
    X[1,t+1] = A @ X[1,t] + hunting_effect


### GRAPHING ############################
import matplotlib.pyplot as plt
labels = ['Without New Tags', 'With New Tags']
for i in range(2):
    plt.plot(np.arange(len(X[i])), X[i,:,0], "-")
    plt.plot(np.arange(len(X[i])), X[i,:,1], "--")
    plt.xlabel(labels[i])
    plt.xlim(0,T)
    plt.ylim(0,300)
    plt.legend(['Rabbit', 'Foxes'])
    plt.show()
    print(f"Population of Rabbits and Foxes over {T} years {labels[i]}:")
    print(X[i,:,0])
    print(X[i,:,1],"\n")
    
### FINAL ANSWER #########################

print("Based on these models, new hunting tags lower the population of foxes over time. It makes the ecosystem between the foxes and rabbits very unstable after time.")
print("When there are no new hunting tags, the predator-prey relationship between the foxes and rabbits stays stable.")
print("Due to the data, I am pro-fox, to help the ecosystem remain stable.")
print("This information shows us that hunting regulations make a large impact on wildlife populations, so it's important to be very mindful of them.")
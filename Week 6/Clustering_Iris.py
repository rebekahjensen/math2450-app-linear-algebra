import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.stats import mode
from sklearn.cluster import KMeans

#task 1:
#prediction:
#the flowers will cluster into 3 groups bc k = 3, since there are 3 flowers, they will likely sort & cluster decently well on the graph
#the data is sorted in 4 features (name, type, feature, data)
#I predict that the Setosa flower will be more prominent in the chart when sorted
#because the difference between petal size is larger than the other 2 flowers


#150 splt 3 ways (50,50,50)
k = 3 #clusters
iris_names = load_iris()['target_names'] 
iris_types = load_iris()['target'] 

iris_feature = load_iris()['feature_names'] #sepal length and width, petal length and widt
iris_data = np.array(load_iris()['data']) 
print(iris_names)
print(iris_types)
print(iris_feature)
print(iris_data)

X_iris = iris_data 
plt.ion() 

X = np.concatenate([[0.3*np.random.randn(2) for i in range(100)], 
                    [[0,1] + 0.5*np.random.randn(2) for i in range(100)], 
                    [[1,1] + 0.4* np.random.randn(2) for i in range(100)],
                    [[1,-1] + 0.3* np.random.randn(2) for i in range(100)],
                    [[-0.5,1] + 0.25* np.random.randn(2) for i in range(100)],
                    [[0.5,-1] + 0.1* np.random.randn(2) for i in range(100)],
                    [[0.5,-0.5] + 0.3* np.random.randn(2) for i in range(100)],
                    [[1,-0.25] + 0.25* np.random.randn(2) for i in range(100)],
                    [[1.75,-0.75] + 0.2* np.random.randn(2) for i in range(100)],
                    [[1,0] + 0.5* np.random.randn(2) for i in range(100)]])



kmeans = KMeans(n_clusters=k, random_state=0).fit(iris_data)
labels = kmeans.labels_ #assignments
reps = kmeans.cluster_centers_ 
J_clust = kmeans.inertia_ #objectives   
print(J_clust)


#plot
grps = [[X_iris[i,:] for i in range(len(X_iris)) if labels[i]==j] for j in range(k)]
for i in range(k):
    plt.scatter([c[0] for c in grps[i]],[c[1] for c in grps[i]])
#plt.xlim(-2,3)
#plt.ylim(-2,3)
plt.show(block = True)


#look for errors
mapping = {} 
for cluster in range(k):
    mask = labels == cluster
    true_labels = iris_types[mask]
    mapping[cluster] = mode(true_labels, keepdims=True)[0][0]

predicted_as_true = np.array([mapping[label] for label in labels]) #predict clusters
errors = np.sum(predicted_as_true != iris_types) 
accuracy = 1 - errors / len(iris_types)

print("Error number:", errors, "out of", len(iris_types)) #printing errors
print("Accuracy:", round(accuracy * 100, 2), "%")

#task 2
#I think it ended up clustering pretty well and as I suspected. The Setosa flower clusters much more distinctly than the other 2
#it's clear which one is Setosa and which ones are the other two based on how the data points cluster
#this happened because Setosa is more detailed than the other 2 flowers, so it's more drawn to its own category as opposed to the more alike flowers
#I'm sure we have ran this a bunch it would cluster the points more accurately. It takes time to learn.
#It looks like there were 17/150 errors and the accuracy was 88.67%, which is pretty good. It takes time to learn and be better.



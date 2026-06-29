import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

###### EXERCISE 1 ####################
# Using the k-means algorithm, find a clustering for which J^clust < epsilon, for epsilon = 5.208, k = 4. 
# Report your initial representatives, your final representatives, your final clustering assignment, and the final clustering objective.
X = np.array ([ [1,2,3], [4,5,6], [1,2,0], [0,0,3], [3,2,1], [2,2,0], [0,5,0], [2,3,1], [6,6,4], [9,3,2], [2,3,4], [7,5,0], [ 2,7,8] ], dtype = float)

#try to get Jclust smaller than e...
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

epsilon = 5.208 #JCLust smaller than e

for seed in [0,1,4,6,8,11,42]: #attempt
    #library
    kmeans = KMeans(n_clusters = 4, init = "random", random_state = seed, n_init = 1)
    kmeans.fit(X_scaled)

    print("Initial Representatives (random seed): ", seed)
    print("\nFinal Representatives (centroids):\n", kmeans.cluster_centers_)
    print("\nCluster Assignments:\n", kmeans.labels_)
    print("\nFinal Clustering Objective (J^clust / inertia):\n", kmeans.inertia_)

    if kmeans.inertia_ < epsilon: 
        print("Requirement passed! JClust = ", kmeans.inertia_, "< Epsilon = ", epsilon, "\nGreat work!")
        break


###### EXERCISE 2 ####################
# Consider the following data set of n = 100 vectors.
# Compute three different clusterings for k= 3, 4, 10 using three different randomized initializations each (hence nine clusterings). 
# To report your clustering include a colored graphic illustrating the clustering (as demonstrated in https://github.com/emisseldine/OpenLinear/blob/main/Chapter4/code/kmeans), 
# list the cluster representatives, and the final clustering objective for each of these three clusterings. 
# Explain which clustering was the best of the nine.  

import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')

#100 vectors :)
X = np.array([[ 0.011499775310454985, -0.06353071139753803],
[ -0.26806860191340304, -0.0911109519553983],
[ -0.33192608299119314, -0.25633299184031716],
[ -0.1807122247382386, 0.4407823656766903],
[ 0.04755725914233897, -0.26038121782191964],
[ -0.2218959599585165, -0.46445115145460325],
[ -0.15720062347314487, 0.09831127821772508],
[ -0.11737628492132425, 0.06322469336557392],
[ -0.254182338438016, 0.46248410082371066],
[ -0.43909490168823184, 0.5809660426246169],
[ 0.21176006985732831, 1.048406087811497],
[ 0.19173151514779985, 1.5772962591069986],
[ 0.2971332017652109, 1.064039078904691],
[ 0.07917226251135184, 0.7490554663368822],
[ 0.2639118824928691, 1.0752542053739997],
[ 0.5372977696283332, 1.036769283189558],
[ 0.4181336907917003, 1.0237111890602981],
[ -0.16251880690627085, 0.8678728394531069],
[ -0.3189020635774326, 1.1795889910940704],
[ -0.5075626762419931, 0.7988086283167466],
[ 0.8269182622564538, 0.9376481206189049],
[ 0.7062514580575565, 0.737016926160736],
[ 0.9660731848931493, 1.126927004885705],
[ 1.1773296447091877, 1.2757715193118528],
[ 1.756214210380178, 1.256692979216825],
[ 1.2699540575385448, 1.2117029396254702],
[ 0.7885165513053876, 0.9598620938111682],
[ 1.6890809127526807, 1.4200118857511428],
[ 1.5752834475149737, 1.2789676692023715],
[ 1.0523805196933704, 1.5434544502126877],
[ 1.2259106600330734, -0.8978919255273496],
[ 0.7253402516314809, -0.7283452009098872],
[ 0.32263393466087575, -0.8460795086539056],
[ 1.0201501479429478, -1.7182430376269078],
[ 0.5323002483607984, -1.1321713406135534],
[ 1.3254747787720103, -0.8587676896616584],
[ 1.4078032219972128, -0.5616177786632082],
[ 1.7316474350015025, -0.9176614871654156],
[ 1.184685490546223, -1.3851624548168016],
[ 0.9513289656008778, -0.7611989358689963],
[ 0.018610029113234172, 0.9538085232074225],
[ -0.446631451896232, 1.0954399045781975],
[ -0.2527719861344526, 0.5477101309865007],
[ -0.30934040367505067, 1.23047363046694],
[ -0.9611101507006983, 0.8322061573342004],
[ -0.5546657032971068, 1.3501952708531475],
[ -0.6524149234749772, 0.9369781770811536],
[ -0.6409264016654703, 1.0903088056413974],
[ -0.5123635803793734, 1.0638675129226425],
[ -0.4190676184921376, 1.0588171245871274],
[ 0.703284915870159, -1.0068331196347922],
[ 0.40447124150341984, -1.037670286112816],
[ 0.5296648386558154, -1.0492904103781007],
[ 0.551113009969552, -0.9598377076582264],
[ 0.4967557047378246, -1.1589919233307204],
[ 0.36520358569991734, -1.0022616314100707],
[ 0.3778351990362021, -1.1293152998298237],
[ 0.6021294680591185, -0.975894520948475],
[ 0.6280584918977341, -1.1558240317054445],
[ 0.509641922560463, -0.9929632629694748],
[ 0.1630855255770059, -0.7335233863877533],
[ 0.6169167547080051, -0.473549644614539],
[ 0.7330276629198617, -1.0145822739738608],
[ 0.6722185626314987, -0.5065969505854474],
[ 0.571994529046489, -0.6257916296234889],
[ 0.21080756579677795, -0.7711100514491268],
[ 0.2474329288688758, -0.3303369462067695],
[ 0.38048626001895547, -0.23143849230707148],
[ 0.7578823745272825, -0.9324635843838731],
[ 0.42666058023235054, -0.49396340598220817],
[ 0.9585756837331035, -0.3409137133391019],
[ 1.0155270840916915, -0.08959069274407203],
[ 0.9342222413847283, -0.11858339351461941],
[ 0.8223020301806827, -0.16670599706753103],
[ 0.9509725646078434, 0.27124055703943317],
[ 1.3082380420505269, -0.31891623348821707],
[ 0.555120274183072, -0.14368370321260343],
[ 0.7678617910000151, -0.5870573626649148],
[ 1.1089885851947607, -0.20284644740530453],
[ 0.9779116200022511, -0.2143500423668491],
[ 1.8232965408889554, -0.2547468789278462],
[ 1.7331387086985606, -0.9104359881393999],
[ 1.7816026449351243, -0.8481857265272674],
[ 1.8445924743295163, -0.8863371822827776],
[ 1.6887871627480715, -1.1066462275084639],
[ 1.8097727990186252, -1.010976866612518],
[ 1.5809744384796107, -0.567877345593579],
[ 1.702596860805505, -0.6775092192418015],
[ 1.7715589402384084, -0.8285201819477293],
[ 1.981445811412673, -0.5080652659333683],
[ 0.2527588733027669, 0.03153075046393112],
[ 0.8718660495889615, -0.09339204334051672],
[ 0.13808126159426448, -0.4050854226605656],
[ 1.082730783251869, -0.06186079623704191],
[ 1.4061282817773362, -1.1623031997546525],
[ 0.26715842314763183, 0.543541991706253],
[ 0.9971507373413223, -0.02725845958354786],
[ 0.9543829638283083, 0.16866762403852925],
[ 0.9045006628426874, -0.05835140413310361],
[ 0.4372646513678142, -0.8876586880633819]], dtype = float)


#plotting
plt.figure(figsize = (5,5))
plt.scatter(X[:,0], X[:,1])
plt.title("100 Vectors")
plt.show()

#use k = 3,4,10
ex_ks = [3,4,10]
random_states = [0,21,42]
results = []

#seed rand initial
for k in ex_ks:
    for seed in random_states:
        kmeans = KMeans(n_clusters = k, random_state = seed, n_init = 10).fit(X)
        labels = kmeans.labels_
        reps = kmeans.cluster_centers_
        J_clust = kmeans.inertia_

        results.append((k, seed, reps, J_clust))

        grps = [[X[i,:] for i in range(len(X)) if labels[i] == j] for j in range(k)]
        plt.figure(figsize=(5,5))
        for i in range(k):
            plt.scatter([c[0] for c in grps[i]], [c[1] for c in grps[i]], label = f"Cluster {i}")
        plt.scatter(reps[:,0], reps[:,1], c= "blue", marker = "x", s = 100, label = "Centroids")
        plt.title(f"k = {k}, seed = {seed}, J = {J_clust:.3f}")
        plt.legend()
        plt.show()

        plt.close()


#explain which clustering was the best of the nine

#since I tested random centroids as initial reps, this is going to run different each time
#but as of this run, of the 9 attempts, the best clustering was when k = 4 and rand seed = 0, which made JClust = 0.8652
#this one was the best because it fulfilled our requirement by having the smallest clustering objective
#the points are grouped tightly around the centroids!
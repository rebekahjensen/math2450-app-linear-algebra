import numpy as np

def ranking(names, scores): #A function to sort the names of mathletes by their scores.
    ranks = []
    temp_scores = scores.copy()
    temp_names = names.copy()
    for i in range(len(names)):
        winner = np.argmax(temp_scores)
        ranks.append(temp_names[winner])
        temp_names.remove(temp_names[winner])
        temp_scores.remove(temp_scores[winner])
    return ranks
        
names = ["Pete Weyl", "Karla Gauss", "Hermie Wielandt", "Artie Cayley", "Emmy Noether", 
"Evie Galois", "Rowan \"Quaternion\" Hamilton", "Dave Hilbert", "Sophie Lie", "Jorge Frobenius", 
"Izzy Schur", "Stevie Humphries", "Mikey Muzychuk", "Manny Leung", "Ollie Tamaschke"]

X = np.array([[11,  9, 10, 13, 30], #Pete Weyl
               [ 7, 17, 10,  1, 11],#Karla Gauss
               [26, 22, 11, 22, 10],#Hermie Wielandt
               [13, 25,  7,  1, 13],#Artie Cayley
               [13, 9, 18, 14, 5],  #Emmy Noether
               [ 4, 14, 10, 25,  0],#Evie Galois
               [ 9, 21, 8, 22, 19], #Rowan "Quaternion" Hamilton
               [30, 14,  7, 24, 16],#Dave Hilbert
               [ 3,  7, 18,  5, 11],#Sophie Lie
               [28, 11, 25,  9, 20],#Jorge Frobenius
               [27, 11, 29,  2, 13],#Izzy Schur
               [ 7, 4, 10, 12, 10], #Stevie Humphries
               [14,  2,  5,  4, 2], #Mikey Muzychuk
               [ 5,  2, 11, 10, 10],#Manny Leung
               [ 3, 19, 14, 19, 9]])#Ollie Tamaschke

### TASK 1 #####################

p = (5,4,3,2,1) #1st, 2nd, 3rd, 4th, 5th

# scores = p*X[0:15] #print all scores :)
# print(scores)
# print((names[0:15]), X[0:15])

scores = (X @ np.array(p)).tolist()
winners = ranking(names, scores)

print("Task 1 Ranking: ")

for i in range(len(names)):
    # print(scores[names.index(winners[i])],winners[i])
    #I want to make the print look better
    print(f"{i+1}. {winners[i]}: {scores[names.index(winners[i])]}")
print("\n")


### TASK 2 #####################
p = (7,4,3,1,1) #1,2,3,4,5

scores = (X @ np.array(p)).tolist()
# print(scores)

winners = ranking(names, scores)
print("Task 2 Ranking: ")

for i in range(len(names)):
    print(f"{i+1}. {winners[i]}: {scores[names.index(winners[i])]}")
          
print("\n")

#QUESTIONS:
#Compare this ranking to the official ranking you computed above. 
#What significant differences do you observe? 
#Why did they change?  

#ANSWERS:
#I noticed that some participant's rankings shifted, especially the ones who were doing well in task 1
#for example, p = (5,4,3,2,1) in task 1. These weights helped participants who scored decently in all placements succeed
#p = (7,4,3,1,1) in task 2, 1st place was heavier, so those who succeeded in 1st place ranked the best
#this happened because changing p point vectors changed the distribution significantly
#(X @ p) 


### TASK 3 ##

#required that p1 >= p2 >= p3 >= p4 >= p5 >= 0 sooo...
p = (1,0,0,0,0) #1,2,3,4,5

#Create two other point vectors to result in two other 
#different MVP winners (not including the two winners from the 
#two previous vectors).
scores = (X @ np.array(p)).tolist()


#write your code here to compute scores
winners = ranking(names, scores)
print("Task 3.1 Ranking: ")

for i in range(len(names)):
    print(f"{i+1}. {winners[i]}: {scores[names.index(winners[i])]}")
print("\n")


#TASK 3.2
p = (1,1,1,0,0) #1,2,3,4,5

#Create two other point vectors to result in two other 
#different MVP winners (not including the two winners from the 
#two previous vectors).
scores = (X @ np.array(p)).tolist()

print("Task 3.2 Ranking: ")
winners = ranking(names, scores)
for i in range(len(names)):
    print(f"{i+1}. {winners[i]}: {scores[names.index(winners[i])]}")

print("\n")

#JORGE STAYS WINNING!!! #MVP 

# #Is there a point vector for which Manny Leung does not get last place?
#yes, in task 3.1, where p = (1,0,0,0,0), Manny is NOT last place
#he is NOT last place because the scoring system in p only cares about 1st place points

print("Manny is NOT last place when p = (1,0,0,0,0)")
print("\n")

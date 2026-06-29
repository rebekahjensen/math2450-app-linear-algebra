import numpy as np

### TASK 1 ###################
#find angle between vectors w/ dot products
#np.linealg.norm(u,v) = legnth of vectors
#np.dot(u,v) = scalar (dot product)
#remember that arccos is cos^-1
angle = lambda u,v : np.arccos(np.dot(u,v) / (np.linalg.norm(u) * np.linalg.norm(v))) 

u = np.array([6,-1])
v = np.array([1,4])
print("Radians: " ,(angle(u,v)), "Degrees: ", (angle(u,v)*180/np.pi))
#should be 85.43 degrees and 1.491 radians

## TASK 2 ###################
CC= np.array([37.6775, -113.0619]) #Cedar City
Pusan = np.array([35.2100, 129.0689]) #Pusan, South Korea

r = 6367.5 #Radius of Earth in km

#converts latitude/longitude coordinates into a vector in R^3
convert_coord = lambda coords, radius : np.array([radius*np.sin(coords[1]*np.pi/180)*np.cos(coords[0]*np.pi/180), 
              radius*np.cos(coords[1]*np.pi/180)*np.cos(coords[0]*np.pi/180), 
              radius*np.sin(coords[0]*np.pi/180)])

CC_vec = convert_coord(CC,r) #cedar city & earth's radius
Pusan_vec = convert_coord(Pusan,r)
#find dot product, length, divide by CC_vec, multiply by Pusan_vec
angle_CP = np.arccos(np.dot(CC_vec, Pusan_vec) / (np.linalg.norm(CC_vec)* np.linalg.norm(Pusan_vec)))
print(r*angle_CP, "is the spherical distance between Cedar City and Busan.") 
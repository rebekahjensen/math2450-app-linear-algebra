# requesting the image from github
def get_image(url):
  import io
  import requests as re
  from PIL import Image

  get = re.get(url) # fetch the image
  img_bytes = io.BytesIO(get.content) # create propper binary object
  img = Image.open(img_bytes) # parse image to an image object

  return img
#%%
import matplotlib.pyplot as plt
import numpy as np

url = r'https://raw.githubusercontent.com/emisseldine/OpenLinear/main/Chapter6/images/bookcover.png'
cover = np.asarray(get_image(url))[:,:,0]
color = 'Blues_r' 

# processing image
plt.figure(figsize=(9,6))
plt.imshow(cover,cmap=color)
plt.axis('off')
plt.show()

#%% Task 1
U,sigma,VT = np.linalg.svd(cover,full_matrices=False)

#%% Task 2
num_vals = [1,2,3,4,5,10,25,100,200,300,400,500,1000,1500,2000]
for k in num_vals:
    blur = (U[:,:k] @ (np.diag(sigma[:k]) @ VT[:k,:]))
    plt.imshow(blur,cmap=color)
    plt.title(f"k = {k}")
    plt.axis('off')
    plt.show()
#Analyze the quality of an image compared to data savings
print()

#%% Task 3
m,n = cover.shape
k = int(0.9*m*n/(m+n+1))
#the rank at which the singular reduction obtains 90% of the original image's size
blur = (U[:,:k] @ (np.diag(sigma[:k]) @ VT[:k,:])) #compute the rank-k singular reduction of blur
plt.figure(figsize=(9,6))
plt.imshow(blur,cmap=color)
plt.title(f"k = {k}")
plt.axis('off')
plt.show()
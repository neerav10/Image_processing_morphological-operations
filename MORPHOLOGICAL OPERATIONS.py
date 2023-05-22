#Neerav Desai 
#basic morphological operations
#%%
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
#%% import and display
img= Image.open(r"") #Include you image path 
plt.subplot_tool()
plt.subplot(3,3,1)
plt.axis("off")
plt.title('Original')
plt.imshow(img)
#%%conv colour img into gray scale
gray_img = img.convert('L')
plt.subplot(3,3,2)
plt.axis("off")
plt.title('Gray')
plt.imshow(gray_img)

#%%array Image
a=np.array(gray_img)
#%%dilation
b= ndimage.binary_dilation(a, structure=np.ones((3,3))).astype(a.dtype)
plt.subplot(3,3,3)
plt.axis("off")
plt.title('Dilated')
plt.imshow(b)
#%%Erosion
se= np.ones((3,3))
c=ndimage.binary_erosion(a,se).astype(a.dtype)
plt.subplot(3,3,4)
plt.axis("off")
plt.title('Eroded')
plt.imshow(c)
#%%opening
d=ndimage.binary_dilation(c,se).astype(a.dtype)
plt.subplot(3,3,5)
plt.axis("off")
plt.title('opening')
plt.imshow(d)
#%%closing
e=ndimage.binary_erosion(b,se).astype(a.dtype)
plt.subplot(3,3,6)
plt.axis("off")
plt.title('closing')
plt.imshow(e)
#%%hit or miss
w = np.ones((3,3)).astype(a.dtype)
hit_miss = ndimage.binary_hit_or_miss(a,w)
plt.subplot(3,3,7)
plt.axis("off")
plt.title('hit or miss')
plt.imshow(hit_miss)
#%%boundary Extraction
b_t = b-c
plt.subplot(3,3,8)
plt.axis("off")
plt.title('boundary')
plt.imshow(b_t)

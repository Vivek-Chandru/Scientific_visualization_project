
"""
Created on Sun Sep  8 12:18:39 2019

Author: Vivek Chandrasekaran
Title : Scientific Visualization Project 1
Description: Wood_2 image filtering and counting the rings in the wood pattern
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
import scipy.misc as misc

def Red(image):        # Variables received as parameters
    image[:,:,1] = 0   # Making green content 0
    image[:,:,2] = 0   # Making blue content 0
    return image       # Returning the image
    
# function for creating green content image
def Green(image):
    image[:,:,0] = 0   # Making red content 0
    image[:,:,2] = 0   # Making blue content 0
    return image
        
# function for creating blue content image
def Blue(image):
    image[:,:,0] = 0   # Making red content 0
    image[:,:,1] = 0   # Making green content 0
    return image

# function for creating gray image
def Gray(image):
    # Luminosity average for getting agray image
    avg = np.dot(image[...,:3], [0.299, 0.587, 0.114]) 
    # Storing the average 2-d in all 3 axes
    image[:,:,0] = avg  
    image[:,:,1] = avg
    image[:,:,2] = avg
    return image


im = plt.imread('wood_2.bmp')

# Converting to red
# Creating a copy in another variable without passing the pointer
im1 = deepcopy(im)   
red = Red(im1)       # Calling the Red function
misc.toimage(red).save('Red.bmp') # Saving red content image
plt.imshow(red)  

# Converting to blue
im2 = deepcopy(im)
blue = Blue(im2)     # Calling the Blue function
misc.toimage(blue).save('Blue.bmp') # Saving blue content image
plt.figure()         # For creating another figure window
plt.imshow(blue)

im3 = deepcopy(im)
green = Green(im3)     # Calling the Blue function
misc.toimage(green).save('Green.bmp') # Saving green content image
plt.figure()         # For creating another figure window
plt.imshow(green)


# Converting to gray
im4 = deepcopy(im)
gray = Gray(im4)     # Calling the Gray function
misc.toimage(gray).save('Gray.bmp') # Saving gray content image
plt.figure()
plt.imshow(gray)


#Gaussian filtering to smoothen disturbance
im5=deepcopy(im)
gauss = cv2.GaussianBlur(im5,(3,3),0)
misc.toimage(gauss).save('Gauss.bmp') # Saving gaussian filtered content image

#Caonsidering Gaussian blur image to convert to gray scale and laplace filter
im = plt.imread('Gauss.bmp')

# Converting to gray
im4 = deepcopy(im)
gray = Gray(im4)     # Calling the Gray function
misc.toimage(gray).save('Gray2.bmp') # Saving gray content image


#laplace filtering
im = plt.imread('Gray2.bmp')
im5 = deepcopy(im)
laplacian = cv2.Laplacian(im5,cv2.CV_64F)
misc.toimage(laplacian).save('lap_fil.bmp') # Saving blue content image
#plt.figure()         # For creating another figure window
#plt.imshow(laplacian)

#reading the filtered image to find the size in pixels
imx = cv2.imread('lap_fil.bmp',0)
size = np.ones(2)
size[0] = len(imx);
size[1] = len(imx[0])
print('----------------------------------')
print('RESULTS')
print('----------------------------------')
print('Size of the image in pixels is') #Displaying the size
print('Rows = ',size[0])
print('Columns = ',size[1])
print('----------------------------------')

##Centering
#imy = cv2.imread('wood_2.bmp',0)
#centering = deepcopy(imy)
#centering[1020,:]= 0 #horizontal black crosshair
#centering[:,900] = 0 #vertical black crosshair
#misc.toimage(centering).save('centering.bmp') 

#counting the number of rings in horizontal direction
c=0
for i in range (900): 
    if (imx[1020,i]>158): #checking for high intensities
        c=c+1               #variable for ring count
print('The number of rings in horizontal direction from the left end to the centre of the wood profile is',c)

#counting the number of rings in the vertical direction
#recording location of the high intensities
d=0
loc=[]
for i in range (1020):
    if (imx[i,900]>158):
            loc.append(i)
#print(loc)     

#filtering high intensities for redundancies and errors in vertical direction
r=0            
for i in range(len(loc)):
    if(loc[i]-loc[i-1]<=1):
        r=r+1           #variable to count consective pixels 
        if(r%9==0):
            d=d+1
        else:
            continue
    d=d+1               # variable for ring count
    r=0
print('The number of rings in the vertical dirtection from the top to the centre of the wood profile is',d)
print('----------------------------------')

# the average number of rings
avg= (d+c)/2
print('The average number of rings in the wwod profile is:')
print(avg)
print('----------------------------------')





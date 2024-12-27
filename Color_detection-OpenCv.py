#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import pandas as pd
import numpy as np


# In[2]:


COLOR_RANGES = {
    'red': {'lower': (0, 120, 70), 'upper': (10, 255, 255)},
    'green': {'lower': (36, 100, 100), 'upper': (86, 255, 255)},
    'yellow': {'lower': (20, 100, 100), 'upper': (30, 255, 255)},
    'black': {'lower': (0, 0, 0), 'upper': (180, 255, 50)},  # Dark colors, low value
    'white': {'lower': (0, 0, 200), 'upper': (180, 20, 255)},  # High value, low saturation
    'blue': {'lower': (94, 80, 2), 'upper': (126, 255, 255)}
}


# In[3]:


# Function to detect the color name based on HSV ranges
def detect_color(hsv_pixel):
    for color_name, ranges in COLOR_RANGES.items():
        lower = np.array(ranges['lower'], dtype='uint8')
        upper = np.array(ranges['upper'], dtype='uint8')
        if cv2.inRange(hsv_pixel, lower, upper):
            return color_name
    return "Unknown"


# In[4]:


# Mouse callback function to detect color on click
def draw_function(event, x, y, flags, param):
    global clicked, color_name
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        hsv_pixel = hsv[y:y+1, x:x+1]  # Get HSV value of the clicked pixel
        color_name = detect_color(hsv_pixel)


# In[5]:


# Read the image
image_path = 'example_image.jpg'  # Replace with your image path
img = cv2.imread(image_path)
if img is None:
    print("Error: Image not loaded. Check the file path!")
    exit()

# Resize image for easier handling
img = cv2.resize(img, (800, 600))


# In[6]:


# Convert the image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Initialize variables
clicked = False
color_name = "None"


# In[7]:


# Create a window and bind the function
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
    cv2.imshow('image', img)
    if clicked:
        # Display the detected color
        cv2.rectangle(img, (20, 20), (600, 60), (0, 0, 0), -1)
        text = f"Detected Color: {color_name}"
        cv2.putText(img, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        clicked = False
        
# Break the loop on 'Esc' key press
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()


# In[ ]:





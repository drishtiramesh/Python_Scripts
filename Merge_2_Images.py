import cv2 


img1 = cv2.imread(r'Img.jpeg', 1) 


img2 = cv2.imread(r'download.png', 1) 

# Blending the images with 0.3 and 0.7
img2r = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
img = cv2.addWeighted(img1, 0.1, img2r, 0.9, 0) 
img= cv2.resize(img,(500,500))
# Show the image 
cv2.imshow('image', img) 
cv2.waitKey(0) 

# Distroy all the window open 
cv2.distroyAllWindows() 

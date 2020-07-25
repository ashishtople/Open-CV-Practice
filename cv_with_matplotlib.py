import cv2
import matplotlib.pyplot as plt

##read image
img = cv2.imread('D:\Ashish\Projects\OpenCv\FirstTrial\sample_images\einstein.png' , 1)

img1 = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

plt.imshow(img1 , cmap='gray')
plt.title('Gray Colormap')
plt.xticks([])   ## Removes x axis numbers from image
plt.yticks([])   ## Removes y axis numbers from image
plt.show()

plt.imshow(img1)
plt.title('image with RGB')
plt.show()

plt.imshow(img1 , cmap='Blues')
plt.title('Blue colormap')
plt.show()
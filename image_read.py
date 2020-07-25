import cv2

#Read the image pixels using the below command -- > color image
img1 = cv2.imread('D:\Ashish\Projects\OpenCv\FirstTrial\sample_images\einstein.png')

##Now img1 has got thr matrix of numbers
print(img1.shape)
## Results in (512 , 900 , 3) -- > this means its color image with 3 matrics for Red , blue and green
print(type(img1))
print(img1.dtype)
## Its ndimentional array with uint8 --> unsigned integeet 8 bites -->
## min value -- >  00000000 --> 0 to max value -- >  11111111 -- > 255

#Read the image pixels using the below command -- > Grey image
img_g = cv2.imread('D:\Ashish\Projects\OpenCv\FirstTrial\sample_images\einstein.png' , 0)
print(img_g.shape)
print(type(img_g))
print(img_g.dtype)

## To view the image

#cv2.imshow('einstein', img_g)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

## To write the image
#cv2.imwrite('D:\Ashish\Projects\OpenCv\FirstTrial\sample_images\einstein_grey.png' , img_g)

############# Read and Write Image is over #####################################
#################### Lets do some linear Algebra ###############################


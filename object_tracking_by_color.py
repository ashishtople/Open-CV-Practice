import cv2
import numpy as np

def main():
    windowName = 'Preview'
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret , frame = cap.read()
    else:
        ret = False

    while ret == True:

        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)  ##HSV Hue Saturation Value -- natural colors

        ## Blue Color -->
        low = np.array([100 , 50 , 50])
        high = np.array([140 , 255 , 255])

        image_mask = cv2.inRange(hsv , low , high)

        ##Next
        low1 = np.array([170,120,70])
        high1 = np.array([180 , 255 , 255])

        img_mask1 = cv2.inRange(hsv , low1 , high1)

        mask1 = image_mask + img_mask1

        mask2 = cv2.bitwise_not(mask1)

        res1 = cv2.bitwise_and(frame , frame , mask = mask1)
        res2 = cv2.bitwise_and(frame , frame , mask = mask2)
        final_output = cv2.addWeighted(res1 , 1 , res2 , 1 , 0)

        #https://www.youtube.com/watch?v=AkY2TpvDGUo

        output = cv2.bitwise_and(frame , frame , mask = image_mask)


        cv2.imshow('Image Mask' , image_mask)
        cv2.imshow(windowName , frame)
        cv2.imshow('Color Tracking' , output)
        cv2.imshow('trial' , final_output)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    cap.release()


if __name__ == "__main__":
    main()
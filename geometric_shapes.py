
#import libraries
import cv2
import numpy as np

##empty function for trackerbar
def emptyfunction():
    print('what')

def main():
    ## Create the screen of size 512,512

    img1 = np.zeros((512,512,3), np.uint8)
    ##Give name to screen
    windowname = 'Testing OpenCV BGR Pallet'
    cv2.namedWindow(windowname)

    #Create tracker bar -- name , windowname , color , and function
    cv2.createTrackbar('B' ,windowname , 0 ,255 , emptyfunction)
    cv2.createTrackbar('G' ,windowname , 0 ,255 , emptyfunction)
    cv2.createTrackbar('R' ,windowname , 0 ,255 , emptyfunction)


    while(True):
        #to keep window screen up until user press ESC while statement is written
        cv2.imshow(windowname , img1)

        ## Position of the taskbar on user movement is captured in variables
        blue = cv2.getTrackbarPos('B' , windowname)
        green = cv2.getTrackbarPos('G', windowname)
        red = cv2.getTrackbarPos('R', windowname)

        #Full window screen is modified with the positional values from above statement
        img1[:] = [blue , green , red]
        #at run time you can see positional values using print
        #print(blue , green , red)

        #loop is broken if the ESC is pressed
        if cv2.waitKey(1) == 27:
            break
    #Once while loop is broken all windws opened are closed
    cv2.destroyAllWindows()


if __name__ =="__main__":
    main()

import cv2
import matplotlib.pyplot as plt

def  main():
    cap = cv2.VideoCapture(0)  ## setup webcam

    if cap.isOpened():          ##if cap is opened (webcam is working)
        ret, frame = cap.read()  ##ret is return variable , cap.read reads input
        print(ret)
        print(frame)
    else:
        ret = False

    img = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title('random image taken from webcam')
    plt.xticks([])
    plt.yticks([])
    plt.show()


    cap.release()  ## releases the webcam . Its mandatory to ri

if __name__ == "__main__":
    main()
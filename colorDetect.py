import numpy as np
import cv2

# Range of color
sensitivity = 20

# Function to rename multiple files 
def main():
    img = cv2.imread('test.jpg')

    # converting from BGR to HSV color space
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # Remove noise
    frame_blur = cv2.GaussianBlur(hsv.copy(), (5, 5), 3)# apply gausion blur to given frame

    # Range for green depend on sensitivity
    lower_green = np.array([60 - sensitivity, 100, 50])
    upper_green = np.array([60 + sensitivity, 255, 255])
    out = cv2.inRange(frame_blur, lower_green, upper_green)
    
    # Display
    cv2.imshow("Out",out)
    cv2.waitKey(0)

    # Clear memories
    cv2.destroyAllWindows()# Closes displayed windows
 

  
# Driver Code 
if __name__ == '__main__': 
    # Calling main() function 
    main()
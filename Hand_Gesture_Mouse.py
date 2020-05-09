import cv2
import numpy as np
import  pyautogui
area=1
cap = cv2.VideoCapture(0)
kernel = np.ones((2,2),np.uint8)

while True:
	ret, frame=cap.read() 
        # if a frame was succesfully grabbed
        if ret:
            _,frame=cap.read()

    		blurred_frame = cv2.GaussianBlur(frame,(5,5),0)
    		upper_bound = np.array([80, 80, 80])
   			lower_bound = np.array([0, 0, 0])
    		mask = cv2.inRange(blurred_frame, lower_bound, upper_bound)

    		dilation = cv2.dilate(mask, kernel, iterations=1)

    		closing = cv2.morphologyEx(dilation, cv2.MORPH_GRADIENT, kernel)
    		closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)

    # Getting the edge of morphology
    		edge = cv2.Canny(closing, 175, 175)



    		contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
   			if len(contours) != 0:
        # draw in blue the contours that were founded
        		cv2.drawContours(frame, contours, -1, 255, 3)

        # find the biggest area
        		c = max(contours, key=cv2.contourArea)
       			M = cv2.moments(c)
       			cx = int(M['m10'] / M['m00'])
        		cy = int(M['m01'] / M['m00'])
       			pyautogui.moveTo( ( 2*cx), 2*cy, 0.025)
        		x, y, w, h = cv2.boundingRect(c)
        # draw the book contour (in green)
        		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    		else:
       			print("gayi")

    		for contour in contours:
        		area = cv2.contourArea(contour)


        		if area > 20000:
            		cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
            		print("this is the areas " + str(area))

        		if (area <= 21000):
            		pyautogui.click()
    		cv2.imshow("Frame", frame)
    # cv2.imshow("blurred", blurred_frame)
    # cv2.imshow('mask', mask)
    		key = cv2.waitKey(1)
    		if key == ord('q'):
        		break

	cap.release()
	cv2.destroyAllWindows()

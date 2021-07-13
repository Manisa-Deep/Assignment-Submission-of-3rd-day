import cv2
import numpy as np 
vid=cv2.VideoCapture('pubg.mp4')
back=cv2.imread('background4.jpg')
while vid.isOpened():
	success, frame= vid.read()
	if success:
		back=cv2.resize(back, (frame.shape[1],frame.shape[0]))
		blended_vid=cv2.addWeighted(frame, 0.8, back, 0.4, gamma=0.1)
		cv2.imshow('frame',blended_vid)
		k=cv2.waitKey(50)
		if k & 0xff == ord('1'):
			back=cv2.imread('background1.jpg')
			back=cv2.resize(back, (frame.shape[1],frame.shape[0]))
			blended_vid=cv2.addWeighted(frame, 0.8, back, 0.4, gamma=0.1)
			cv2.imshow('frame',blended_vid)
			k=cv2.waitKey(50)
		if k & 0xff == ord('2'):
			back=cv2.imread('background2.jpg')
			back=cv2.resize(back, (frame.shape[1],frame.shape[0]))
			blended_vid=cv2.addWeighted(frame, 0.8, back, 0.4, gamma=0.1)
			cv2.imshow('frame',blended_vid)
			k=cv2.waitKey(50)
		if k & 0xff == ord('3'):
			back=cv2.imread('background3.jpg')
			back=cv2.resize(back, (frame.shape[1],frame.shape[0]))
			blended_vid=cv2.addWeighted(frame, 0.8, back, 0.4, gamma=0.1)
			cv2.imshow('frame',blended_vid)
			k=cv2.waitKey(50)
		if k & 0xff == ord('4'):
			back=cv2.imread('background4.jpg')
			back=cv2.resize(back, (frame.shape[1],frame.shape[0]))
			blended_vid=cv2.addWeighted(frame, 0.8, back, 0.4, gamma=0.1)
			cv2.imshow('frame',blended_vid)
			k=cv2.waitKey(50)
		if k & 0xff == ord('q'):
			break
	else:
		print('cant open vid')
		break

vid.release()
cv2.destroyAllWindows()
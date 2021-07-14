import cv2
cam=cv2.VideoCapture(0)
back_img=cv2.imread('images/background0.jpg')
while True:
	flag, frame=cam.read()
	if not flag:
		print('could not access webcam')
		break
	back_img=cv2.resize(back_img, (frame.shape[1],frame.shape[0]))
	blended_frame=cv2.addWeighted(frame, 0.8, back_img, 0.4, gamma=0.1)
	cv2.imshow('blended_frame',blended_frame)
	k=cv2.waitKey(10)
	if k & 0xff == ord('1'):
		back_img=cv2.imread('images/background1.jpg')
		back_img=cv2.resize(back_img, (frame.shape[1],frame.shape[0]))
		blended_frame=cv2.addWeighted(frame, 0.8, back_img, 0.4, gamma=0.1)
		cv2.imshow('blended_frame',blended_frame)
	if k & 0xff == ord('2'):
		back_img=cv2.imread('images/background2.jpg')
		back_img=cv2.resize(back_img, (frame.shape[1],frame.shape[0]))
		blended_frame=cv2.addWeighted(frame, 0.8, back_img, 0.4, gamma=0.1)
		cv2.imshow('blended_frame',blended_frame)
	if k & 0xff == ord('3'):
		back_img=cv2.imread('images/background3.jpg')
		back_img=cv2.resize(back_img, (frame.shape[1],frame.shape[0]))
		blended_frame=cv2.addWeighted(frame, 0.8, back_img, 0.4, gamma=0.1)
		cv2.imshow('blended_frame',blended_frame)
	if k & 0xff == ord('4'):
		back_img=cv2.imread('images/background4.jpg')
		back_img=cv2.resize(back_img, (frame.shape[1],frame.shape[0]))
		blended_frame=cv2.addWeighted(frame, 0.8, back_img, 0.4, gamma=0.1)
		cv2.imshow('blended_frame',blended_frame)
	if k & 0xff == ord('5'):
		back_img=cv2.imread('images/background5.jpg')
		back_img=cv2.resize(back_img, (frame.shape[1],frame.shape[0]))
		blended_frame=cv2.addWeighted(frame, 0.8, back_img, 0.4, gamma=0.1)
		cv2.imshow('blended_frame',blended_frame)
	if k & 0xff == ord('6'):
		back_img=cv2.imread('images/background6.jpg')
		back_img=cv2.resize(back_img, (frame.shape[1],frame.shape[0]))
		blended_frame=cv2.addWeighted(frame, 0.8, back_img, 0.4, gamma=0.1)
		cv2.imshow('blended_frame',blended_frame)
	if k & 0xff==ord('q'):
		break
cam.release()
cv2.destroyAllWindows()
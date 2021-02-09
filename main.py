import cv2

vid = cv2.VideoCapture(0)

ret, frame = vid.read()

cv2.imshow('frame', frame)


while True:
	ret, frame = vid.read()
	cv2.imshow(frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object 
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

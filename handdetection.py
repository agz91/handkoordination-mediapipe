import cv2
import config

#add VideoCapture.release() at the end of main.py

print("Importing Handdetection module...\n")

def cap_init():
	print("Initializing Cameras...\n")
	cv2.VideoCapture(1).set(cv2.CAP_PROP_FRAME_WIDTH, config.cap_frame_width)
	cv2.VideoCapture(1).set(cv2.CAP_PROP_FRAME_HEIGHT, config.cap_frame_height)

	cv2.VideoCapture(2).set(cv2.CAP_PROP_FRAME_WIDTH, config.cap_frame_width)
	cv2.VideoCapture(2).set(cv2.CAP_PROP_FRAME_HEIGHT, config.cap_frame_height)

	cv2.VideoCapture(3).set(cv2.CAP_PROP_FRAME_WIDTH, config.cap_frame_width)
	cv2.VideoCapture(3).set(cv2.CAP_PROP_FRAME_HEIGHT, config.cap_frame_height)
	print("Cameras initialized!\n")

def detectHand(camera_id):
	with config.mp_hands.Hands(
		static_image_mode=False,
		max_num_hands=2,
		model_complexity=1,
		min_detection_confidence=0.5,
		min_tracking_confidence=0.5) as hands:
		while cv2.VideoCapture(camera_id).isOpened():
			success, image = cv2.VideoCapture(camera_id).read()
			if not success:
				print("Ignoring empty camera frame.")
				continue

			image.flags.writeable = False
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			image = cv2.flip(image, 1)
			results = hands.process(image)
			if results == None:
				break
			else: return results

if __name__ == '__main__':
	cap_init()
	detectHand()
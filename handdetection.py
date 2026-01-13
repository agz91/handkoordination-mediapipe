import cv2
import config

print("Importing Handdetection module...\n")

def cap_init():
	print("Initializing Cameras...\n")
	for x in range(1,3):
		config.cam[x].set(cv2.CAP_PROP_FRAME_WIDTH, config.cap_frame_width)
		config.cam[x].set(cv2.CAP_PROP_FRAME_HEIGHT, config.cap_frame_height)
	print("Cameras initialized!\n")

def detectHand(camera_id):
	with config.mp_hands.Hands(
		static_image_mode=False,
		max_num_hands=2,
		model_complexity=1,
		min_detection_confidence=0.5,
		min_tracking_confidence=0.5) as hands:
		print("Opening camera...\n")
		while config.cam[camera_id].isOpened():
			print("Camera opened!\n")

			print("Capturing camera frame...\n")
			success, image = config.cam[camera_id].read()
			print("Capturing camera frame...\n")
			if success:
				print("Camera frame captured successfully.\n")
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
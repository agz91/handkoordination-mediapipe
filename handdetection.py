import config

print("Importing Handdetection module...\n")

def cap_init():
	print("Initializing Cameras...\n")
	config.cap1.set(config.cv2.CAP_PROP_FRAME_WIDTH, config.cap_frame_width)
	config.cap1.set(config.cv2.CAP_PROP_FRAME_HEIGHT, config.cap_frame_height)
	cap_frame_width = config.cap1.get(config.cv2.CAP_PROP_FRAME_WIDTH)
	cap_frame_height = config.cap1.get(config.cv2.CAP_PROP_FRAME_HEIGHT)

	config.cap2.set(config.cv2.CAP_PROP_FRAME_WIDTH, config.cap_frame_width)
	config.cap2.set(config.cv2.CAP_PROP_FRAME_HEIGHT, config.cap_frame_height)
	cap1_frame_width = config.cap2.get(config.cv2.CAP_PROP_FRAME_WIDTH)
	cap1_frame_height = config.cap2.get(config.cv2.CAP_PROP_FRAME_HEIGHT)
	
	config.cap3.set(config.cv2.CAP_PROP_FRAME_WIDTH, config.cap_frame_width)
	config.cap3.set(config.cv2.CAP_PROP_FRAME_HEIGHT, config.cap_frame_height)
	cap2_frame_width = config.cap3.get(config.cv2.CAP_PROP_FRAME_WIDTH)
	cap2_frame_height = config.cap3.get(config.cv2.CAP_PROP_FRAME_HEIGHT)
	print("Camera initialized!\n")

def detectHand(cap_id):
	with config.mp_hands.Hands(
		static_image_mode=False,
		max_num_hands=2,
		model_complexity=1,
		min_detection_confidence=0.5,
		min_tracking_confidence=0.5) as hands:
		while config.cap.isOpened():
			success, image = config.cap[cap_id].read()
			if not success:
				print("Ignoring empty camera frame.")
				continue

			image.flags.writeable = False
			image = config.cv2.cvtColor(image, config.cv2.COLOR_BGR2RGB)
			image = config.cv2.flip(image, 1)
			results = hands.process(image)
			if results == None:
				break
			else: return results

if __name__ == '__main__':
	cap_init()
	detectHand()
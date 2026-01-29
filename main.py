import config
import handdetection
from camera_id_extractor import get_camera_id
import cam_selector
from gesture_logic_v2 import gesture_logic
import cv2
import time
config.init()

while True:
	#image = cam_selector.find_camera()
	#for i in range(len(image)):
	#	if image[i] is not None:
	#		cv2.imshow("Show Recorded Picture", image[i])
	#		cv2.waitKey(0)
	#		cv2.destroyAllWindows()

	#gesture_id = 10
	#print(gesture_logic(gesture_id, handdetection.detectHand(get_camera_id(gesture_id))))
	#extractor.Extractor(handdetection.detectHand())
	#print(index_finger_tip_touch.INDEX_FINGER_TIP_TOUCH(handdetection.detectHand()))
	#print(index_thumb_tip_touch.INDEX_THUMB_TIP_TOUCH(handdetection.detectHand()))
	#print(thumb_middle_tip_touch.THUMB_MIDDLE_TIP_TOUCH(handdetection.detectHand()))
	#print(thumb_ring_tip_touch.THUMB_RING_TIP_TOUCH(handdetection.detectHand()))
	#print(thumb_pinky_tip_touch.THUMB_PINKY_TIP_TOUCH(handdetection.detectHand())) 
	time.sleep(1)

cv2.destroyAllWindows()
cv2.VideoCapturerelease()
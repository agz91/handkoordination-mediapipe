import config
import handdetection
from camera_id_extractor import get_camera_id
import time
from gesture_logic_v2 import gesture_logic
import cv2
config.init()
handdetection.cap_init()

while True:
	gesture_id = 1
	print(gesture_logic(gesture_id, handdetection.detectHand(get_camera_id(gesture_id))))
	#extractor.Extractor(handdetection.detectHand())
	#print(index_finger_tip_touch.INDEX_FINGER_TIP_TOUCH(handdetection.detectHand()))
	#print(index_thumb_tip_touch.INDEX_THUMB_TIP_TOUCH(handdetection.detectHand()))
	#print(thumb_middle_tip_touch.THUMB_MIDDLE_TIP_TOUCH(handdetection.detectHand()))
	#print(thumb_ring_tip_touch.THUMB_RING_TIP_TOUCH(handdetection.detectHand()))
	#print(thumb_pinky_tip_touch.THUMB_PINKY_TIP_TOUCH(handdetection.detectHand())) 
	time.sleep(1)

cv2.destroyAllWindows()
cv2.VideoCapturerelease()
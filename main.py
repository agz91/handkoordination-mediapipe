import config
import handdetection
import camera_id_extractor
import time
import gesture_logic_v2 as gesture_logic
config.init()

while True:
	print(gesture_logic(camera_id_extractor.extractor(1), handdetection.detectHand()))
	#extractor.Extractor(handdetection.detectHand())
	#print(index_finger_tip_touch.INDEX_FINGER_TIP_TOUCH(handdetection.detectHand()))
	#print(index_thumb_tip_touch.INDEX_THUMB_TIP_TOUCH(handdetection.detectHand()))
	#print(thumb_middle_tip_touch.THUMB_MIDDLE_TIP_TOUCH(handdetection.detectHand()))
	#print(thumb_ring_tip_touch.THUMB_RING_TIP_TOUCH(handdetection.detectHand()))
	#print(thumb_pinky_tip_touch.THUMB_PINKY_TIP_TOUCH(handdetection.detectHand()))
	time.sleep(1)

cv2.destroyAllWindows()
cap.release()
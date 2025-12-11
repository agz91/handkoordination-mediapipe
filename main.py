import config
import handdetection
import extractor
import index_finger_tip_touch
import index_thumb_tip_touch
import thumb_middle_tip_touch
import thumb_ring_tip_touch
import thumb_pinky_tip_touch
import time
import gesture_logic_v2
config.init()

while True:
    print(gesture_logic_v2.gesture_logic(1, handdetection.detectHand()))
    #extractor.Extractor(handdetection.detectHand())
    #print(index_finger_tip_touch.INDEX_FINGER_TIP_TOUCH(handdetection.detectHand()))
    #print(index_thumb_tip_touch.INDEX_THUMB_TIP_TOUCH(handdetection.detectHand()))
    #print(thumb_middle_tip_touch.THUMB_MIDDLE_TIP_TOUCH(handdetection.detectHand()))
    #print(thumb_ring_tip_touch.THUMB_RING_TIP_TOUCH(handdetection.detectHand()))
    #print(thumb_pinky_tip_touch.THUMB_PINKY_TIP_TOUCH(handdetection.detectHand()))

    time.sleep(1)

cv2.destroyAllWindows()
cap.release()
import config
import handdetection
import gesture_logic
import time
#from gesture_logic 
config.init()

while True:
    time.sleep(1)
    print(gesture_logic.INDEX_FINGER_TIP_TOUCH(handdetection.detectHand()))

cv2.destroyAllWindows()
cap.release()
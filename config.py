import mediapipe as mp
import cv2

print("Importing config module...\n")

def init():
    print("Initializing global variables...")
    global cap_frame_width
    cap_frame_width = 1920

    global cap_frame_height
    cap_frame_height = 1080

    global FINGER_COMPARE_TOLERANCE
    FINGER_COMPARE_TOLERANCE = 50

    global mp_hands
    mp_hands = mp.solutions.hands

    global cap
    cap = cv2.VideoCapture(0)

    global INDEX_FINGER_TIP_compare1_X
    INDEX_FINGER_TIP_compare1_X = 1

    global INDEX_FINGER_TIP_compare2_X
    INDEX_FINGER_TIP_compare2_X = 1

    global INDEX_FINGER_TIP_compare1_Y
    INDEX_FINGER_TIP_compare1_Y = 1

    global INDEX_FINGER_TIP_compare2_Y
    INDEX_FINGER_TIP_compare2_Y = 1



if __name__ == '__main__':
  init()
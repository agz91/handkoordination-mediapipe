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





if __name__ == '__main__':
  init()
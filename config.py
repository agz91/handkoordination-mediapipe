import mediapipe as mp
import cv2

print("Importing config module...\n")

def init():
	print("Initializing global variables...\n")
	global cap_frame_width
	cap_frame_width = 1280

	global cap_frame_height
	cap_frame_height = 720

	global FINGER_COMPARE_TOLERANCE
	FINGER_COMPARE_TOLERANCE = 60

	global mp_hands
	mp_hands = mp.solutions.hands

	global cam
	cam = [cv2.VideoCapture(0), cv2.VideoCapture(2), cv2.VideoCapture(3)]

	#global gesture_id
	#gesture_id = [None] * 33
	#gesture_id[1] = "left"
	#gesture_id[2] = "left"
	#gesture_id[3] = "left"
	#gesture_id[4] = "left"
	#gesture_id[5] = "right"
	#gesture_id[6] = "right"
	#gesture_id[7] = "right"
	#gesture_id[8] = "right"
	#gesture_id[9] = "middle"
	#gesture_id[10] = "middle"
	#gesture_id[11] = "middle"
	#gesture_id[12] = "middle"
	#gesture_id[13] = "middle"
	#gesture_id[14] = "middle"
	#gesture_id[15] = "middle"
	#gesture_id[16] = "middle"
	#gesture_id[17] = "middle"
	#gesture_id[18] = "middle"
	#gesture_id[19] = "middle"
	#gesture_id[20] = "middle"
	#gesture_id[21] = "middle"
	#gesture_id[22] = "middle"
	#gesture_id[23] = "middle"
	#gesture_id[24] = "middle"
	#gesture_id[25] = "middle"
	#gesture_id[26] = "middle"
	#gesture_id[27] = "middle"
	#gesture_id[28] = "middle"
	#gesture_id[29] = "middle"
	#gesture_id[30] = "middle"
	#gesture_id[31] = "middle"
	#gesture_id[32] = "middle"
	#gesture_id[33] = "middle"

if __name__ == '__main__':
	init()
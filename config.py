# ----- import der benötigten biblotheken und module -----
# biliothek zur erkennung von händen mit bestimmten hand
# koordinaten
from difflib import restore

import mediapipe as mp
# bibliothek für die verwendung der kameras
import cv2

print("Importing config module...\n")

# ----- inhalt der funktion -----
# initialisiert verschiedene variablen welche in allen
# modulen verwendet werden
def init():
	print("Initializing global variables...\n")

	# weite des kamerabildes in pixeln
	global cap_frame_width
	cap_frame_width = 1280

	# höhe der kamerabildes in pixeln
	global cap_frame_height
	cap_frame_height = 720

	# toleranz für den vergleich der koordinaten
	global FINGER_COMPARE_TOLERANCE_MULTI
	FINGER_COMPARE_TOLERANCE_MULTI = 50

	global FINGER_COMPARE_TOLERANCE_SINGLE
	FINGER_COMPARE_TOLERANCE_SINGLE = 20

	# speicherung der funktion als variable zur leserlichkeit
	global mp_hands
	mp_hands = mp.solutions.hands

	# liste für die initialisierung der 3 kameras
	global cam
	cam = [None, None, None]

	# alle gestik ids mit der zugeordneten kamera
	global gesture
	gesture = {}
	# struktur:
	# gesture[id] = {"camera":kamera id, "hand":"Right"/"Left"/"Both", "finger0":landmark linke hand, "finger1":landmark rechte hand}
	gesture[0] = None # wird nicht verwendet, da die gestik ids bei 1 beginnen
	gesture[1] = {"camera":0, "hand":"Right", "finger0":mp_hands.HandLandmark.PINKY_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[2] = {"camera":0, "hand":"Right", "finger0":mp_hands.HandLandmark.RING_FINGER_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[3] = {"camera":0, "hand":"Right", "finger0":mp_hands.HandLandmark.MIDDLE_FINGER_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[4] = {"camera":0, "hand":"Right", "finger0":mp_hands.HandLandmark.INDEX_FINGER_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[5] = {"camera":1, "hand":"Left", "finger0":mp_hands.HandLandmark.INDEX_FINGER_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[6] = {"camera":1, "hand":"Left", "finger0":mp_hands.HandLandmark.MIDDLE_FINGER_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[7] = {"camera":1, "hand":"Left", "finger0":mp_hands.HandLandmark.RING_FINGER_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[8] = {"camera":1, "hand":"Left", "finger0":mp_hands.HandLandmark.PINKY_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[9] = {"camera":1, "hand":"Both", "finger0":mp_hands.HandLandmark.THUMB_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[10] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.THUMB_TIP, "finger1":mp_hands.HandLandmark.INDEX_FINGER_TIP}
	gesture[11] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.THUMB_TIP, "finger1":mp_hands.HandLandmark.MIDDLE_FINGER_TIP}
	gesture[12] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.THUMB_TIP, "finger1":mp_hands.HandLandmark.RING_FINGER_TIP}
	gesture[13] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.THUMB_TIP, "finger1":mp_hands.HandLandmark.PINKY_TIP}
	gesture[14] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.INDEX_FINGER_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[15] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.INDEX_FINGER_TIP, "finger1":mp_hands.HandLandmark.INDEX_FINGER_TIP}
	gesture[16] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.INDEX_FINGER_TIP, "finger1":mp_hands.HandLandmark.MIDDLE_FINGER_TIP}
	gesture[17] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.INDEX_FINGER_TIP, "finger1":mp_hands.HandLandmark.RING_FINGER_TIP}
	gesture[18] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.INDEX_FINGER_TIP, "finger1":mp_hands.HandLandmark.PINKY_TIP}
	gesture[19] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.MIDDLE_FINGER_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[20] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.MIDDLE_FINGER_TIP, "finger1":mp_hands.HandLandmark.INDEX_FINGER_TIP}
	gesture[21] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.MIDDLE_FINGER_TIP, "finger1":mp_hands.HandLandmark.MIDDLE_FINGER_TIP}
	gesture[22] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.MIDDLE_FINGER_TIP, "finger1":mp_hands.HandLandmark.RING_FINGER_TIP}
	gesture[23] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.MIDDLE_FINGER_TIP, "finger1":mp_hands.HandLandmark.PINKY_TIP}
	gesture[24] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.RING_FINGER_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[25] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.RING_FINGER_TIP, "finger1":mp_hands.HandLandmark.INDEX_FINGER_TIP}
	gesture[26] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.RING_FINGER_TIP, "finger1":mp_hands.HandLandmark.MIDDLE_FINGER_TIP}
	gesture[27] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.RING_FINGER_TIP, "finger1":mp_hands.HandLandmark.RING_FINGER_TIP}
	gesture[28] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.RING_FINGER_TIP, "finger1":mp_hands.HandLandmark.PINKY_TIP}
	gesture[29] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.PINKY_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[30] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.PINKY_TIP, "finger1":mp_hands.HandLandmark.INDEX_FINGER_TIP}
	gesture[31] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.PINKY_TIP, "finger1":mp_hands.HandLandmark.MIDDLE_FINGER_TIP}
	gesture[32] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.PINKY_TIP, "finger1":mp_hands.HandLandmark.RING_FINGER_TIP}
	gesture[33] = {"camera":2, "hand":"Both", "finger0":mp_hands.HandLandmark.PINKY_TIP, "finger1":mp_hands.HandLandmark.PINKY_TIP}

# stellt sicher, dass die funktion nur ausgeführt wird, wenn sie
# aus dem hauptprogramm spezifisch aufgerufen wird
if __name__ == '__main__':
	init()
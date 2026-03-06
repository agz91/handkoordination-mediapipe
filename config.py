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
	gesture[0] = None # wird nicht verwendet, da die gestik ids bei 1 beginnen
	gesture[1] = {"camera":0, "hand":"Right", "finger0":mp_hands.HandLandmark.PINKY_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	gesture[2] = {"camera":0, "hand":"Right", "finger0":mp_hands.HandLandmark.RING_FINGER_TIP, "finger1":mp_hands.HandLandmark.THUMB_TIP}
	#gesture[3] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[4] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[5] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[6] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[7] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[8] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[9] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[10] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[11] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[12] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[13] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[14] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[15] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[16] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[17] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[18] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[19] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[20] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[21] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[22] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[23] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[24] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[25] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[26] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[27] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[28] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[29] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[30] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[31] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[32] = {"camera":, "hand":, "finger0":, "finger1":}
	#gesture[33] = {"camera":, "hand":, "finger0":, "finger1":}

# stellt sicher, dass die funktion nur ausgeführt wird, wenn sie
# aus dem hauptprogramm spezifisch aufgerufen wird
if __name__ == '__main__':
	init()
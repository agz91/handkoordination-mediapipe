# ----- import der benötigten biblotheken und module -----
# biliothek zur erkennung von händen mit bestimmten hand
# koordinaten
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
	global FINGER_COMPARE_TOLERANCE
	FINGER_COMPARE_TOLERANCE = 60

	# speicherung der funktion als variable zur leserlichkeit
	global mp_hands
	mp_hands = mp.solutions.hands

	# liste für die initialisierung der 3 kameras
	global cam
	cam = [None, None, None]

	# alle gestik ids mit der zugeordneten kamera
	# global gesture_id
	# gesture_id = [None] * 33
	# gesture_id[1] = "left"
	# gesture_id[2] = "left"
	# gesture_id[3] = "left"
	# gesture_id[4] = "left"
	# gesture_id[5] = "right"
	# gesture_id[6] = "right"
	# gesture_id[7] = "right"
	# gesture_id[8] = "right"
	# gesture_id[9] = "middle"
	# gesture_id[10] = "middle"
	# gesture_id[11] = "middle"
	# gesture_id[12] = "middle"
	# gesture_id[13] = "middle"
	# gesture_id[14] = "middle"
	# gesture_id[15] = "middle"
	# gesture_id[16] = "middle"
	# gesture_id[17] = "middle"
	# gesture_id[18] = "middle"
	# gesture_id[19] = "middle"
	# gesture_id[20] = "middle"
	# gesture_id[21] = "middle"
	# gesture_id[22] = "middle"
	# gesture_id[23] = "middle"
	# gesture_id[24] = "middle"
	# gesture_id[25] = "middle"
	# gesture_id[26] = "middle"
	# gesture_id[27] = "middle"
	# gesture_id[28] = "middle"
	# gesture_id[29] = "middle"
	# gesture_id[30] = "middle"
	# gesture_id[31] = "middle"
	# gesture_id[32] = "middle"
	# gesture_id[33] = "middle"

# stellt sicher, dass die funktion nur ausgeführt wird, wenn sie
# aus dem hauptprogramm spezifisch aufgerufen wird
if __name__ == '__main__':
	init()
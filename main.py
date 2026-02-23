# ----- import der benötigten biblotheken und module -----
# konfiguratiuonsmodul mit global verwendeten variablen
import config
# macht ein bild und gibt dieses an das machine learning modell
# weiter, gibt eine liste mit resultaten aus
import handdetection
# gibt die zu benutzende kamera aufgrund einer gestik id aus
from camera_id_extractor import get_camera_id
# durchsucht die angeschlossenen kameras und ordnet sie richtig
# zu
import cam_selector
# bestimmt aus der resultat liste ob eine übung richtig gemacht
# wurde
from gesture_logic_v2 import gesture_logic
# bibliothek für die verwendung der kameras
import cv2
# eingebaute bibliothek mit verschiedenen funktionen zur zeit
import time
# initialisiert die variablen der konfigurationsdatei
config.init()

# ----- inhalt des hauptprogrammes -----
while True:

	# testet die resultate des cam_selectors
	#image = cam_selector.find_camera()
	#for i in range(len(image)):
	#	if image[i] is not None:
	#		cv2.imshow("Show Recorded Picture", image[i])
	#		cv2.waitKey(0)
	#		cv2.destroyAllWindows()

	# gestik id für die zu testende gestik
	cam_selector.find_camera()
	gesture_id = 10
	# druckt die resultate der gesten logik der mitgegebenen gestik in die konsole
	print(gesture_logic(gesture_id, handdetection.detectHand(get_camera_id(gesture_id))))
	time.sleep(1)
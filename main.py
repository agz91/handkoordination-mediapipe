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
from gesture_logic_v3 import gesture_logic
# bibliothek für die verwendung der kameras
import cv2
# eingebaute bibliothek mit verschiedenen funktionen zur zeit
import time
# initialisiert eine test kamera
from cam_selector_testcam import test_find_camera
# initialisiert die variablen der konfigurationsdatei
config.init()
cam_selector.find_camera()

# ----- inhalt des hauptprogrammes -----
while True:
	id = 15
	# druckt die resultate der gesten logik der mitgegebenen gestik in die konsole
	print(gesture_logic(id, handdetection.detectHand(config.gesture[id]["camera"])))
	time.sleep(1)
# ----- import der benötigten biblotheken und module -----
# bibliothek für die verwendung der kameras
import cv2
# konfiguratiuonsmodul mit global verwendeten variablen
import config

print("Importing Handdetection module...\n")

# ----- inhalt der funktion -----
# mitgegeben wird eine id für die zu verwendende kamera
def detectHand(camera_id):
	if config.cam[camera_id] is None:
		print(f"Module handdetection.py: Camera {camera_id} is not initialized.")
		return None
	# folgender code wird mit der funktion Hands ausgeführt
	with config.mp_hands.Hands(
		# verschiedene einstellungen für das machine learning
		# modell
		static_image_mode=False,
		max_num_hands=2,
		model_complexity=1,
		min_detection_confidence=0.5,
		min_tracking_confidence=0.5) as hands:
		print("Opening camera...\n")
		# kontrolliert ob die kamera initialisiert wurde
		while config.cam[camera_id].isOpened():
			print("Camera opened!\n")
			
			# nimmt ein bild auf
			print("Capturing camera frame...\n")
			success, image = config.cam[camera_id].read()
			print("Camera frame captured!\n")
			# kontrolliert ob bildaufnahme erfolgreich war
			if success:
				print("Camera frame captured successfully.\n")
			if not success:
				print("Ignoring empty camera frame.")
				continue
			# bearbeitung des aufgenommenen bildes
			image.flags.writeable = False
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			image = cv2.flip(image, 1)
			# weitergabe des bildes an das machine learning modell
			# rückgabe einer resultat liste
			results = hands.process(image)
			# kontrolliert ob die resultat liste leer ist, rückgabe
			# dieser falls nicht
			if results == None:
				break
			else: return results

# stellt sicher, dass die funktion nur ausgeführt wird, wenn sie
# aus dem hauptprogramm spezifisch aufgerufen wird
if __name__ == '__main__':
	detectHand()
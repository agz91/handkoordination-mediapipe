# ----- import der benötigten biblotheken und module -----
# konfiguratiuonsmodul mit global verwendeten variablen
import config
# bibliothek für die verwendung der kameras
import cv2
# bibliothek für die bestimmung der kamera id
from cv2_enumerate_cameras import enumerate_cameras

print("Importing Camera Selector module...\n")

# ----- inhalt der funktion -----
# mitgegeben weird eine api präferenz für die bildaufnahme, eine variable für die kamera id,
# sowie eine liste mit 3 elementen für die aufgenommenen bilder
def find_camera(apiprefference = cv2.CAP_MSMF, cam_id = 0, image = [None, None, None]):
    # geht durch jedes element der liste mit kamera ids
    for camera in enumerate_cameras(apiprefference):
        # ausführung nur wenn eine bestimmte art kamera erkannt wird
        if camera.name == "USB Camera" and camera.vid == 0x0BDA and camera.pid == 0x5844:
            print(f"Camera found: {camera.name} at {camera.index}")
            # initialisierung der gefundenen kamera
            config.cam[cam_id] = cv2.VideoCapture(camera.index, apiprefference)
            # festlegung der auflösung
            config.cam[cam_id].set(cv2.CAP_PROP_FRAME_WIDTH, config.cap_frame_width)
            config.cam[cam_id].set(cv2.CAP_PROP_FRAME_HEIGHT, config.cap_frame_height)
            # auslesen eines bildes
            success, image[cam_id] = config.cam[cam_id].read()
            # bestimmung, ob auslesen gelungen ist
            if success:
                print(f"Camera {cam_id} is operational.")
            else:
                print(f"Failed to read from camera {cam_id}.")
            cam_id += 1
        # wenn die kamera nicht erkannt wird, wird eine fehlermeldung ausgegeben und die schleife verlassen
        else:
            print(f"Module cam_selector.py: Camera {camera.name} does not match criteria.")
            break
    # liste mit 3 elementen für die aufgenommenen bilder wird zurück gegeben
    return image

# stellt sicher, dass die funktion nur ausgeführt wird, wenn sie aus dem hauptprogramm
# spezifisch aufgerufen wird
if __name__ == '__main__':
	find_camera()
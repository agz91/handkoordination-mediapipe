# ----- import der benötigten biblotheken und module -----
# konfiguratiuonsmodul mit global verwendeten variablen
import config

print("Importing camera_id_extractor module...\n")

# ----- inhalt der funktion -----
# mitgegeben wird eine id für die gesuchte gestik
def get_camera_id(gesture_id):
    # gibt anhand der mitgegebenen gestik id die zu benutzende
    # kamera id zurück
    if gesture_id in range(1, 5):
        print (f"Right camera selected.")
        return 0  # right camera
    elif gesture_id in range(5, 9):
        print (f"Left camera selected.")
        return 1  # left camera
    else:
        print (f"Middle camera selected.")
        return 2  # middle camera

# stellt sicher, dass die funktion nur ausgeführt wird, wenn sie
# aus dem hauptprogramm spezifisch aufgerufen wird
if __name__ == '__main__':
    get_camera_id()
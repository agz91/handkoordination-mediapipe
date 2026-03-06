# ----- import der benötigten biblotheken und module -----
# konfiguratiuonsmodul mit global verwendeten variablen
import config

print("Importing gesture_logic module...\n")

# ----- inhalt der funktion -----
def gesture_logic(id, Handdetection_results):
    if Handdetection_results is None or Handdetection_results.multi_hand_landmarks is None:
        print (f"Module gesture_logic_v3.py: No hand detection results to process.")
        return None
    print(f"Processing gesture logic for gesture ID: {id}\n")
    counter = 0
    # verwendet den code, welcher mit der mitgegebenen gestik id
    # übereinstimmt
    if config.gesture[id]["hand"] == "Right":
        for hand_landmarks in Handdetection_results.multi_hand_landmarks:
            finger_0 = hand_landmarks.landmark[config.gesture[id]["finger0"]]
            finger_1 = hand_landmarks.landmark[config.gesture[id]["finger1"]]
            Handedness = Handdetection_results.multi_handedness[counter].classification[0].label
            
            if Handedness == "Right":
                return False
            
            coord_finger_0 = (
                int((1 - finger_0.x) * config.cap_frame_width), 
                int(finger_0.y * config.cap_frame_height))
            coord_finger_1 = (
                int((1 - finger_1.x) * config.cap_frame_width), 
                int(finger_1.y * config.cap_frame_height))
            
            print(f"State X: {coord_finger_0[0]} - {coord_finger_1[0]}")
            print(f"State Y: {coord_finger_0[1]} - {coord_finger_1[1]}")

            if (abs(coord_finger_0[0] - coord_finger_1[0]) < config.FINGER_COMPARE_TOLERANCE_MULTI and
                abs(coord_finger_0[1] - coord_finger_1[1]) < config.FINGER_COMPARE_TOLERANCE_MULTI):
                return True
            else:
                return False
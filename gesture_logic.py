import config

print("Importing gesture_logic module...\n")

counter = 0

global INDEX_FINGER_TIP_compare1_X
INDEX_FINGER_TIP_compare1_X = 0

global INDEX_FINGER_TIP_compare2_X
INDEX_FINGER_TIP_compare2_X = 0

global INDEX_FINGER_TIP_compare1_Y
INDEX_FINGER_TIP_compare1_Y = 0

global INDEX_FINGER_TIP_compare2_Y
INDEX_FINGER_TIP_compare2_Y = 0

def INDEX_FINGER_TIP_TOUCH(Handdetection_results):
  if Handdetection_results.multi_hand_landmarks:
    for hand_landmarks in Handdetection_results.multi_hand_landmarks:
      INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
      HANDEDNESS = Handdetection_results.multi_handedness 
      # calculate pixel on screen in relation to coordinate of hand (scale 0-1) (as whole number)

      coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
      coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)



      HANDEDNESS = str(HANDEDNESS)
      HANDEDNESS_length = len(HANDEDNESS)
        

      if HANDEDNESS_length >= 100:
        x = HANDEDNESS.split("}",1)
        state = 3
      elif HANDEDNESS.find("Left") != -1:
        state = 2  
      elif HANDEDNESS.find("Right") != -1:
        state = 1
      else:
        state = 0


      if counter % 2 == 0:
        config.INDEX_FINGER_TIP_compare1_X = coord_INDEX_FINGER_TIP_X
        config.INDEX_FINGER_TIP_compare1_Y = coord_INDEX_FINGER_TIP_Y
      elif counter % 2 == 1:
        config.INDEX_FINGER_TIP_compare2_X = coord_INDEX_FINGER_TIP_X
        config.INDEX_FINGER_TIP_compare2_Y = coord_INDEX_FINGER_TIP_Y

      if((abs(INDEX_FINGER_TIP_compare1_X-INDEX_FINGER_TIP_compare2_X)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
        statex = True
      else:
        statex = False

      if((abs(INDEX_FINGER_TIP_compare1_Y-INDEX_FINGER_TIP_compare2_Y)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
        statey = True
      else:
        statey = False

      if (statex and statey):
        return True           
      #print("State X: ",INDEX_FINGER_TIP_compare1_X," - ",INDEX_FINGER_TIP_compare2_X," = ",statex)
      #print("State Y: ",INDEX_FINGER_TIP_compare1_Y," - ",INDEX_FINGER_TIP_compare2_Y," = ",statey)


if __name__ == '__main__':
  INDEX_FINGER_TIP_TOUCH()
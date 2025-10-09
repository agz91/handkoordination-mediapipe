import config

print("Importing INDEX_FINGER_TIP_TOUCH module...\n")

counter = 0 



def INDEX_FINGER_TIP_TOUCH(Handdetection_results):
  INDEX_FINGER_TIP_compare1_X = 1
  INDEX_FINGER_TIP_compare2_X = 1
  INDEX_FINGER_TIP_compare1_Y = 1
  INDEX_FINGER_TIP_compare2_Y = 1
  counter = 0
  if Handdetection_results.multi_hand_landmarks:
    for hand_landmarks in Handdetection_results.multi_hand_landmarks:
      INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
      HANDEDNESS = Handdetection_results.multi_handedness 
      # calculate pixel on screen in relation to coordinate of hand (scale 0-1) (as whole number)
      counter += 1
      coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
      coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
      print(counter)
      print(coord_INDEX_FINGER_TIP_X)
      print(coord_INDEX_FINGER_TIP_Y)


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


      if counter % 2 == 1:
        INDEX_FINGER_TIP_compare1_X = coord_INDEX_FINGER_TIP_X
        INDEX_FINGER_TIP_compare1_Y = coord_INDEX_FINGER_TIP_Y
      elif counter % 2 == 0:
        INDEX_FINGER_TIP_compare2_X = coord_INDEX_FINGER_TIP_X
        INDEX_FINGER_TIP_compare2_Y = coord_INDEX_FINGER_TIP_Y


      if((abs(INDEX_FINGER_TIP_compare1_X-INDEX_FINGER_TIP_compare2_X)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
        statex = True
      else:
        statex = False

      if((abs(INDEX_FINGER_TIP_compare1_Y-INDEX_FINGER_TIP_compare2_Y)) <= config.FINGER_COMPARE_TOLERANCE and state == 3):
        statey = True
      else:
        statey = False
      print("State X: ",INDEX_FINGER_TIP_compare1_X," - ",INDEX_FINGER_TIP_compare2_X," = ",statex)
      print("State Y: ",INDEX_FINGER_TIP_compare1_Y," - ",INDEX_FINGER_TIP_compare2_Y," = ",statey)
      if (statex and statey and counter == 2):
        return True
      elif (counter == 2):
        return False



if __name__ == '__main__':
  INDEX_FINGER_TIP_TOUCH()
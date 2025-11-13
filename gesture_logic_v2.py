import config

print("Importing gesture_logic module...\n")

def gesture_logic(picture_id, Handdetection_results):
  INDEX_FINGER_TIP_compare1_X = 1
  INDEX_FINGER_TIP_compare2_X = 1
  INDEX_FINGER_TIP_compare1_Y = 1
  INDEX_FINGER_TIP_compare2_Y = 1
  counter = 0
  match picture_id:
    case 1:
      # right: thumb, pinky
      PINKY_TIP_compare_X = 1
      PINKY_compare_Y = 1
      THUMB_TIP_compare_X = 1
      THUMB_TIP_compare_Y = 1
      counter = 0
      if Handdetection_results.multi_hand_landmarks:
        for hand_landmarks in Handdetection_results.multi_hand_landmarks:
          PINKY_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.PINKY_TIP]
          THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
          HANDEDNESS = Handdetection_results.multi_handedness
          counter += 1
          coord_PINKY_TIP_X = int((1 - PINKY_TIP.x) * config.cap_frame_width)
          coord_PINKY_TIP_Y = int(PINKY_TIP.y * config.cap_frame_height)
          coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
          coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

          HANDEDNESS = str(HANDEDNESS)
          HANDEDNESS_length = len(HANDEDNESS)

          if HANDEDNESS.find("Right") == -1 and HANDEDNESS.find("Left") != -1:
            return False

          if((abs(coord_PINKY_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
            statex = True
          else:
            statex = False

          if((abs(coord_PINKY_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
            statey = True
          else:
            statey = False
          print("State X: ",coord_PINKY_TIP_X," - ",coord_THUMB_TIP_X," = ",statex)
          print("State Y: ",coord_PINKY_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
          if (statex and statey):
            return True
          else:
            return False
      
    case 2:
      #right: thumb, ring
      RING_FINGER_TIP_compare_X = 1
      RING_FINGER_compare_Y = 1
      THUMB_TIP_compare_X = 1
      THUMB_TIP_compare_Y = 1
      counter = 0
      if Handdetection_results.multi_hand_landmarks:
        for hand_landmarks in Handdetection_results.multi_hand_landmarks:
          RING_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.RING_FINGER_TIP]
          THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
          HANDEDNESS = Handdetection_results.multi_handedness
          counter += 1
          coord_RING_FINGER_TIP_X = int((1 - RING_FINGER_TIP.x) * config.cap_frame_width)
          coord_RING_FINGER_TIP_Y = int(RING_FINGER_TIP.y * config.cap_frame_height)
          coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
          coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

          HANDEDNESS = str(HANDEDNESS)
          HANDEDNESS_length = len(HANDEDNESS)

          if HANDEDNESS.find("Right") == -1 and HANDEDNESS.find("Left") != -1:
            return False

          if((abs(coord_RING_FINGER_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
            statex = True
          else:
            statex = False

          if((abs(coord_RING_FINGER_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
            statey = True
          else:
            statey = False
          print("State X: ",coord_RING_FINGER_TIP_X," - ",coord_RING_FINGER_TIP_X," = ",statex)
          print("State Y: ",coord_RING_FINGER_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
          if (statex and statey):
            return True
          else:
            return False

    case 3:
      #right: thumb, middle
      MIDDLE_FINGER_TIP_compare_X = 1
      MIDDLE_FINGER_compare_Y = 1
      THUMB_TIP_compare_X = 1
      THUMB_TIP_compare_Y = 1
      counter = 0
      if Handdetection_results.multi_hand_landmarks:
        for hand_landmarks in Handdetection_results.multi_hand_landmarks:
          MIDDLE_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
          THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
          HANDEDNESS = Handdetection_results.multi_handedness
          counter += 1

          coord_MIDDLE_FINGER_TIP_X = int((1 - MIDDLE_FINGER_TIP.x) * config.cap_frame_width)
          coord_MIDDLE_FINGER_TIP_Y = int(MIDDLE_FINGER_TIP.y * config.cap_frame_height)
          coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
          coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

          HANDEDNESS = str(HANDEDNESS)
          HANDEDNESS_length = len(HANDEDNESS)

          if HANDEDNESS.find("Right") == -1 and HANDEDNESS.find("Left") != -1:
            return False

          if((abs(coord_MIDDLE_FINGER_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
            statex = True
          else:
            statex = False

          if((abs(coord_MIDDLE_FINGER_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
            statey = True
          else:
            statey = False
          print("State X: ",coord_MIDDLE_FINGER_TIP_X," - ",coord_MIDDLE_FINGER_TIP_X," = ",statex)
          print("State Y: ",coord_MIDDLE_FINGER_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
          if (statex and statey):
            return True
          else:
            return False

    case 4:
      #right: thumb, index
      INDEX_FINGER_TIP_compare_X = 1
      INDEX_FINGER_TIP_compare_Y = 1
      THUMB_TIP_compare_X = 1
      THUMB_TIP_compare_Y = 1
      counter = 0
      if Handdetection_results.multi_hand_landmarks:
        for hand_landmarks in Handdetection_results.multi_hand_landmarks:
          INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
          THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
          HANDEDNESS = Handdetection_results.multi_handedness
          counter += 1
          coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
          coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
          coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
          coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

          HANDEDNESS = str(HANDEDNESS)
          HANDEDNESS_length = len(HANDEDNESS)

          if HANDEDNESS.find("Right") == -1 and HANDEDNESS.find("Left") != -1:
            return False

          if((abs(coord_INDEX_FINGER_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
            statex = True
          else:
            statex = False

          if((abs(coord_INDEX_FINGER_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
            statey = True
          else:
            statey = False
          print("State X: ",coord_INDEX_FINGER_TIP_X," - ",coord_INDEX_FINGER_TIP_X," = ",statex)
          print("State Y: ",coord_INDEX_FINGER_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
          if (statex and statey):
            return True
          else:
            return False

    case 5:
      #left: thumb, index
      INDEX_FINGER_TIP_compare_X = 1
      INDEX_FINGER_TIP_compare_Y = 1
      THUMB_TIP_compare_X = 1
      THUMB_TIP_compare_Y = 1
      counter = 0
      if Handdetection_results.multi_hand_landmarks:
        for hand_landmarks in Handdetection_results.multi_hand_landmarks:
          INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
          THUMB_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.THUMB_TIP]
          HANDEDNESS = Handdetection_results.multi_handedness
          counter += 1
          coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
          coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
          coord_THUMB_TIP_X = int((1 - THUMB_TIP.x) * config.cap_frame_width)
          coord_THUMB_TIP_Y = int(THUMB_TIP.y * config.cap_frame_height)

          HANDEDNESS = str(HANDEDNESS)
          HANDEDNESS_length = len(HANDEDNESS)

          if HANDEDNESS.find("Right") != -1 and HANDEDNESS.find("Left") == -1:
            return False

          if((abs(coord_INDEX_FINGER_TIP_X-coord_THUMB_TIP_X)) <= config.FINGER_COMPARE_TOLERANCE):
            statex = True
          else:
            statex = False

          if((abs(coord_INDEX_FINGER_TIP_Y-coord_THUMB_TIP_Y)) <= config.FINGER_COMPARE_TOLERANCE):
            statey = True
          else:
            statey = False
          print("State X: ",coord_INDEX_FINGER_TIP_X," - ",coord_INDEX_FINGER_TIP_X," = ",statex)
          print("State Y: ",coord_INDEX_FINGER_TIP_Y," - ",coord_THUMB_TIP_Y," = ",statey)
          if (statex and statey):
            return True
          else:
            return False

    case 6:
      #left: thumb, index
      
    #case 7:
    #case 8:
    #case 9:
    #case 10:
    #case 11:
    #case 12:
    #case 13:
    #case 14:
    case 15:
      if Handdetection_results.multi_hand_landmarks:
        for hand_landmarks in Handdetection_results.multi_hand_landmarks:
          INDEX_FINGER_TIP = hand_landmarks.landmark[config.mp_hands.HandLandmark.INDEX_FINGER_TIP]
          HANDEDNESS = Handdetection_results.multi_handedness 
          # calculate pixel on screen in relation to coordinate of hand (scale 0-1) (as whole number)
          counter += 1
          coord_INDEX_FINGER_TIP_X = int((1 - INDEX_FINGER_TIP.x) * config.cap_frame_width)
          coord_INDEX_FINGER_TIP_Y = int(INDEX_FINGER_TIP.y * config.cap_frame_height)
          #print(counter)
          #print(coord_INDEX_FINGER_TIP_X)
          #print(coord_INDEX_FINGER_TIP_Y)


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
    #case 16:
    #case 17:
    #case 18:
    #case 19:
    #case 20:
    #case 21:
    #case 22:
    #case 23:
    #case 24:
    #case 25:
    #case 26:
    #case 27:
    #case 28:
    #case 29:
    #case 30:





if __name__ == '__main__':
  gesture_logic()
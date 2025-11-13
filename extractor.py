import config



def Extractor(Handdetection_results):
    xList = []
    yList = []


    if Handdetection_results.multi_hand_landmarks:
        print("test")
        print(Handdetection_results.multi_hand_landmarks[1])


    
    if Handdetection_results.multi_hand_landmarks:
        handlist = [Hand(x, y, z) for x, y, z in Handdetection_results.multi_hand_landmarks[0]]
        for obj in handlist:
            print(obj.x, obj.y)
            break
                    
if __name__ == '__main__':
  Extractor()
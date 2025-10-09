import pygame
import time
#from handdetection_Class import Handdetection
from Fenster_Class import Fenster

pygame.init()
F_Weite = 1280 
F_Hoehe = 720 #Fenstergröße
fenster = pygame.display.set_mode((F_Weite, F_Hoehe))
F_Name=pygame.display.set_caption("Handerkennung")

pygame.font.init()
Schrift=pygame.font.SysFont(None,50) #Schriftart
Zeit=pygame.time.Clock()
Timer=0
#detector=Handdetection() #Handerkennung starten

while True:
    pygame.display.set_mode((F_Weite,F_Hoehe))
    pygame.display.set_caption("Hand Detection")
    Fenster.start_screen(F_Weite,F_Hoehe,fenster,Zeit,Schrift)

    Timer = int(Fenster.Timer_Einagabe)+1 #da  beim starten 1s verzögerung vorhanden ist

    letzte_nummer=None
    Aufgabe,Aufgabe_platz,letzte_nummer=Fenster.lade_zufaellige_aufgabe(letzte_nummer)
    punkte=0
    start_zeit=time.time()
    aktiv=True
    status=False

    pygame.display.set_mode((F_Weite,F_Hoehe))
    pygame.display.set_caption("Hand Detection")

    while aktiv:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    status=True
        
        if status:
            Aufgabe, Aufgabe_rect,letzte_nummer=Fenster.lade_zufaellige_aufgabe(letzte_nummer)
            punkte +=1
            status = False
        
       # detector.get_hand_detection_frame() #aktualisieren der Handerkennung

        vergangene_Zeit = time.time()-start_zeit
        verbleibende_Zeit=max(0,int(Timer-vergangene_Zeit)) 

        fenster.fill((255,255,255))

        timer_text = Schrift.render(f"Zeit: {verbleibende_Zeit}s",True,(0,0,0))
        text_platz = timer_text.get_rect(center=(F_Weite//2,30))
        fenster.blit(timer_text,text_platz)

        punkte_text=Schrift.render(f"Punkte: {punkte}",True,(0,0,0))
        punkte_platz=punkte_text.get_rect(topright=(F_Weite-20,20))
        fenster.blit(punkte_text, punkte_platz)

        Aufgabe_platz_topleft = (0,0)
        fenster.blit(Aufgabe,Aufgabe_platz_topleft)

        rahmen_dicke = 10
        pygame.draw.rect(fenster,(0,0,0),(0,0,F_Weite,F_Hoehe),rahmen_dicke)
        
        pygame.display.update()
        Zeit.tick(30)

        if verbleibende_Zeit <=0:
            aktiv = False
        
    #detector.release()

    pygame.display.set_mode((F_Weite,F_Hoehe))
    pygame.display.set_caption("Hand Detection")
    aktion = Fenster.end_screen(punkte,F_Weite,F_Hoehe,fenster,Zeit)
    if aktion == "Neustart":
        continue
    else:
        break

pygame.quit()






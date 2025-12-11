import pygame
import time
import config
import handdetection 
from Fenster_Class import Fenster
import gesture_logic_v2 

import os
import sys

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0]))) #Spiel startet im richtigen Ordner


pygame.init() #initialisierung von Pygame
config.init() #initialisierung von config
pygame.font.init() #initialisierung von pagame Schrift

F_Weite = 1280 
F_Hoehe = 720 #Fenstergröße
fenster = pygame.display.set_mode((F_Weite, F_Hoehe)) #fenstergröße definiert


Schrift=pygame.font.SysFont(None,50) #Schriftart
Zeit=pygame.time.Clock() #Zeit definiert
Timer = 0 # Timer auf 0 gesetzt
modus_wahl=None #keinModus ausgewählt
status = False #Status auf falsch gesetzt
highscores = []  # Liste der Top 5, wird bei jedem Start neu geleert


while True:

    pygame.display.set_caption("Hand Detection") #Fensterbezeichnung
    modus_wahl,Spieler_Name=Fenster.start_screen(F_Weite,F_Hoehe,fenster,Zeit,Schrift,modus_wahl) #Start Fenster öffnen
    
    Timer = int(Fenster.Timer_Eingabe)+1 #Timer setzten plus 1s, da beim starten 1s verzögerung vorhanden ist

    letzte_nummer=None #letzte nummer definieren
    Aufgabe,Aufgabe_platz,letzte_nummer=Fenster.lade_zufaellige_aufgabe(letzte_nummer,modus_wahl) #Aufgabe laden
    punkte=0 #Punktestand auf 0 setzten
    start_zeit=time.time() # Startzeit definieren
    aktiv=True #aktiv true setzten um schleife zu starten


    while aktiv:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Programm beenden
                pygame.quit()
                exit()    

        if gesture_logic_v2.gesture_logic(letzte_nummer,handdetection.detectHand()):
            status=True
        else:
            status=False

      
        if status:
            Aufgabe, Aufgabe_rect,letzte_nummer=Fenster.lade_zufaellige_aufgabe(letzte_nummer,modus_wahl)
            punkte +=1
            status = False

        vergangene_Zeit = time.time()-start_zeit
        verbleibende_Zeit=max(0,int(Timer-vergangene_Zeit)) #berechnung von vergangener und verbleibender Zeit

        fenster.fill((255,255,255)) #weißer Hintergrund

        timer_text = Schrift.render(f"Zeit: {verbleibende_Zeit}s",True,(0,0,0))
        text_platz = timer_text.get_rect(center=(F_Weite//2,30))
        fenster.blit(timer_text,text_platz) #Timer Text erstellen und anzeigen

        punkte_text=Schrift.render(f"Punkte: {punkte}",True,(0,0,0))
        punkte_platz=punkte_text.get_rect(topright=(F_Weite-20,20))
        fenster.blit(punkte_text, punkte_platz) #Punkte Text erstellen und anzeigen

        Aufgabe_platz_topleft = (0,0)
        fenster.blit(Aufgabe,Aufgabe_platz_topleft) #Aufgabe anzeigen

        rahmen_dicke = 10
        pygame.draw.rect(fenster,(0,0,0),(0,0,F_Weite,F_Hoehe),rahmen_dicke) #Rahmen zeichnen
        
        pygame.display.update() #Anzeige aktualisieren

        Zeit.tick(30) #Bildwiederholrate (Frames per second) begrenzen

        if verbleibende_Zeit <=0:
            aktiv = False
        
    #detector.release()

    pygame.display.set_mode((F_Weite,F_Hoehe))
    pygame.display.set_caption("Hand Detection")
    aktion, highscores = Fenster.end_screen(punkte,F_Weite,F_Hoehe,fenster,Zeit, Spieler_Name, highscores)
    if aktion == "Neustart":
        continue
    else:
        break

pygame.quit()






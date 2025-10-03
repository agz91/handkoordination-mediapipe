import pygame
import numpy
import time
import random

Timer=10 #Timer Zeit in Sekunden

pygame.init()
F_Weite = 1280 
F_Hoehe = 720 #Fenstergröße
fenster = pygame.display.set_mode((F_Weite, F_Hoehe))
F_Name=pygame.display.set_caption("Handerkennung")

pygame.font.init()
Schrift=pygame.font.SysFont(None,48) #Schriftart
Zeit=pygame.time.Clock()

class Fenster:
    def draw_button (fenster, platz, text, Schrift,b_farbe,t_farbe):
        pygame.draw.rect(fenster,b_farbe,platz)
        b_text = Schrift.render(text,True,t_farbe)
        text_platz = b_text.get_rect(center=platz.center)
        fenster.blit(b_text, text_platz)

    def lade_zufaellige_aufgabe(letzte_nummer, max_weite=500, max_hoehe=500):
        Bild_Nummer = random.randint(1,4)
        while Bild_Nummer == letzte_nummer:
            Bild_Nummer = random.randint(1,4)
        letzte_nummer=Bild_Nummer

        Bild_Datei = f"Image{Bild_Nummer}.jpg"
        Aufgabe = pygame.image.load(Bild_Datei)

        orig_weite, orig_hoehe =Aufgabe.get_size()
        skal_faktor = min(max_weite / orig_weite, max_hoehe/orig_hoehe)
        neue_weite = int(orig_weite * skal_faktor)
        neue_hoehe = int(orig_hoehe * skal_faktor)

        Aufgabe = pygame.transform.scale(Aufgabe, (neue_weite, neue_hoehe))
        Aufgabe = pygame.transform.rotate(Aufgabe, 90)

        Aufgabe_platz = Aufgabe.get_rect()

        return Aufgabe, Aufgabe_platz, letzte_nummer
    
    def start_screen():
        b_schrift = pygame.font.SysFont(None, 60) #Schriftgröße
        b_start = pygame.Rect(F_Weite//2 - 100, F_Hoehe//2 - 40, 200, 80) 

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b_start.collidepoint(event.pos):
                        return
            
            fenster.fill((255,255,255))
            Fenster.draw_button(fenster,b_start,"Starten",b_schrift,(0,100,0),(255,255,255))

            pygame.display.update()
            Zeit.tick(30)
        
    def end_screen(punkte):
        p_schrift = pygame.font.SysFont(None, 72) #Schriftgröße
        b_schrift = pygame.font.SysFont(None, 48) #Schriftgröße
        b_restart = pygame.Rect(F_Weite//2 - 300, F_Hoehe//2 - 40, 200, 80) 
        b_ende = pygame.Rect(F_Weite//2 + 100, F_Hoehe//2 - 40, 200, 80)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b_restart.collidepoint(event.pos):
                        pygame.display.set_mode((F_Weite,F_Hoehe))
                        pygame.display.set_caption("Hand Detection")
                        return "Neustart"
                    if b_ende.collidepoint(event.pos):
                        pygame.quit()
                        exit()

            fenster.fill((255,255,255))

            p_text=p_schrift.render(f"Punkte: {punkte}",True,(0,0,0))
            p_platz=p_text.get_rect(center=(F_Weite//2,80))
            fenster.blit(p_text,p_platz)

            Fenster.draw_button(fenster,b_restart,"Neustart",b_schrift,(0,0,150),(255,255,255))
            Fenster.draw_button(fenster,b_ende,"Beenden",b_schrift,(150,0,0),(255,255,255))

            pygame.display.update()
            Zeit.tick(30)


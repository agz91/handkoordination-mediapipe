import pygame
import random



class Fenster:
    def draw_button (fenster, platz, text, Schrift,b_farbe,t_farbe):
        pygame.draw.rect(fenster,b_farbe,platz)
        b_text = Schrift.render(text,True,t_farbe)
        text_platz = b_text.get_rect(center=platz.center)
        fenster.blit(b_text, text_platz)

    def lade_zufaellige_aufgabe(letzte_nummer,modus_wahl, max_weite=500, max_hoehe=500):
        
        if modus_wahl == "rechts":
            Bild_Nummer = random.randint(1,4)
            while Bild_Nummer == letzte_nummer:
                Bild_Nummer = random.randint(1,4)
            letzte_nummer=Bild_Nummer
        elif modus_wahl == "links":
            Bild_Nummer = random.randint(5,8)
            while Bild_Nummer == letzte_nummer:
                Bild_Nummer = random.randint(5,8)
            letzte_nummer=Bild_Nummer
        elif modus_wahl == "beide":
            Bild_Nummer = random.randint(9,33)
            while Bild_Nummer == letzte_nummer:
                Bild_Nummer = random.randint(9,33)
            letzte_nummer=Bild_Nummer
        elif modus_wahl == "alle":
            Bild_Nummer = random.randint(1,33)
            while Bild_Nummer == letzte_nummer:
                Bild_Nummer = random.randint(1,33)
            letzte_nummer=Bild_Nummer

        Bild_Datei = f"Image{Bild_Nummer}.jpg"
        Aufgabe = pygame.image.load(Bild_Datei)

        orig_weite, orig_hoehe =Aufgabe.get_size()
        skal_faktor = min(max_weite / orig_weite, max_hoehe/orig_hoehe)
        neue_weite = int(orig_weite * skal_faktor)
        neue_hoehe = int(orig_hoehe * skal_faktor)

        Aufgabe = pygame.transform.scale(Aufgabe, (neue_weite, neue_hoehe))

        Aufgabe_platz = Aufgabe.get_rect()

        return Aufgabe, Aufgabe_platz, letzte_nummer
    
    Timer_Eingabe=""
    
    def start_screen(F_Weite,F_Hoehe,fenster,zeit,Schrift,modus_wahl):
        b_schrift = pygame.font.SysFont(None, 60) #Schriftgröße
        b_schrift_auswahl = pygame.font.SysFont(None, 45) #Schriftgröße

        button_weite, button_hoehe= 250,150
        abstand = 15

        b_start = pygame.Rect ((F_Weite - 350)//2, (F_Hoehe - 200)//2, 350, 200)

        b_rechts = pygame.Rect (F_Weite - button_weite - abstand, abstand, button_weite, button_hoehe/2)
        b_links = pygame.Rect (F_Weite - button_weite - abstand, abstand + (button_hoehe/2 + abstand), button_weite, button_hoehe/2)
        b_beide = pygame.Rect (F_Weite - button_weite - abstand, abstand + 2*(button_hoehe/2 + abstand), button_weite, button_hoehe/2)
        b_alle = pygame.Rect (F_Weite - button_weite - abstand, abstand + 3*(button_hoehe/2 + abstand), button_weite, button_hoehe/2)

        buttons = [
            (b_rechts, "Rechte Hand", "rechts"),
            (b_links, "Linke Hand", "links"),
            (b_beide, "Beide Hände", "beide"),
            (b_alle, "Alle", "alle")
        ]

        f_inaktiv = (0,0,0)
        f_aktiv=(0,100,0)
        f_fehler=(255,0,0)
        farbe=f_inaktiv

        z_feld = pygame.Rect(550,100,200,50)
        aktiv = False
        timerfehler = False
        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for rect, text, mode in buttons:
                        if rect.collidepoint(event.pos):
                         modus_wahl = mode
                         break
                
                    if b_start.collidepoint(event.pos):
                        try:
                            Timer_wert=int(Fenster.Timer_Eingabe)
                        except ValueError:
                            Timer_wert=0
                        if Timer_wert > 0 and modus_wahl is not None:
                            return modus_wahl
                        else:
                            farbe = f_fehler 
                            timerfehler = True
                    if z_feld.collidepoint(event.pos):
                        aktiv = not aktiv
                    else:
                        aktiv = False
                    if farbe != f_fehler:
                        farbe = f_aktiv if aktiv else f_inaktiv
                    else:
                        farbe = f_aktiv if aktiv else f_fehler
                elif event.type == pygame.KEYDOWN and aktiv:
                    if event.key == pygame.K_BACKSPACE:
                        Fenster.Timer_Eingabe = Fenster.Timer_Eingabe[:-1]
                    else:
                        Fenster.Timer_Eingabe += event.unicode
            
            fenster.fill((255,255,255))

            for rect, text, mode in buttons:
                if modus_wahl == mode:
                    farbe_button = f_aktiv
                else:
                    farbe_button = f_inaktiv
                Fenster.draw_button(fenster, rect, text, b_schrift_auswahl, farbe_button, (255,255,255))

            Fenster.draw_button(fenster,b_start,"Starten",b_schrift,(0,100,0),(255,255,255))
            pygame.draw.rect(fenster,farbe,z_feld,2)
            text_surface = Schrift.render(Fenster.Timer_Eingabe, True, (0, 0, 0))
            fenster.blit(text_surface, (z_feld.x + 5, z_feld.y + 5))

            timer_text = Schrift.render(f"Timer:",True,(0,0,0))
            text_platz = timer_text.get_rect(center=(F_Weite//2,70))
            fenster.blit(timer_text,text_platz)

            if timerfehler:
                timerfehler_text = Schrift.render(f"!!!Zeit und Modus festlegen!!!",True,(255,0,0))
                fehlertext_platz = timerfehler_text.get_rect(center=(F_Weite//2,200))
                fenster.blit(timerfehler_text,fehlertext_platz)
            
            pygame.display.update()
        
    def end_screen(punkte,F_Weite,F_Hoehe,fenster,Zeit):
        p_schrift = pygame.font.SysFont(None, 72) #Schriftgröße
        b_schrift = pygame.font.SysFont(None, 60) #Schriftgröße
        button_weite, button_hoehe, Abstand= 350, 200, 50
        b_restart = pygame.Rect((F_Weite - (2*button_weite+Abstand))//2, (F_Hoehe-button_hoehe)//2, button_weite, button_hoehe) 
        b_ende = pygame.Rect(b_restart.right + Abstand, (F_Hoehe-button_hoehe)//2, button_weite, button_hoehe) 

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
            


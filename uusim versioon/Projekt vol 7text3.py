import pygame
import random
import time
import math
import tkinter
from tkinter import messagebox

pygame.init()

def lev1():
    global kiirusXTase, kiirusYa, kiirusYb
    kiirusXTase = 2
    kiirusYa = 3
    kiirusYb = 5
    tkAken.destroy()

def lev2():
    global kiirusXTase, kiirusYa, kiirusYb
    kiirusXTase = 3
    kiirusYa = 5
    kiirusYb = 6
    tkAken.destroy()

def lev3():
    global kiirusXTase, kiirusYa, kiirusYb
    kiirusXTase = 4
    kiirusYa = 8
    kiirusYb = 9
    tkAken.destroy()

tkAken = tkinter.Tk()
leveliNupp = tkinter.Button(tkAken, text = "Level 1", command = lev1)
leveliNupp2 = tkinter.Button(tkAken, text = "Level 2", command = lev2)
leveliNupp3 = tkinter.Button(tkAken, text = "Level 3", command = lev3)
leveliNupp.pack()
leveliNupp2.pack()
leveliNupp3.pack()
tkAken.mainloop()

nool = pygame.image.load("nool2.png")          # võtab kasutusele pildi
pahaNool = pygame.image.load("pahaNool2.png")  # võtab kasutusele pildi
aken = pygame.display.set_mode((600, 400))     # loob ekraani
ekraaniLaius, ekraaniKõrgus = pygame.display.get_surface().get_size()  # annab ekraani laiuse- ja kõrguse
mängKäib = True                    # selle muutujaga saab mängu hiljem kinni panna
kõikAsjad = pygame.sprite.Group()  # sprite'de grupp, mida kasutatakse kõige ekraanile joonistamiseks
enemys = pygame.sprite.Group()     # sprite'de grupp, mida kasutatakse "kokkupõrke" kontrollimiseks
muutuja = 0
fps = 0
font = pygame.font.SysFont("aerial", 72)


class Player(pygame.sprite.Sprite):  # klassi loomine
    def __init__(self):              # mängu käivitudes, esialgsed väärtused
        pygame.sprite.Sprite.__init__(self)
        self.image = nool
        self.rect = self.image.get_rect()
        self.rect.x = ekraaniLaius / 2
        self.rect.bottom = ekraaniKõrgus  # tegelaskuju põhja asukoht ekraanil
        self.kiirusY = 0  # kiirus y-teljel
        self.kiirusX = 0  # kiirus x-teljel

    def update(self):  # uuendus funktsioon
        klahv = pygame.key.get_pressed()  # kui mingit nuppu vajutatakse
        if klahv[pygame.K_LEFT]:          # siis olenevalt vajutatud klahvist
            self.kiirusX += -1            # kiirus jääb muutuma
        if klahv[pygame.K_RIGHT]:
            self.kiirusX += 1
        if klahv[pygame.K_UP]:
            self.kiirusY -= 1
        if klahv[pygame.K_DOWN]:
            self.kiirusY += 1

        self.rect.x += self.kiirusX  # mängja asukoha määramine olenevalt kogutud kiirusest
        self.rect.y += self.kiirusY  # ----------------------------------------------------

        # see piirab mängja liikumist (et ekraanilt ära ei kaoks)
        if self.rect.right > ekraaniLaius:  # hetkel töötab ainult parema servaga :)
            self.kiirusX = 0
            self.rect.right = ekraaniLaius
        if self.rect.left < 0:
            self.kiirusX = 0
            self.rect.left = 0
        if self.rect.top < 0:
            self.kiirusY = 0
            self.rect.top = 0
        if self.rect.bottom > ekraaniKõrgus:
            self.kiirusY = 0
            self.rect.bottom = ekraaniKõrgus

        # see osa pidurdab mängjat
        if self.kiirusX < 0:     # kui kiirus on nullist väiksem (mängja liigub vasakule)
            self.kiirusX += 0.5  # siis hakkab keha kiirendama paremale, kuni jääb seisma
        if self.kiirusX > 0:     # ülejäänud suundadega toimitakse samamoodi
            self.kiirusX -= 0.5
        if self.kiirusY < 0:
            self.kiirusY += 0.5
        if self.kiirusY > 0:
            self.kiirusY -= 0.5


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pahaNool
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ekraaniLaius)
        self.rect.bottom = 0
        self.kiirusX = random.randint(-2, 2)
        self.kiirusY = random.randint(kiirusYa, kiirusYb)
        self.rng = random.randint(0, 100)

    def update(self):
        self.rect.bottom += self.kiirusY
        self.rect.x += self.kiirusX
        self.rng = random.randint(0, 100)
        if self.rng < 10:
            self.kiirusX = random.randint(-kiirusXTase, kiirusXTase)


player = Player()      # klassi saab esile kutsuda muutujaga
enemy = Enemy()
kõikAsjad.add(player)  # muutuja saab panna sprite'de gruppi

while mängKäib:  # hetkel lõpmatu tsükkel; mängu tsükkel

    for sündmus in pygame.event.get():   # vaatab, millised sündmused pygames toimuvad
        if sündmus.type == pygame.QUIT:  # kui sündmus on QUIT, siis mäng läheb kinni
            mängKäib = False             # tsükkel lõpetatakse sellega

    if random.randint(0, 100) < 10:       # RNG - kas juhtub midagi või ei
        m = Enemy()                      # klass pannakse muutujasse
        kõikAsjad.add(m)                 # muutuja pannakse sprite'de gruppi
        enemys.add(m)                    # muutuja pannakse sprite'de gruppi

    aeg = time.perf_counter()  # taimer
    aeg = (math.floor(aeg))
    if aeg != muutuja:
        print("fps: ", fps)
        muutuja = aeg
        fps = 0
    if aeg == muutuja:
        fps += 1
    if aeg >= 30:  # kui mängu käivitamisest on möödunud 30 sekundit
        skoor = "Aeg läbi, skoor on: " + str(round(aeg))
        mängKäib = False  # siis mäng saab läbi

    # kontrollib kokkupõrget (tõeväärtus, määrab, kas sprite kaob ära või ei)
    collision = pygame.sprite.spritecollide(player, enemys, False)
    for col in collision:  # kui leidub kokkupõrge
        skoor = "skoor on: " + str(round(aeg))
        mängKäib = False   # siis mäng saab läbi
        break

    aken.fill([50, 50, 50])  # täidab tausta ühtse värviga
    kõikAsjad.update()
    kõikAsjad.draw(aken)
    pygame.display.flip()
    pygame.time.delay(17)

text = font.render(skoor, True, (200, 200, 200))
aken.fill([0, 0, 0])
aken.blit(text, (ekraaniLaius/2 - text.get_width() / 2, ekraaniKõrgus/2 - text.get_height() / 2))
pygame.display.flip()
tkAken = tkinter.Tk()
tkAken.withdraw()
messagebox.showinfo("Mäng läbi", "teie skoor on: " + str(round(aeg)))
pygame.quit()

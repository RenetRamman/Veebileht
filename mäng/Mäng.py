import random
import pygame
##def kuul_pihtas(vx,vy,kx,ky):
##    for i,j in zip(vy,vy):
##    if:
##        return (True)
##    else:
##        return (False)
pygame.init()
aeg = pygame.time.Clock()
fps = 60
## teen akna
ekraanX = 800
ekraanY = 400
ekraan = pygame.display.set_mode((ekraanX, ekraanY))


## nimi
pygame.display.set_caption("Mäng")

x = 50
y = 50
kuulix = []
kuuliy = []
kuul = False
kuulidekaugus = 200
kiirus = 2
kuulikiirus = 5
vaenlased = [800]
vaenlx = 600
vloendur = 100
vkiirus = 3
vaenlasedy = []
taust = pygame.image.load("taust.png").convert()
laev = pygame.image.load("laev.png").convert_alpha()
bullet = pygame.image.load("bullet.png").convert_alpha()
vaenlane = pygame.image.load("space-ship.png").convert_alpha()
kuulid = []
kord = 0
run = True

def sulgemine():
    ## saab ristist kinni panna
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
run = True            
while run:
    # sama mida sinu delay funktsioon tegi
    aeg.tick(fps)
    
    sulgemine()
    ## liikuv taust
    kordaja = kord % taust.get_rect().width
    ekraan.blit(taust, ((kordaja - taust.get_rect().width), 0))
    if kordaja < ekraanX:
        ekraan.blit(taust, (kordaja, 0))
    kord -= 1
    
    keys = pygame.key.get_pressed()
    
    ## juhtimine
    if keys[pygame.K_UP]:
        y -= kiirus
    if keys[pygame.K_DOWN]:
        y += kiirus
    ## laskmine
    if kuulix == [] or kuulix[-1] > kuulidekaugus: ## jätab kuulide laskmise vahele väikse vahe
        if keys[pygame.K_SPACE]:
            kuul = True
            kuulix.append(180)
            kuuliy.append(y+50)

    loendur = 0
    for kux,kuy in zip(kuulix,kuuliy):
        kuulix[loendur]+= kuulikiirus
        ekraan.blit(bullet, (kux,kuy))
        loendur += 1
    if kuulix == []:
        kuulid = False
    elif kuulix[0] > 800:
        kuulix.pop(0)
        kuuliy.pop(0)
    if vloendur == 0:
        vaenlased.append(800)
        vaenlasedy.append(random.randint(0,400))
        vloendur = 100
    vloendur -= 1
    lv = 0
    for vaen,ye in zip(vaenlased,vaenlasedy):
        vaenlased[lv] -= vkiirus
        ekraan.blit(vaenlane, (vaen,ye))
        l = range(y+10,y-10)
        if vaen == 50  and ye in range(y-60,y+60):
##            run = False
            print("lp")
            None
##        if kuul_pihtas(vaenlased,vaenlasedy,kuulix,kuuliy):
##            print(pihtas)
        lv +=1
    loendur -= 1
    ekraan.blit(laev, (x,y))
    pygame.display.update()
pygame.quit()
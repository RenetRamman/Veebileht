import pygame

#main
pygame.init()
pygame.display.set_caption("Mäng")
#display
ekraanX = 800
ekraanY = 400
ekraan = pygame.display.set_mode((ekraanX, ekraanY))
#fps
aeg = pygame.time.Clock()
fps = 60
#sprites
taust = pygame.image.load("taust.png").convert_alpha()
laev = pygame.image.load("laev.png").convert_alpha()
bullet = pygame.image.load("bullet.png").convert_alpha()
bullets = pygame.sprite.Group()
x = 50
y = 50
kiirus = 2
taustakordaja = 0

class bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet
        self.bottom = y
        self.centerx = x
        self.speedx = 10
    
    def update(self):
        self.rect.x += self.speedx
        
    

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
                
    #liikuv taust 
    kordaja = taustakordaja % taust.get_rect().width
    ekraan.blit(taust, ((kordaja - taust.get_rect().width), 0))
    if kordaja < ekraanX:
        ekraan.blit(taust, (kordaja, 0))
    taustakordaja -= 1
    #juhtimine
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
         y -= kiirus
    if keys[pygame.K_DOWN]:
        y += kiirus
    if keys[pygame.K_SPACE]:
        bullet = bullet(x,y)
        bullets.add(bullet)
    #laev
    ekraan.blit(laev, (x,y))
            
    #display uuendamine jms
    aeg.tick(fps)
    pygame.display.update()
            

        
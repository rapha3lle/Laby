import pygame
from tableaux import niveau


class perso(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        self.image = pygame.image.load("assets/crapeaux.png").convert_alpha()

        self.image = pygame.transform.scale(self.image, (30, 30))

    def prt(self):
        ecran.blit(self.image, (self.x, self.y))

    def get_size(self):
        return self.image.get_size()

    def get_pos(self):
        return (self.x, self.y)


pygame.init()

ecran = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Labyrinthe")
clock = pygame.time.Clock()
raph = perso()
height = ecran.get_height()
width = ecran.get_width()
raph_h, raph_w = raph.get_size()
"""raph.x = int(width / 2 - raph_w / 2)
raph.y = int(height / 2 - raph_h / 2)"""
BLUE = (0, 100, 250)
BLACK = (0, 0, 0)
mur = pygame.image.load("assets/mur.jpg").convert_alpha()
mur = pygame.transform.scale(mur, (30, 30))

fond = pygame.image.load("assets/fond.png").convert_alpha()
fond = pygame.transform.scale(fond, (30, 30))


nenu = pygame.image.load("assets/nenuphar.png").convert_alpha()
nenu = pygame.transform.scale(nenu, (30, 30))


continuer = True



raph.x = 30
raph.y = 30

def draw(ecran, niveau):
    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                ecran.blit(mur, (i * 30, j * 30))
            elif case == 0:
                ecran.blit(fond,(i * 30, j * 30))
            elif case == 3:
                ecran.blit(nenu, (i * 30, j * 30))
            elif case == 2:
                ecran.blit(fond, (i * 30, j * 30))
                ecran.blit(raph.image, (raph.x, raph.y))

def one(x, y):
    print(x, y)

    if niveau[y][x] == 1:
        return False
    elif niveau[y][x] == 0:
        return True
    elif niveau[y][x] == 2:
        return True
    elif niveau[y][x] == 3:
        return True





while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:
            x = int(raph.x // 30)
            y = int(raph.y // 30)
            one(x, y)
            if event.key == pygame.K_RIGHT:
                print("right ",raph.x)
                if  raph.x <= 390 and one(x + 1, y):
                    raph.x += 30
                else:
                    raph.x = raph.x
            if event.key == pygame.K_LEFT:
                print("left")
                if one(x - 1, y) and raph.x > 0:
                    raph.x -= 30
                else:
                    raph.x = raph.x
            if event.key == pygame.K_UP:
                print("up")
                if one(x, y - 1) and raph.y > 0:
                    raph.y -= 30
                else:
                    raph.y = raph.y
            if event.key == pygame.K_DOWN:
                print("down")
                if raph.y <= 390 and one(x, y + 1):
                    raph.y += 30
                else:
                    raph.y = raph.y
                """x, y = raph.get_pos()
                print("X =", x, "Y =", y)"""

    ecran.fill(BLUE)
    draw(ecran, niveau)
    raph.prt()
    pygame.display.update()
    clock.tick(60)

    pygame.display.flip()

pygame.quit()

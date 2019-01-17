import pygame
from random import randint
pygame.init()

displayHeight = 600
displayWidth = 800

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
darkBlue = (0,0,128)

kratosImg = pygame.image.load('godofwar.jpeg')
def kratos(a,b):
    gameDisplay.blit(kratosImg, (a,b))

bloodImg = pygame.image.load('blood.png')
def blood(a,b):
    gameDisplay.blit(pygame.transform.scale(bloodImg,(5,5)), (a,b))

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("GOD OF WAR (game of the year edition)")

gameDisplay.fill(white)
kratos(0,0)

rectCount = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if rectCount <= 500:
        blood(randint(0,800),randint(0,600))
        rectCount= rectCount+1
        
    pygame.display.update()

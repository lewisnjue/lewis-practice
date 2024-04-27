import pygame  
pygame.init()
import os 
import math

# constants 

FORCE = 6 

WIDTH,HEIGHT = 500,480
FPS = 60 
WHITE = (255,255,255)
BLACK = (0,0,0)
MOVE_LEFT_COUNTER = 0
MOVE_RIGHT_COUNTER = 0
PLAYER_X = (WIDTH // 2 - 30)
VELOCITY = 5
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('resource','bg.jpg')),(WIDTH,HEIGHT)) 

PLAYER_STAND = pygame.image.load(os.path.join('resource','standing.png'))


PLAYER_MOVE_RIGHT = [pygame.image.load(os.path.join('resource','R1.png')),pygame.image.load(os.path.join('resource','R2.png')),pygame.image.load(os.path.join('resource','R3.png')),pygame.image.load(os.path.join('resource','R4.png')),pygame.image.load(os.path.join('resource','R5.png')),pygame.image.load(os.path.join('resource','R6.png')),pygame.image.load(os.path.join('resource','R7.png')),pygame.image.load(os.path.join('resource','R8.png')),pygame.image.load(os.path.join('resource','R9.png'))]
PLAYER_MOVE_LEFT = [pygame.image.load(os.path.join('resource','L1.png')),pygame.image.load(os.path.join('resource','L2.png')),pygame.image.load(os.path.join('resource','L3.png')),pygame.image.load(os.path.join('resource','L4.png')),pygame.image.load(os.path.join('resource','L5.png')),pygame.image.load(os.path.join('resource','L6.png')),pygame.image.load(os.path.join('resource','L7.png')),pygame.image.load(os.path.join('resource','L8.png')),pygame.image.load(os.path.join('resource','L9.png'))]

IMAGE_Y_POSTION = HEIGHT

pygame.display.set_caption("FIHGING")


def move_left():
    global  VELOCITY
    global PLAYER_X
    global MOVE_LEFT_COUNTER
    if MOVE_LEFT_COUNTER >= 8:
        MOVE_LEFT_COUNTER = 0
    MOVE_LEFT_COUNTER += 0.2
   
    PLAYER_RECT = PLAYER_MOVE_LEFT[int(MOVE_LEFT_COUNTER)].get_rect(bottomleft = (PLAYER_X,HEIGHT))
    
    WIN.blit(PLAYER_MOVE_LEFT[int(MOVE_LEFT_COUNTER)],PLAYER_RECT)
    PLAYER_X-= VELOCITY




def move_right():
    global  VELOCITY
    global PLAYER_X
    global MOVE_RIGHT_COUNTER

    if MOVE_RIGHT_COUNTER > len(PLAYER_MOVE_RIGHT)-1:
        MOVE_RIGHT_COUNTER = 0

    MOVE_RIGHT_COUNTER += 0.2
    
    PLAYER_RECT = PLAYER_MOVE_RIGHT[int(MOVE_RIGHT_COUNTER)].get_rect(bottomleft = (PLAYER_X,HEIGHT))
   
    WIN.blit(PLAYER_MOVE_RIGHT[int(MOVE_RIGHT_COUNTER)],PLAYER_RECT)
    PLAYER_X+= VELOCITY
    

def jump(is_jump = False):
    global IMAGE_Y_POSTION
    global FORCE
    if is_jump:
        IMAGE_Y_POSTION -= FORCE
        FORCE -=1 
        if IMAGE_Y_POSTION <= - 6:
            FORCE = 6
            is_jump = False
            return True
        
        return False

    




            
def imprement_movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move_left()

    elif keys[pygame.K_RIGHT]:
        move_right()

    else:
        PLAYER_STAND_RECT = PLAYER_STAND.get_rect(bottomleft = (PLAYER_X,HEIGHT))
        WIN.blit(PLAYER_STAND,PLAYER_STAND_RECT)

def draw():
    WIN.blit(BACKGROUND_IMAGE,(0,0))
    imprement_movement()
    KEYS = pygame.key.get_pressed()
    if KEYS[pygame.K_SPACE] and FORCE == 6:
        jump(is_jump = True)
    else:
        jump(is_jump = False)

    
    
    pygame.display.update()
def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw()
        clock.tick(FPS)
    pygame.quit()
if __name__ == "__main__":
    main()
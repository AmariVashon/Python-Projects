import pygame
import random as rd
import time

pygame.init()
pygame.font.init()

WIDTH = 700
HEIGHT = 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot blocks")

FPS = 60

WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)

PATH = r'c:/Users/amari/OneDrive/Desktop/Python/pygame/Assets/'

FONT = pygame.font.Font(PATH+'ARCADE_N.TTF', 20)

SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

VELOCITY = 5
BULLET_VELOCITY = 4
MAX_BULLETS = 3

BLOCK_HIT = pygame.USEREVENT + 1
SPACESHIP_HIT = pygame.USEREVENT + 2
BLOCK_OFF_SCREEN = pygame.USEREVENT + 3

blocks = []
BLOCKS_AMT = 1
BLOCKS_VELOCITY = 1

BACKGROUND = pygame.image.load(PATH+'space_background.jpg')

BLUE_SPACESHIP_LOAD = pygame.image.load(PATH+'spaceship_blue.png')
BLUE_SPACESHIP = pygame.transform.scale(BLUE_SPACESHIP_LOAD, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

def draw(spaceship, bullets, score, level):
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(BLUE_SPACESHIP, (spaceship.x, spaceship.y))

    handle_blocks()

    score_text = FONT.render("Score: " + str(score), 1, WHITE)
    WIN.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))

    level_text = FONT.render("Level: " + str(level), 1, WHITE)
    WIN.blit(level_text, (WIDTH - level_text.get_width() - 10, 50))

    for bullet in bullets:
        pygame.draw.rect(WIN, WHITE, bullet)

    pygame.display.update()

def user_movement(keys_pressed, spaceship):
    if keys_pressed[pygame.K_a] and spaceship.x - VELOCITY > 0:
        spaceship.x -= VELOCITY 
    if keys_pressed[pygame.K_w] and spaceship.y - VELOCITY > 0:
        spaceship.y -= VELOCITY
    if keys_pressed[pygame.K_d] and spaceship.x + VELOCITY + spaceship.width < WIDTH:
        spaceship.x += VELOCITY
    if keys_pressed[pygame.K_s] and spaceship.y + VELOCITY + spaceship.height < HEIGHT:
        spaceship.y += VELOCITY

class Block():
    velocity = 1
    y_position = rd.randrange(-250, -30)

    def __init__(self):
        self.width = 40
        self.height = 40
        self.velocity = Block.velocity
        self.x = rd.randrange(0 + self.width, WIDTH - self.width)
        self.y = Block.y_position

    @classmethod
    def setVelocity(self, amt):
        Block.velocity = amt
    
    def update(self):
        self.y += self.velocity
        #if self.y > HEIGHT:
            #self.y = rd.randrange(-150, -20)
            #self.x = rd.randint(0 + self.width, WIDTH - self.width)
    
    def draw(self):
        pygame.draw.rect(WIN, RED, pygame.Rect(self.x, self.y, self.width, self.height))
    
    def get_block(self):
        return pygame.draw.rect(WIN, RED, pygame.Rect(self.x, self.y, self.width, self.height))
    
    def reset_blocks(self):
        self.y = rd.randrange(-250, -30)

def create_blocks(amt):
    for i in range(amt):
        blocks.append(Block())

create_blocks(BLOCKS_AMT)

def handle_blocks():
    for block in blocks:
        block.update()
        block.draw()

def block_off_screen(blocks):
    for block in blocks:
        if block.y > HEIGHT:
            pygame.event.post(pygame.event.Event(BLOCK_OFF_SCREEN))

def user_hit(blocks, spaceship):
    for block in blocks:
        if block.get_block().colliderect(spaceship):
            pygame.event.post(pygame.event.Event(SPACESHIP_HIT))


def handle_bullets(bullets, blocks):
    for bullet in bullets:
        bullet.y -= BULLET_VELOCITY
        if bullet.y < 0:
            bullets.remove(bullet)
        for block in blocks:
            if block.get_block().colliderect(bullet):
                pygame.event.post(pygame.event.Event(BLOCK_HIT))
                bullets.remove(bullet)
                blocks.remove(block)
                create_blocks(1)

def text_objects(text, font):
    textSurface = font.render(text, True, BLUE)
    return textSurface, textSurface.get_rect()

def display_message(text):
    largeText = pygame.font.SysFont('comicsans', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH/2), (HEIGHT/2))
    WIN.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

def crash():
    display_message("You died!")

def game_over():
    display_message("Game over.")

def yes_button(msg, x, y, w, h, ic, ac, action=None, blocks=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(WIN, ac, (x, y, w, h))

        if click[0] == 1 and action != None and blocks != None:
            for block in blocks:
                block.reset_blocks()
            action()
            
    else:
        pygame.draw.rect(WIN, ic, (x, y, w, h))
    
    text = FONT.render(msg, 1, BLACK)
    WIN.blit(text, (x+w/2 - 30, y+h/2 - 8))

def no_button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(WIN, ac, (x, y, w, h))

        if click[0] == 1 and action != None and blocks != None:
            action()
            
    else:
        pygame.draw.rect(WIN, ic, (x, y, w, h))
    
    text = FONT.render(msg, 1, BLACK)
    WIN.blit(text, (x+w/2 - 20, y+h/2 - 8))

def play_again():
    clock = pygame.time.Clock()
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        play_question = FONT.render("Do you want to play again?", 1, WHITE)
        WIN.blit(play_question, (140, 200))

        yes_button("YES", 250, HEIGHT/2, 100, 50, GREEN, BRIGHT_GREEN, main, blocks)
        no_button("NO", WIDTH/2 + 50, HEIGHT/2, 100, 50, RED, BRIGHT_RED, pygame.quit)

        pygame.display.update()
        clock.tick(FPS)

def main():
    spaceship = pygame.Rect(WIDTH/2, HEIGHT * 0.90, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    bullets = []

    run = True
    clock = pygame.time.Clock()

    score = 0
    CHANGE_SCORE = 30
    level = 1

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and len(bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(spaceship.x + spaceship.width//2, spaceship.y, 5, 10)
                    bullets.append(bullet)
            if event.type == BLOCK_HIT:
                score += CHANGE_SCORE
                velocity_increase = 0.3
                if score == 150:
                    create_blocks(1)
                    CHANGE_SCORE = 50
                    level = 2
                elif score == 500:
                    Block.setVelocity(BLOCKS_VELOCITY+velocity_increase)
                    CHANGE_SCORE = 100
                    velocity_increase = 0.6
                    level = 3
                elif score == 2000:
                    create_blocks(1)
                    Block.setVelocity(BLOCKS_VELOCITY+velocity_increase)
                    CHANGE_SCORE = 200
                    level = 4
                    velocity_increase = 1
                elif score == 3400:
                    Block.setVelocity(BLOCKS_VELOCITY+velocity_increase)
                    level = 5
                    CHANGE_SCORE = 400
                elif score == 6600:
                    create_blocks(2)
                    level = 6
                    CHANGE_SCORE = 500
                    velocity_increase = 2
                elif score == 11600:
                    create_blocks(1)
                    Block.setVelocity(BLOCKS_VELOCITY+velocity_increase)
                    level = 7
                    CHANGE_SCORE = 800
                    velocity_increase = 3
                elif score == 19600:
                    Block.setVelocity(BLOCKS_VELOCITY+velocity_increase)
                    create_blocks(1)
                    level = 8
                    CHANGE_SCORE = 1000
                    velocity_increase = 4
                elif score == 29600:
                    Block.setVelocity(BLOCKS_VELOCITY+velocity_increase)
                    create_blocks(2)
                    level = 9

            if event.type == SPACESHIP_HIT:
                level = 1
                score = 0
                blocks.clear()
                create_blocks(BLOCKS_AMT)
                crash()
                run = False
            if event.type == BLOCK_OFF_SCREEN:
                level = 1
                score = 0
                blocks.clear()
                create_blocks(BLOCKS_AMT)
                game_over()
                run = False
                
        
                     
        pygame.display.update()
        keys_pressed = pygame.key.get_pressed()
        user_movement(keys_pressed, spaceship)
        handle_bullets(bullets, blocks)
        block_off_screen(blocks)
        user_hit(blocks, spaceship)
        draw(spaceship, bullets, score, level)
    
    play_again()
    #pygame.quit()

if __name__ == "__main__":
    main()
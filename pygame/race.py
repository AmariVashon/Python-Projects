import pygame
import random as rd
import time

pygame.init()

WIDTH, HEIGHT = 900, 500
FPS = 60
PATH = r'c:/Users/amari/OneDrive/Desktop/Python/pygame/Assets/'

WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)

FONT = pygame.font.SysFont('comicsans', 30)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Race game")

lane1 = pygame.Rect(WIDTH * 0.195, 0, 5, HEIGHT)
lane2 = pygame.Rect(WIDTH * 0.195 * 2, 0, 5, HEIGHT)
lane3 = pygame.Rect(WIDTH * 0.195 * 3, 0, 5, HEIGHT)
lane4 = pygame.Rect(WIDTH * 0.195 * 4, 0, 5, HEIGHT)
finish_line = pygame.Rect(0, 0, WIDTH, 20)

red_car_load = pygame.image.load(PATH+'red_car.png')
red_car = pygame.transform.scale(red_car_load, (55, 75))

yellow_car_load = pygame.image.load(PATH+'yellow_car.png')
yellow_car = pygame.transform.scale(yellow_car_load, (55, 75))

blue_car_load = pygame.image.load(PATH+'blue_car.png')
blue_car = pygame.transform.scale(blue_car_load, (55, 75))

purple_car_load = pygame.image.load(PATH+'purple_car.png')
purple_car = pygame.transform.scale(purple_car_load, (55, 75))

green_car_load = pygame.image.load(PATH+'green_car.png')
green_car = pygame.transform.scale(green_car_load, (55, 75))

def car(x, y, image):
    WIN.blit(image, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()

def display_message(text):
    largeText = pygame.font.SysFont('comicsans', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH/2), (HEIGHT/2))
    WIN.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

def winner(car):
    display_message(car + " has won!")

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(WIN, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(WIN, ic, (x, y, w, h))
    
    text = FONT.render(msg, 1, BLACK)
    WIN.blit(text, (x+w/2 - 16, y+h/2 - 8))

def play_again():
    clock = pygame.time.Clock()
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            
        WIN.fill(WHITE)

        play_question = FONT.render("Do you want to watch again?", 1, BLACK)
        WIN.blit(play_question, (340, 200))

        button("YES", 300, HEIGHT/2, 100, 50, GREEN, BRIGHT_GREEN, main)
        button("NO", WIDTH/2 + 100, HEIGHT/2, 100, 50, RED, BRIGHT_RED, pygame.quit)

        pygame.display.update()
        clock.tick(FPS)
    

def main():
    clock = pygame.time.Clock()
    crashed = False

    red_car_x = WIDTH * 0.27
    red_car_y = HEIGHT * 0.85

    yellow_car_x = WIDTH * 0.47
    yellow_car_y = HEIGHT * 0.85

    blue_car_x = WIDTH * 0.67
    blue_car_y = HEIGHT * 0.85

    purple_car_x = WIDTH * 0.87
    purple_car_y = HEIGHT * 0.85

    green_car_x = WIDTH * 0.07
    green_car_y = HEIGHT * 0.85

    while not crashed:
        red_car_speed = rd.random()
        yellow_car_speed = rd.random()
        blue_car_speed = rd.random()
        purple_car_speed = rd.random()
        green_car_speed = rd.random()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        
        WIN.fill(WHITE)
        pygame.draw.rect(WIN, BLACK, lane1)
        pygame.draw.rect(WIN, BLACK, lane2)
        pygame.draw.rect(WIN, BLACK, lane3)
        pygame.draw.rect(WIN, BLACK, lane4)
        pygame.draw.rect(WIN, RED, finish_line)
        
        red_car_y -= red_car_speed
        yellow_car_y -= yellow_car_speed
        blue_car_y -= blue_car_speed
        purple_car_y -= purple_car_speed
        green_car_y -= green_car_speed

        car(yellow_car_x, yellow_car_y, yellow_car)
        car(red_car_x, red_car_y, red_car)
        car(blue_car_x, blue_car_y, blue_car)
        car(purple_car_x, purple_car_y, purple_car)
        car(green_car_x, green_car_y, green_car)

        if red_car_y < finish_line.y + finish_line.height:
            winner("Red car")
            break
        if yellow_car_y < finish_line.y + finish_line.height:
            winner("Yellow car")
            break
        if blue_car_y < finish_line.y + finish_line.height:
            winner("Blue car")
            break
        if purple_car_y < finish_line.y + finish_line.height:
            winner("Purple car")
            break
        if green_car_y < finish_line.y + finish_line.height:
            winner("Green car")
            break
        
        pygame.display.update()
        clock.tick(FPS)
    play_again()
    #pygame.quit()

if __name__ == "__main__":
    main()
    '''
    pygame.draw.rect(WIN, GREEN, (300, HEIGHT/2, 100, 50))
        pygame.draw.rect(WIN, RED, (WIDTH/2 + 100, HEIGHT/2, 100, 50))

        play_question = FONT.render("Do you want to watch again?", 1, BLACK)
        WIN.blit(play_question, (340, 200))

        yes_text = FONT.render("YES", 1, BLACK)
        WIN.blit(yes_text, (300 + (100/2 - 20), HEIGHT/2 + (50/2) - 5))

        no_text = FONT.render('NO', 1, BLACK)
        WIN.blit(no_text, ((WIDTH/2 + 100) + 100/2 - 18, (HEIGHT/2) + (50/2) - 5))
        '''
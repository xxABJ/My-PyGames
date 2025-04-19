import pygame, os, random
pygame.font.init()
pygame.mixer.init()

#files
import configure
#from configure import *

### Main window and game

WIDTH = 1200
HEIGHT = 800

SPACESHIP_STARTPOINT_LEFTSIDE = {"x":100, "y":WIDTH//2}
SPACESHIP_STARTPOINT_RIGHTSIDE = {"x":1100, "y":WIDTH//2}

VELOCITY = 5
BULLET_VELOCITY = 30
MAX_BULLETS = 4

LEFTSHIP_HIT = pygame.USEREVENT + 1
RIGHTSHIP_HIT = pygame.USEREVENT + 2

LEFTSIDE_HEALTHFONT = pygame.font.SysFont("Impact", 30)
RIGHTSIDE_HEALTHFONT = pygame.font.SysFont("Impact", 30)
WINNER = pygame.font.SysFont("Impact", 50)

BORDER = pygame.Rect(WIDTH//2, 0, 20, HEIGHT)

BG_1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background_solar.png")), (WIDTH, HEIGHT))
BG_2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background_planet.png")), (WIDTH, HEIGHT))
BG_3 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background_cyber.png")), (WIDTH, HEIGHT))
BACKGROUNDS = random.choice([BG_1, BG_2, BG_3])

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders!")

def leftship_handle_movment(key_pressed, leftship_rect):

    if key_pressed[pygame.K_d] and leftship_rect.x + leftship_rect.width + VELOCITY < BORDER.x:
        leftship_rect.x += VELOCITY
    if key_pressed[pygame.K_a] and leftship_rect.x - VELOCITY > 0:
        leftship_rect.x -= VELOCITY
    if key_pressed[pygame.K_s] and leftship_rect.y + leftship_rect.height + VELOCITY < HEIGHT:
        leftship_rect.y += VELOCITY
    if key_pressed[pygame.K_w] and leftship_rect.y - VELOCITY > 0:
        leftship_rect.y -= VELOCITY

def rightship_handle_movment(key_pressed, rightship_rect):

    if key_pressed[pygame.K_RIGHT] and rightship_rect.x + rightship_rect.width + VELOCITY < WIDTH:
        rightship_rect.x += VELOCITY
    if key_pressed[pygame.K_LEFT] and rightship_rect.x - VELOCITY > BORDER.x + BORDER.width:
        rightship_rect.x -= VELOCITY
    if key_pressed[pygame.K_DOWN] and rightship_rect.y + rightship_rect.height + VELOCITY < HEIGHT:
        rightship_rect.y += VELOCITY
    if key_pressed[pygame.K_UP] and rightship_rect.y - VELOCITY > 0:
        rightship_rect.y -= VELOCITY

def bullet_handle(leftship_rect, leftship_bullets, rightship_rect, rightship_bullets):

    for bullet in leftship_bullets:
        bullet.x += BULLET_VELOCITY
        if rightship_rect.colliderect(bullet):
            leftship_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(RIGHTSHIP_HIT))
        elif bullet.x + bullet.width > WIDTH:
            leftship_bullets.remove(bullet)
    
    for bullet in rightship_bullets:
        bullet.x -= BULLET_VELOCITY
        if leftship_rect.colliderect(bullet):
            rightship_bullets.remove(bullet)
            pygame.event.post(pygame.event.Event(LEFTSHIP_HIT))
        elif bullet.x < 0:
            rightship_bullets.remove(bullet)

def winner(winner_text):

    winner_text_object = WINNER.render(str(winner_text), 1 , (220, 150, 10))
    WINDOW.blit(winner_text_object, ((WIDTH - winner_text_object.get_width()) // 2, (HEIGHT - winner_text_object.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(6000)


def draw_window(leftship_sprite, leftship_rect, leftship_colour, rightship_sprite, rightship_rect, rightship_colour, leftship_bullets, rightship_bullets, leftship_health, rightship_health):

    #WINDOW.fill("tan2")
    WINDOW.blit(BACKGROUNDS, (0,0))
    pygame.draw.rect(WINDOW, ("gray25"), BORDER)

    leftside_healthfont_object = LEFTSIDE_HEALTHFONT.render("Health: " + str(leftship_health), 1 , (255, 255, 255))
    rightside_healthfont_object = RIGHTSIDE_HEALTHFONT.render("Health: " + str(rightship_health), 1 , (255, 255, 255))

    WINDOW.blit(leftside_healthfont_object, (20, 20))
    WINDOW.blit(rightside_healthfont_object, (WIDTH - rightside_healthfont_object.get_width() - 20, 20))

    WINDOW.blit(leftship_sprite, leftship_rect)
    WINDOW.blit(rightship_sprite, rightship_rect)

    for bullet in leftship_bullets:
        pygame.draw.rect(WINDOW, (leftship_colour), bullet)
    
    for bullet in rightship_bullets:
        pygame.draw.rect(WINDOW, (rightship_colour), bullet)

    pygame.display.update()

def main(leftship_sprite_rect_bulletcolour, rightship_sprite_rect_bulletcolour):

    leftship_sprite = leftship_sprite_rect_bulletcolour[0]
    leftship_rect = leftship_sprite_rect_bulletcolour[1]
    leftship_colour = leftship_sprite_rect_bulletcolour[2][0]
    leftship_colourtext = leftship_sprite_rect_bulletcolour[2][1]

    rightship_sprite = rightship_sprite_rect_bulletcolour[0]
    rightship_rect = rightship_sprite_rect_bulletcolour[1]
    rightship_colour = rightship_sprite_rect_bulletcolour[2][0]
    rightship_colourtext = rightship_sprite_rect_bulletcolour[2][1]

    leftship_bullets = []
    rightship_bullets = []

    leftship_health = 10
    rightship_health = 10

    run = True
    clock = pygame.time.Clock()
    pygame.init()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b and len(leftship_bullets) < MAX_BULLETS:
                    leftship_bullet = pygame.Rect(leftship_rect.x + leftship_rect.width, leftship_rect.y + leftship_rect.height//2, 10, 5)
                    leftship_bullets.append(leftship_bullet)
                if event.key == pygame.K_RCTRL and len(rightship_bullets) < MAX_BULLETS:
                    rightship_bullet = pygame.Rect(rightship_rect.x, rightship_rect.y + rightship_rect.height//2, 10, 5)
                    rightship_bullets.append(rightship_bullet)
            
            if event.type == LEFTSHIP_HIT:
                leftship_health -= 1
            if event.type == RIGHTSHIP_HIT:
                rightship_health -= 1
            #if event.type == SHOOT:
                #

            winner_text = ""
            if rightship_health == 0:
                winner_text = f"The {leftship_colourtext} ship on the left is the winner!"
            elif leftship_health == 0:
                winner_text = f"The {rightship_colourtext} ship on the right is the winner!"
            if winner_text != "":
                run = False
                winner(winner_text)

        key_pressed = pygame.key.get_pressed()
        draw_window(leftship_sprite, leftship_rect, leftship_colour, rightship_sprite, rightship_rect, rightship_colour, leftship_bullets, rightship_bullets,leftship_health, rightship_health)
        leftship_handle_movment(key_pressed, leftship_rect); rightship_handle_movment(key_pressed, rightship_rect)
        bullet_handle(leftship_rect, leftship_bullets, rightship_rect, rightship_bullets)

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    configure.ROOT.mainloop()                     # starting with tk root because main() is started else where in a func
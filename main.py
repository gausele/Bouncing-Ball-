import pygame
import sys


text_surface = None

def createBall():
    pygame.draw.circle(screen, color, (x,y), radius)

def button():
    pygame.draw.rect(screen, button_color, button_rect)

def button_text():
    but_font = pygame.font.SysFont(None, 12)
    text_surface = but_font.render("Ugly Green Rectangle", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)


pygame.init()
font = pygame.font.SysFont(None, 20)
color = (255, 255, 255)

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

running = True

x,y = WIDTH // 2, HEIGHT // 2
dx, dy = 0, 0
radius = 50
g = 1
accel = 10
counter = 0

clock = pygame.time.Clock()

button_rect = pygame.Rect(2, 2, 100, 50)  
button_color = (0, 255, 0)  
text = None
message_end_time = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Log : BUTTON CLICKED.")
                text = font.render("Wow, you clicked the ugly green rectangular button, you fucking twat", True, (255, 255, 255))
                message_end_time = pygame.time.get_ticks() + 2000
            else:    
                pos = event.pos
                print(pos)
                x,y = pos
        elif event.type == pygame.QUIT:
            running = False

    dy += g
    y += dy


    
    if x - radius <= 0 or x + radius >= WIDTH:
        dx = -dx
    if y + radius >= HEIGHT:
        y = HEIGHT - radius
        dy = -dy*0.7

    screen.fill((0,0,0))
    createBall()
    button()
    button_text()
 
    if text and pygame.time.get_ticks() < message_end_time:
        screen.blit(text, (120, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
print("Successfully imported pygame!")

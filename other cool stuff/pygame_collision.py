import pygame 
import time 

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

font = pygame.font.Font(None, 36)
health = 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("green")
    circle = pygame.draw.circle(screen, "yellow", player_pos, 40)


    #two parrarel lines parameters
    line_w =screen.get_width()
    line_h = screen.get_height()


    line1 = pygame.draw.line(screen, "black", (0,line_h/4), (line_w,line_h/4), 2)
    line2 = pygame.draw.line(screen, "black", (0,line_h*0.75), (line_w,line_h*0.75), 2)
    text = font.render(f"Zycie: {health}", True, "black")
    screen.blit(text, (0, 0))

    if circle.colliderect(line1) or circle.colliderect(line2):
        health -= 1
        if(health <= 0):
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()


    dt = clock.tick(60) / 1000

pygame.quit()

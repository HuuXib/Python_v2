import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True 
dt = 0

#takes the screen height and width(1270x720) and set actual player positon in center of the window 
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


#main loop
while running:
    #loop that take care that my program won't freeze
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
    
    #area color
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    
    #that cares about refreshing my screen so i can se the circle is moving 
    pygame.display.flip()

    #delta time argument cares that my game won't run faster when i play on higher fps rate 
    dt = clock.tick(60) / 1000

pygame.quit()
import pygame

pygame.init()

w, h = 500, 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Moving Ball")

radius = 25
x, y = w // 2, h // 2
speed = 5

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x - radius > 0:
        x -= speed
    if keys[pygame.K_d] and x + radius < w:
        x += speed
    if keys[pygame.K_w] and y - radius > 0:
        y -= speed
    if keys[pygame.K_s] and y + radius < h:
        y += speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
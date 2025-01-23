import pygame
import math

pygame.init()   # For initialization

# Initial values and position
w = 500     # Width for screen
h = 500     # Height for screen
cp = (w/2, h/2) # Center point
pos = [cp[0], cp[1]]    # Initial position as the center point
angle = 0   # Initial angle
rotate = 10 # Rotation speed degrees
move = 10   # Movement speed
screen = pygame.display.set_mode((w, h))

def drawing_the_vectors():
    # x-axis as red for example
    x_axis = (pos[0] + 50 * math.cos(math.radians(angle)), pos[1] + 50 * math.sin(math.radians(angle)))
    pygame.draw.line(screen, (255,0,0), pos, x_axis, 5)

    # y-axis as blue for example
    y_axis = (pos[0] - 50 * math.sin(math.radians(angle)), pos[1] + 50 * math.cos(math.radians(angle)))
    pygame.draw.line(screen, (0,0,255), pos, y_axis, 5)

run = True
while run:
    screen.fill((0, 0, 0))    # Nice black window
    drawing_the_vectors()

    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:  # Left key action: rotation
            angle = angle + rotate
        if key[pygame.K_RIGHT]: # Right key action: rotation (other way)
            angle = angle - rotate
        if key[pygame.K_UP]:  # Up keu action: Move forward in the direction of x-axis (red)
            pos[0] = pos[0] + move * math.cos(math.radians(angle))
            pos[1] = pos[1] + move * math.sin(math.radians(angle))
        if key[pygame.K_DOWN]:  # Down key action: Move backward in the direction of x-axis (red)
            pos[0] = pos[0] - move * math.cos(math.radians(angle))
            pos[1] = pos[1] - move * math.sin(math.radians(angle))
        if key[pygame.K_q]: # q key quits the game and closes the window
            run = False

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()

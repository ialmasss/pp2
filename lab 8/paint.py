import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    x, y = 0, 0
    mode = 'blue'
    tool = 'brush'  
    points = []

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_y:
                    mode = 'yellow'

                if event.key == pygame.K_1:
                    tool = 'rect'
                elif event.key == pygame.K_2:
                    tool = 'circle'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_p:
                    tool = 'brush'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    radius = min(50, radius + 2)
                elif event.button == 3: 
                    radius = max(2, radius - 2)

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points.append((position, tool, mode, radius))
                points = points[-256:]

        screen.fill((255, 255, 255)) 

        for p, tool, color_mode, r in points:
            drawElement(screen, p, tool, color_mode, r)

        pygame.display.flip()
        clock.tick(60)

def drawElement(screen, pos, tool, color_mode, radius):
    colors = {
        'blue': (0, 0, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'yellow': (255, 255, 0),
        'eraser': (255, 255, 255)
    }
    color = colors.get(color_mode, (0, 0, 0))

    if tool == 'brush':
        pygame.draw.circle(screen, color, pos, radius)
    elif tool == 'rect':
        pygame.draw.rect(screen, color, (pos[0] - radius, pos[1] - radius, 2 * radius, 2 * radius))
    elif tool == 'circle':
        pygame.draw.circle(screen, color, pos, radius, 2)
    elif tool == 'eraser':
        pygame.draw.circle(screen, (255, 255, 255), pos, radius)

main()

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
    drawing = False

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
               (event.type == pygame.KEYDOWN and (
                    (event.key == pygame.K_w and ctrl_held) or
                    (event.key == pygame.K_F4 and alt_held) or
                    event.key == pygame.K_ESCAPE)):
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: mode = 'red'
                elif event.key == pygame.K_g: mode = 'green'
                elif event.key == pygame.K_b: mode = 'blue'
                elif event.key == pygame.K_y: mode = 'yellow'

                elif event.key == pygame.K_1: tool = 'rect'
                elif event.key == pygame.K_2: tool = 'circle'
                elif event.key == pygame.K_3: tool = 'square'
                elif event.key == pygame.K_4: tool = 'right_triangle'
                elif event.key == pygame.K_5: tool = 'equilateral_triangle'
                elif event.key == pygame.K_6: tool = 'rhombus'
                elif event.key == pygame.K_e: tool = 'eraser'
                elif event.key == pygame.K_p: tool = 'brush'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    radius = min(50, radius + 2)
                    drawing = True
                elif event.button == 3:
                    radius = max(2, radius - 2)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False

            if event.type == pygame.MOUSEMOTION and drawing:
                position = event.pos
                points.append((position, tool, mode, radius))
                points = points[-512:]

        screen.fill((255, 255, 255))

        for p, tool_name, color_mode, r in points:
            drawElement(screen, p, tool_name, color_mode, r)

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
    if tool == 'eraser':
        color = colors['eraser']

    x, y = pos

    if tool == 'brush':
        pygame.draw.circle(screen, color, pos, radius)
    elif tool == 'rect':
        pygame.draw.rect(screen, color, (x - radius, y - radius, 2 * radius, 2 * radius))
    elif tool == 'circle':
        pygame.draw.circle(screen, color, pos, radius, 2)
    elif tool == 'square':
        pygame.draw.rect(screen, color, (x - radius, y - radius, 2 * radius, 2 * radius))
    elif tool == 'right_triangle':
        points = [(x, y - radius), (x, y + radius), (x + radius, y + radius)]
        pygame.draw.polygon(screen, color, points)
    elif tool == 'equilateral_triangle':
        h = int((3 ** 0.5) / 2 * radius * 2)
        points = [(x, y - h // 2), (x - radius, y + h // 2), (x + radius, y + h // 2)]
        pygame.draw.polygon(screen, color, points)
    elif tool == 'rhombus':
        points = [(x, y - radius), (x - radius, y), (x, y + radius), (x + radius, y)]
        pygame.draw.polygon(screen, color, points)

main()

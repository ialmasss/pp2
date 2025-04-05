import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
speed = 5
snake = [(100, 100)] 
direction = (GRID_SIZE, 0) 

foods = []  # multiple food items
food_spawn_interval = 3000  # ms
food_lifetime = 5000  # ms
last_food_spawn_time = pygame.time.get_ticks()

score = 0
level = 1


def generate_food():
    while True:
        pos = (
            random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
            random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        )
        if pos not in snake and all(f["pos"] != pos for f in foods):
            return {
                "pos": pos,
                "weight": random.randint(1, 3),
                "spawn_time": pygame.time.get_ticks()
            }


running = True
while running:
    screen.fill(BLACK)

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)

    # Spawn new food
    if current_time - last_food_spawn_time > food_spawn_interval:
        foods.append(generate_food())
        last_food_spawn_time = current_time

    # Remove expired food
    foods = [f for f in foods if current_time - f["spawn_time"] < food_lifetime]

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False

    if new_head in snake:
        running = False

    snake.insert(0, new_head)

    eaten = None
    for f in foods:
        if new_head == f["pos"]:
            score += f["weight"]
            eaten = f
            if score % 4 == 0:
                level += 1
                speed += 2
            break
    if eaten:
        foods.remove(eaten)
    else:
        snake.pop()

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

    for f in foods:
        pygame.draw.rect(screen, RED, (*f["pos"], GRID_SIZE, GRID_SIZE))

    font = pygame.font.Font(None, 30)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()

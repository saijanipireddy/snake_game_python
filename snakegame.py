import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("VB Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.SysFont("arial", 24)

# Clock
clock = pygame.time.Clock()

# Snake setup
snake_block = 10
snake_x, snake_y = width // 2, height // 2
change_x, change_y = 0, 0
snake_body = [(snake_x, snake_y)]

# Food setup
def get_new_food():
    return random.randrange(0, width, snake_block), random.randrange(0, height, snake_block)

food_x, food_y = get_new_food()

# Score
score = 0

# Game Over Screen
def game_over_screen():
    game_screen.fill(BLACK)
    game_over_text = font.render("Game Over! Press R to Restart or Q to Quit.", True, RED)
    game_screen.blit(game_over_text, (width // 2 - 200, height // 2 - 20))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# Main game function
def main():
    global change_x, change_y, snake_x, snake_y, food_x, food_y, score, snake_body
    snake_x, snake_y = width // 2, height // 2
    change_x, change_y = 0, 0
    snake_body = [(snake_x, snake_y)]
    food_x, food_y = get_new_food()
    score = 0
    speed = 10

    running = True
    while running:
        clock.tick(speed + score // 5)  # Increase speed with score

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Movement controls
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and change_x == 0:
                    change_x = -snake_block
                    change_y = 0
                elif event.key == pygame.K_RIGHT and change_x == 0:
                    change_x = snake_block
                    change_y = 0
                elif event.key == pygame.K_UP and change_y == 0:
                    change_x = 0
                    change_y = -snake_block
                elif event.key == pygame.K_DOWN and change_y == 0:
                    change_x = 0
                    change_y = snake_block

        snake_x = (snake_x + change_x) % width
        # Update snake position
        snake_y = (snake_y + change_y) % height
        head = (snake_x, snake_y)

        # Collision with itself
        if head in snake_body[:-1]:
            game_over_screen()

        snake_body.append(head)

        # Eat food
        if snake_x == food_x and snake_y == food_y:
            score += 1
            food_x, food_y = get_new_food()
        else:
            snake_body.pop(0)

        # Draw everything
        game_screen.fill(BLACK)
        pygame.draw.rect(game_screen, GREEN, [food_x, food_y, snake_block, snake_block])
        for block in snake_body:
            pygame.draw.rect(game_screen, WHITE, [block[0], block[1], snake_block, snake_block])

        score_text = font.render(f"Score: {score}", True, WHITE)
        game_screen.blit(score_text, (10, 10))

        pygame.display.update()

    pygame.quit()

# Run the game
main()

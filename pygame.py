import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize Snake
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_speed_x = 0
snake_speed_y = 0
snake_body = []
snake_length = 1

# Initialize Food
food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

# Score
score = 0

# Game Over flag
game_over = False

# Main Game Loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_speed_y == 0:
                snake_speed_x = 0
                snake_speed_y = -SNAKE_SIZE
            if event.key == pygame.K_DOWN and snake_speed_y == 0:
                snake_speed_x = 0
                snake_speed_y = SNAKE_SIZE
            if event.key == pygame.K_LEFT and snake_speed_x == 0:
                snake_speed_x = -SNAKE_SIZE
                snake_speed_y = 0
            if event.key == pygame.K_RIGHT and snake_speed_x == 0:
                snake_speed_x = SNAKE_SIZE
                snake_speed_y = 0

    # Move the Snake
    snake_x += snake_speed_x
    snake_y += snake_speed_y

    # Check for collisions with the boundaries
    if snake_x >= WIDTH or snake_x < 0 or snake_y >= HEIGHT or snake_y < 0:
        game_over = True

    # Check for collisions with itself
    for segment in snake_body:
        if segment == (snake_x, snake_y):
            game_over = True

    # Add the current position to the snake's body
    snake_body.append((snake_x, snake_y))

    # Check if the snake ate the food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    else:
        # Remove the last segment of the snake's body if it didn't eat the food
        if len(snake_body) > snake_length:
            del snake_body[0]

    # Clear the screen
    screen.fill(WHITE)

    # Draw the food
    pygame.draw.rect(screen, RED, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    # Update the display
    pygame.display.update()

    # Control game speed
    time.sleep(1 / SNAKE_SPEED)

# Game over message
font = pygame.font.Font(None, 36)
text = font.render(f"Game Over! Your Score: {score}", True, RED)
text_rect = text.get_rect()
text_rect.center = (WIDTH // 2, HEIGHT // 2)
screen.blit(text, text_rect)
pygame.display.update()

# Wait for a few seconds before closing the game
time.sleep(2)

# Quit Pygame
pygame.quit()

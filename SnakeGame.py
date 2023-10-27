import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the snake and food
snake_block_size = 20
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 50)

def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block_size, snake_block_size])

def display_score(score):
    text = score_font.render("Score: " + str(score), True, black)
    window.blit(text, [10, 10])

def game_loop():
    game_over = False
    game_quit = False

    while not game_quit:
        while game_over:
            window.fill(white)
            game_over_text = font_style.render("Game Over!", True, red)
            restart_text = font_style.render("Press Q-Quit or C-Play Again", True, black)
            window.blit(game_over_text, [window_width / 2 - 100, window_height / 2 - 50])
            window.blit(restart_text, [window_width / 2 - 200, window_height / 2])
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Snake initial position
        snake_x = window_width / 2
        snake_y = window_height / 2

        # Snake movement
        snake_x_change = 0
        snake_y_change = 0

        snake_list = []
        snake_length = 1

        # Food initial position
        food_x = round(random.randrange(0, window_width - snake_block_size) / snake_block_size) * snake_block_size
        food_y = round(random.randrange(0, window_height - snake_block_size) / snake_block_size) * snake_block_size

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block_size
                    snake_x_change = 0

        snake_x += snake_x_change
        snake_y += snake_y_change

        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_over = True

        window.fill(white)
        pygame.draw.rect(window, green, [food_x, food_y, snake_block_size, snake_block_size])

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        draw_snake(snake_block_size, snake_list)
        display_score(snake_length - 1)

        pygame.display.flip()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, window_width - snake_block_size) / snake_block_size) * snake_block_size
            food_y = round(random.randrange(0, window_height - snake_block_size) / snake_block_size) * snake_block_size
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()

# Start the game
game_loop()

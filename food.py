import pygame
import random
import snake


class Food():
    def __init__(self, WIDTH, HEIGHT, x, y):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.apple_eaten = True
        self.apple_pos = (20, 20)
        self.s = snake.Snake(WIDTH, HEIGHT)

        self.get_food_position(x, y)

        self.apple = pygame.image.load("res\images\_apple.png")

    def update(self, x, y, game_display):

        self.check_if_eaten(x, y)

        if self.apple_eaten:
            self.get_food_position(x, y)

        self.blit_apple(game_display)

    def get_food_position(self, x, y):

        while True:

            self.apple_pos = (random.randint(self.WIDTH-self.WIDTH, self.WIDTH - 20), random.randint(self.HEIGHT-self.HEIGHT, self.HEIGHT - 20))  # -20 stops the apple spawning off screen
            apple_in_snake = False

            if self.apple_pos[0] % 20 == 0 and self.apple_pos[1] %20 == 0:  # checks if divisible by twenty as snake moves 20 pixels at a time

                for i in range(0, len(x)-1):
                    if x[i]-20 <= self.apple_pos[0] and x[i]+20 >= self.apple_pos[0] and y[i]-20 <= self.apple_pos[1] and y[i]+20 >= self.apple_pos[1]:
                        apple_in_snake = True
                        print("APPLE IN SNAKE!")
                        break
            else:
                continue

            if not apple_in_snake:
                break

        return self.apple_pos

    def check_if_eaten(self, x, y):
        if x[0] <= self.apple_pos[0] and x[0] >= self.apple_pos[0] and y[0] <= self.apple_pos[1] and y[0] >= self.apple_pos[1]:
            self.apple_eaten = True
        else:
            self.apple_eaten = False

    def blit_apple(self, game_display):
        game_display.blit(self.apple, self.apple_pos)



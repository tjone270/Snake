import pygame

white = (255, 255, 255)
black = (0, 0, 0)


class Snake():
    def __init__(self, WIDTH, HEIGHT):
        half_width = WIDTH/2
        half_height = HEIGHT/2
        self.x = [half_width, half_width, half_width]
        self.y = [half_height, half_height-20, half_height-40]
        self.snake_part = pygame.image.load("res\images\snake_part.png")
        self.direction = "up"

    def update(self, game_display):
        self.update_position()
        self.blit_snake(game_display)

    def update_position(self):
        get_key_pressed = pygame.key.get_pressed()

        if get_key_pressed[pygame.K_w] and self.direction != "down":
            self.direction = "up"
        elif get_key_pressed[pygame.K_s] and self.direction != "up":
            self.direction = "down"
        elif get_key_pressed[pygame.K_a] and self.direction != "right":
            self.direction = "left"
        elif get_key_pressed[pygame.K_d] and self.direction != "left":
            self.direction = "right"

        i = len(self.x) - 1

        while i >= 1:   # for loop??
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            i -= 1

        if self.direction == "up":
            self.y[0] += -20
        elif self.direction == "down":
            self.y[0] += 20
        elif self.direction == "left":
            self.x[0] += -20
        elif self.direction == "right":
            self.x[0] += 20

    def add_snake_part(self):
        xy_len = len(self.x)

        if self.direction == "up":
            self.x.append(self.x[xy_len-1])
            self.y.append(self.y[xy_len-1] + 20)
        elif self.direction == "down":
            self.x.append(self.x[xy_len-1])
            self.y.append(self.y[xy_len-1] - 20)
        elif self.direction == "left":
            self.x.append(self.x[xy_len-1] + 20)
            self.y.append(self.y[xy_len-1])
        elif self.direction == "right":
            self.x.append(self.x[xy_len-1] - 20)
            self.y.append(self.y[xy_len-1])

    def check_in_bounds(self, WIDTH, HEIGHT):
        if self.x[0] + 9 > WIDTH or self.x[0] + 9 < WIDTH - WIDTH or self.y[0] + 9 > HEIGHT or self.y[0] + 9 < HEIGHT - HEIGHT:
            return True

    def blit_snake(self, game_display):
        for i in range(0, len(self.x)):
            game_display.blit(self.snake_part, (self.x[i], self.y[i]))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
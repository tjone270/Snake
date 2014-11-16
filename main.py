import pygame
import snake
import food
import winsound

WIDTH = 1280
HEIGHT = 720

white = (255, 255, 255)
black = (0, 0, 0)


class Display():
    def __init__(self):
        pygame.init()

        #self.play_sound("res\sounds\song.wav")

        self.score = 0
        self.smallfont = pygame.font.SysFont("monospace", 15)
        self.largefont = pygame.font.SysFont("monospace", 50)

        self.s = snake.Snake(WIDTH, HEIGHT)
        self.f = food.Food(WIDTH, HEIGHT, self.s.get_x(), self.s.get_y())

        self.game_display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Snake - Daniel Sykes")

    def play_sound(self, file_path):
        winsound.PlaySound(file_path, winsound.SND_FILENAME | winsound.SND_ASYNC)

    def game_loop(self):
        dead = False
        while True:

            if dead:
                pygame.time.wait(2000)
                d = Display()
                d.game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.game_display.fill(white)

            self.s.update(self.game_display)  # update snake

            self.f.update(self.s.get_x(), self.s.get_y(), self.game_display)  # update food
            if self.f.apple_eaten:
                self.play_sound("res\sounds\eat.wav")
                self.score += 1
                self.s.add_snake_part()
                self.f.apple_eaten = False

            if self.s.check_in_bounds(WIDTH, HEIGHT):
                txt_you_died = self.largefont.render("YOU DIED", 1, black)
                self.game_display.blit(txt_you_died, (WIDTH/2 - 130, HEIGHT/2 - 30))
                dead = True

            label = self.smallfont.render("Score: "+ str(self.score), 1, black)
            self.game_display.blit(label, (20, 20))

            pygame.display.update()
            self.clock.tick(10)



if __name__ == '__main__':
    d = Display()
    d.game_loop()
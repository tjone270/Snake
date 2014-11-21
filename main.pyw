import pygame
import menu
import snake
import food
import os; os.environ['SDL_VIDEO_CENTERED'] = '1'  # centers pygame window

WIDTH = 720
HEIGHT = 520

white = (255, 255, 255)
black = (0, 0, 0)


class Display():
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        self.game_display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Snake - Daniel Sykes")

        pygame.mixer.music.load("res\sounds\song.wav")
        pygame.mixer.music.set_volume(0.2)

        self.score = 0
        self.totalTicks = 0
        self.game_speed = 30
        self.smallfont = pygame.font.SysFont("monospace", 15)
        self.largefont = pygame.font.SysFont("monospace", 50)

        self.s = snake.Snake(WIDTH, HEIGHT)
        self.f = food.Food(WIDTH, HEIGHT, self.s.get_x(), self.s.get_y())
        self.m = menu.Menu()

        self.eat_sound = pygame.mixer.Sound("res\sounds\eat.wav")
        self.dead_sound = pygame.mixer.Sound("res\sounds\dead.wav")

    def game_loop(self):  # MAIN LOOP
        dead = False
        global scoreTime
        global score
        first_loop = True
        while True:

            if self.m.in_menu:
                self.m.run(self.game_display, WIDTH, HEIGHT)

            if self.m.get_playing():
                if first_loop:
                    self.game_speed = self.m.get_game_speed()

                if not pygame.mixer.music.get_busy() and self.m.get_music() == "On":
                    pygame.mixer.music.play()

                if dead:
                    pygame.mixer.music.stop()
                    if self.m.get_sfx() == "On":
                        self.dead_sound.play()
                    pygame.time.wait(1500)
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
                    if self.m.get_sfx() == "On":
                        self.eat_sound.play()
                    score = 10
                    self.score += int(score)

                    self.s.add_snake_part()
                    self.f.apple_eaten = False

                if self.s.check_out_bounds(WIDTH, HEIGHT):
                    txt_you_died = self.largefont.render("YOU DIED", 1, black)
                    self.game_display.blit(txt_you_died, (WIDTH/2 - 130, HEIGHT/2 - 30))
                    dead = True


                if self.s.check_crashed():
                    txt_you_died = self.largefont.render("YOU DIED", 1, black)
                    self.game_display.blit(txt_you_died, (WIDTH/2 - 130, HEIGHT/2 - 30))
                    dead = True

                label = self.smallfont.render("Score: "+ str(self.score), 1, black)
                self.game_display.blit(label, (20, 20))

            if self.m.playing and first_loop:
                for x in range(2, 0, -1):
                    countdown_txt = self.largefont.render(str(x), 1, black)
                    self.game_display.blit(countdown_txt, (WIDTH/2 - 5, HEIGHT/2 - 100))
                    pygame.display.update()
                    self.clock.tick(self.game_speed)
                    pygame.time.wait(1000)
                    pygame.draw.rect(self.game_display, white, (WIDTH/2 - 5, HEIGHT/2 - 100, 40, 50), 0)

                first_loop = False


            pygame.display.update()
            self.clock.tick(self.game_speed)

if __name__ == '__main__':
    d = Display()
    d.game_loop()
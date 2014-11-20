import pygame

white = (255, 255, 255)
black = (0, 0, 0)
grey_dull = (180, 180, 180)
grey = (220, 220, 220)
red_dull = (180, 0, 0)
green_dull = (0, 180, 0)
red = (255, 0, 0)
green = (0, 255, 0)


class Menu():
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        self.clock = pygame.time.Clock()
        self.in_menu = True
        self.playing = False
        self.buttonfont = pygame.font.SysFont("monospace", 25)
        self.get_diff = False
        self.game_speed = 30
        self.main_menu = True
        self.option_menu = False
        self.menu_sound = pygame.mixer.Sound("res\sounds\_button.wav")
        self.music = True
        self.sfx = True

    def menu_button(self, msg, game_display, x, y, w, h, ic, ac, action=None):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        get_key_pressed = pygame.key.get_pressed()

        if get_key_pressed[pygame.K_ESCAPE]:
            self.get_diff = False
            self.option_menu = False
            self.main_menu = True

        if x + w > mouse_pos[0] > x and y + h > mouse_pos[1] > y:  # checks if in bounds of  box:
            pygame.draw.rect(game_display, ac, (x, y, w, h))  # (---, ---, (x, y, width, height))
            if mouse_click[0] == 1 and action != None:
                if not self.playing:
                    self.menu_sound.play()
                action()

        else:

            pygame.draw.rect(game_display, ic, (x, y, w, h))  # button

        textsurf, textrect = self.text_objects(msg, self.buttonfont)
        textrect.center = (x + w/2, y + h/2)
        game_display.blit(textsurf, textrect)

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def run(self, game_display, WIDTH, HEIGHT):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(white)

        if self.option_menu:  # Option menu
            buttonwidth = WIDTH/5 + 20; buttonheight = HEIGHT/16 + 10; buttonx = WIDTH/2 - buttonwidth/2; buttony = HEIGHT/2 - buttonheight
            self.menu_button("Music: "+ self.get_music(), game_display, buttonx, buttony, buttonwidth, buttonheight, grey_dull, grey, self.set_music)
            buttony = HEIGHT/2 + buttonheight
            self.menu_button("SFX: "+ self.get_sfx(), game_display, buttonx, buttony, buttonwidth, buttonheight, grey_dull, grey, self.set_sfx)

        elif self.get_diff:  # Difficulty menu
            buttonwidth = WIDTH/5; buttonheight = HEIGHT/16 + 10; buttonx = WIDTH*0.2 - buttonwidth/2; buttony = HEIGHT - HEIGHT/2
            self.menu_button("Normal", game_display, buttonx, buttony, buttonwidth, buttonheight, green_dull, green, self.set_game_speed_normal)

            buttonx =  WIDTH*0.5 - buttonwidth/2
            self.menu_button("Hard", game_display, buttonx, buttony, buttonwidth, buttonheight, green_dull, green, self.set_game_speed_hard)

            buttonx =  WIDTH*0.8 - buttonwidth/2
            self.menu_button("Insane", game_display, buttonx, buttony, buttonwidth, buttonheight, green_dull, green, self.set_game_speed_insane)

        elif self.main_menu: # Main Menu
            buttonwidth = WIDTH/2; buttonheight = HEIGHT/8; buttonx = 0 + buttonwidth/2; buttony = HEIGHT - HEIGHT/1.5;  # text not actually button
            self.menu_button("Snake - Daniel Sykes", game_display, buttonx, buttony, buttonwidth, buttonheight, white, white)

            buttonx = WIDTH/5; buttony = HEIGHT - HEIGHT/3.5; buttonwidth = WIDTH/5; buttonheight = HEIGHT/8
            self.menu_button("Start", game_display, buttonx, buttony, buttonwidth, buttonheight, green_dull, green, self.get_difficulty)  # Start button

            buttonx = WIDTH - (WIDTH/5)*2 ; buttony =  HEIGHT - HEIGHT/3.5;
            self.menu_button("Exit", game_display, buttonx, buttony, buttonwidth, buttonheight, red_dull, red, self.quit_game)  # Quit button

            buttonheight = HEIGHT/16 + 10; buttonx = WIDTH - buttonwidth - 10 ; buttony =  0 + HEIGHT/10;
            self.menu_button("Options", game_display, buttonx, buttony, buttonwidth, buttonheight, grey_dull, grey, self.get_options)  # Options button

    def get_difficulty(self):
        self.get_diff = True
        self.main_menu = False

    def get_options(self):
        self.get_diff = False
        self.main_menu = False
        self.option_menu = True

    def set_music(self):
        if self.music:
            self.music =  False
        else:
            self.music = True
        pygame.time.wait(200)

    def set_sfx(self):
        if self.sfx:
            self.sfx = False
        else:
            self.sfx = True
        pygame.time.wait(200)

    def get_music(self):
        if self.music:
            return "On"
        else:
            return "Off"

    def get_sfx(self):
        if self.sfx:
            return "On"
        else:
            return "Off"


    def get_game_speed(self):
        return self.game_speed

    def set_game_speed_normal(self):
        self.game_speed = 10
        self.playing = True
        self.menu = False
    def set_game_speed_hard(self):
        self.game_speed = 20
        self.playing = True
        self.menu = False
    def set_game_speed_insane(self):
        self.game_speed = 30
        self.playing = True
        self.menu = False

    def quit_game(self):
        pygame.quit()
        quit()

    def get_playing(self):
        return self.playing

    def reset_vars(self):
        self.in_menu = True
        self.playing = False
        self.get_diff = False
        self.game_speed = 30
        self.main_menu = True
        self.option_menu = False






import pygame
import downloads
import Ball
import Gamer
import settings
import menu
import time
import pygame.freetype
import win_or_lose as wor


class Game:
    def __init__(self):
        self.value_for_while = True
        self.menu_mode = True
        self.window = pygame.display.set_mode(settings.SIZE)
        pygame.display.set_caption("ICE CREAM BALLS")
        self.clock = pygame.time.Clock()
        self.menu = menu.Menu(self)
        self.gamer = Gamer.Gamer(self)
        self.fp = 0
        self.balls_list = []
        self.music = downloads.back_mus
        self.lives = 3
        self.balls = Ball.Balls(self)
        self.font = pygame.freetype.Font(None, 24)
        self.condition = None
        self.wor = wor.end(self)

    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.value_for_while = False

    def draw(self):
        self.window.blit(downloads.back, [0, 0])
        self.gamer.draw(self.window)
        # self.balls.draw()
        if self.fp % 50 == 0:
            self.balls = Ball.Balls(self)
            self.balls_list.append(self.balls)

        for i in self.balls_list:
            i.draw()
        self.font.render_to(self.window, [0, 0], f'{self.fp // 100}', [24, 240, 31])



    def update(self):
        self.gamer.update()
        for ball in self.balls_list:
            if self.gamer.hitbox.colliderect(ball.hitbox) == True:
                self.balls_list.remove(ball)
                if self.gamer.hitbox.w <= ball.hitbox.w:
                    self.lives -= 1
                else:
                    self.gamer.change_size()
        for i in self.balls_list:
            i.update()
        if self.lives == 0:
            print('lose')

    def start(self):
        while self.value_for_while == True:
            if self.menu_mode == True:
                self.menu.draw()
                self.menu.events()

            elif self.condition != None:
                self.wor.draw()


            else:

                self.draw()
                self.events()
                self.update()
                self.music.play(-1)
            pygame.display.update()
            self.fp += 1
            self.clock.tick(100)


game = Game()
game.start()

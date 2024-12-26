import pygame
import downloads


class Win:
    def __init__(self, game):
        self.game = game
        self.picture = downloads.win
        self.hitbox = pygame.Rect([0, 0], self.picture.get_size())

    def draw(self):
        self.game.window.blit(self.picture, self.hitbox)

    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.game.value_for_while = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.condition = ''
                    self.game.work = True
                    self.game.menu_mode = True


class Lose:
    def __init__(self, game):
        self.game = game
        self.picture = downloads.lose
        self.hitbox = pygame.Rect([0, 0], self.picture.get_size())

    def draw(self):
        self.game.window.blit(self.picture, self.hitbox)

    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.game.value_for_while = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.condition = ''
                    self.game.work = True
                    self.game.menu_mode = True


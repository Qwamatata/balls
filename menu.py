import pygame
import downloads
import pygame.freetype
class Menu:
    def __init__(self, game):
        self.picture = downloads.menu
        self.game = game
        self.text = pygame.freetype.Font(None,28)
        self.picture_1 = downloads.button
        self.music = downloads.start
    def draw(self):
        self.game.window.blit(self.picture,[0,0])
        self.text.render_to(self.game.window,[0,0],'PRESS Esc FOR START!',[247, 99, 99])
        self.game.window.blit(self.picture_1,[0,0])

    def events(self):

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.game.value_for_while = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.music.play()
                    self.game.menu_mode = False
                    self.game.lives = 3
                    self.game.food = 0
                    self.game.fp = 0
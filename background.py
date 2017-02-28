import pygame;
from pygame.sprite import Sprite

class Background(Sprite):
    def __init__(self,game_settings):
        pygame.sprite.Sprite.__init__(self);
        self.image = pygame.image.load("./images/sm_bg.png");
        self.image = pygame.transform.scale(self.image,(game_settings.screen_size[0],game_settings.screen_size[1]));
        self.rect = self.image.get_rect();
        self.rect.left = 0;
        self.rect.top = 0;

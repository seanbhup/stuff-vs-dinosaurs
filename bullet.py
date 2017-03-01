import pygame;
from pygame.sprite import Sprite;

class Bullet(Sprite):
    def __init__(self,screen,character):
        super(Bullet,self).__init__();
        self.screen = screen;
        self.screen_rect = self.screen.get_rect();
        self.image = pygame.image.load("./images/mage_bullet.png");
        self.image = pygame.transform.scale(self.image,(30,30));
        self.rect = self.image.get_rect();

        self.rect.centerx = character.rect.right - 10;
        self.rect.top = character.rect.top;

        self.x = self.rect.x;
        self.y = self.rect.y;
    def update(self,character):
        self.x += 10 * character.shoot_speed;
        self.rect.x = self.x;
    def draw(self):
        self.screen.blit(self.image, self.rect)

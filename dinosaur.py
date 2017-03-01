import pygame;
from pygame.sprite import Sprite;

class Dinosaur(Sprite):
    def __init__(self,screen,speed,health):
        super(Dinosaur,self).__init__();
        self.speed = speed;
        self.health = health;
        self.image = pygame.image.load("./images/dino_walk1.png");
        self.image = pygame.transform.scale(self.image,(100,53));
        self.rect = self.image.get_rect();
        self.screen = screen;
        self.screen_rect = screen.get_rect();
        self.rect.centery = self.screen_rect.centery + 40;
        self.rect.right = self.screen_rect.right + 100;

        self.x = float(self.rect.x);

    def update(self):
        self.x -= self.speed * 5;
        self.rect.x = self.x;


    def draw(self):
        self.screen.blit(self.image, self.rect);

    def hit(self,damage):
        self.health -= damage;

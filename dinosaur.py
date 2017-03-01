import pygame;
from pygame.sprite import Sprite;
from random import randint;


class Dinosaur(Sprite):
    def __init__(self,screen,game_settings):
        super(Dinosaur,self).__init__();
        self.speed = game_settings.dinosaur_speed;
        self.health = game_settings.dinosaur_health;
        self.image = pygame.image.load("./images/michael.png");
        self.image = pygame.transform.scale(self.image,(90,90));
        self.rect = self.image.get_rect();
        self.screen = screen;
        self.screen_rect = screen.get_rect();

        self.yard_row = randint(0,4)
        self.rect.centery = game_settings.squares["rows"][self.yard_row] + 40;
        self.rect.right = self.screen_rect.right;

        game_settings.dinosaur_in_row[self.yard_row] += 1





        self.x = float(self.rect.x);

    def update(self):
        self.x -= self.speed * 5;
        self.rect.x = self.x;





    def draw(self):
        self.screen.blit(self.image, self.rect);

    def hit(self,damage):
        self.health -= damage;

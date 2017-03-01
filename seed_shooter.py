import pygame;
from pygame.sprite import Sprite;
from character import Character;

class Seed_Shooter(Character):
    def __init__(self,screen,square):
        self.screen = screen;
        self.shoot_speed = 2;
        self.health = 5;
        self.image_file = "./images/mage_shooting_middle.png";
        self.square = square

        super(Seed_Shooter,self).__init__();

import pygame;
from pygame.sprite import Sprite;
from character import Character;

class Mage_Shooter(Character):
    def __init__(self,screen,square):
        self.screen = screen;
        self.shoot_speed = 10;
        self.health = 5;
        self.image_file = "./images/mage.png";
        self.square = square

        super(Seed_Shooter,self).__init__();

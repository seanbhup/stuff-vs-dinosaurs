import pygame;
from pygame.sprite import Sprite;

class Character(Sprite):
    def __init__(self):
        super(Character,self).__init__();
        self.screen_rect = self.screen.get_rect();
        self.image = pygame.image.load(self.image_file);
        self.image = pygame.transform.scale(self.image,(100,80));
        self.rect = self.image.get_rect();

        self.rect.left = self.square.rect.left # + 10;
        self.rect.top = self.square.rect.top;
        self.yard_row = self.square.row_number

        self.last_shot = 0;
        
    def draw(self):
        self.screen.blit(self.image, self.rect);

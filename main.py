import pygame;
import sys;
import os
from settings import Settings;
from background import Background;
from square import Square;
from character import Character;
from dinosaur import Dinosaur;
from bullet import Bullet;
import game_functions as game_func
from pygame.sprite import Group, groupcollide;

pygame.init();
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size);
pygame.display.set_caption("STUFF VS. DINOSAURS");
background = Background(game_settings);


dinosaurs = Group();
characters = Group();
squares = Group();
bullets = Group();



for i in range(0,5):
    for j in range(0,9):
        squares.add(Square(screen,game_settings,i,j));

def run_game():
    tick = 0;
    while 1923014810498219048120948:
        if game_settings.game_active:
            game_func.check_events(screen,game_settings,squares,characters,bullets)
            # screen.fill(game_settings.bg_color);
            tick += 1;
            if tick % 30 == 0 or tick == 1:
                dinosaurs.add(Dinosaur(screen,game_settings));


            dinosaur_got_shot = groupcollide(dinosaurs,bullets,False,False);
            character_got_hit = groupcollide(dinosaurs,characters,False,True);
            for dinosaur in dinosaur_got_shot:
                # print dinosaur;
                if dinosaur.yard_row == dinosaur_got_shot[dinosaur][0].yard_row:
                    bullets.remove(dinosaur_got_shot[dinosaur][0])
                    dinosaur.hit(1);
                    if(dinosaur.health <= 0):
                        dinosaurs.remove(dinosaur);
                        # os.system("say ow")
                        game_settings.dinosaur_in_row[dinosaur.yard_row] -= 1;


        game_func.update_screen(screen,game_settings,background,dinosaurs,squares,characters,bullets,tick);
        pygame.display.flip();

run_game();

import pygame;
import sys;
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
        game_func.check_events(screen,game_settings,squares,characters,bullets)
        game_func.update_screen(screen,game_settings,background,dinosaurs,squares,characters,bullets,tick);
        # screen.fill(game_settings.bg_color);
        tick += 1;
        if tick % 110 == 0:
            dinosaurs.add(Dinosaur(screen,game_settings.dinosaur_speed,game_settings.dinosaur_health));


        dinosaur_got_shot = groupcollide(dinosaurs,bullets,False,True);
        character_got_hit = groupcollide(dinosaurs,characters,False,True);
        for dinosaur in dinosaur_got_shot:
            print dinosaur;
            dinosaur.hit(1);
            if(dinosaur.health <= 0):
                dinosaurs.remove(dinosaur);

        # if dinosaur_got_shot:
        #     game_settings.dinosaur_health -= 1
        #     if game_settings.dinosaur_health == 0:
        #         dinosaur_got_shot = groupcollide(dinosaurs,bullets,True,True);
        # else:
        #     game_settings.dinosaur_health = game_settings.dinosaur_health;



        pygame.display.flip();

run_game();

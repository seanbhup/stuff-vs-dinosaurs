import sys;
import pygame;
from seed_shooter import Seed_Shooter;
from mage_shooter import Mage_Shooter;
from bullet import Bullet;
from pygame.sprite import Group, groupcollide;


def check_events(screen,game_settings,squares,characters,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            syst.exit();
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos();
            # print mouse_x;
            # print mouse_y;
            # print squares;
            for square in squares:
                if square.rect.collidepoint(mouse_x,mouse_y):
                    # print "Square #",square.square_number;
                    characters.add(Seed_Shooter(screen,square));
                # elif square.rect.collidepoint(mouse_x,mouse_y) and event.type == pygame.KEY_SPACE:
                #     characters.add(Mage_Shooter(screen,square));
        elif (event.type == pygame.MOUSEBUTTONDOWN) and (event.type == pygame.KEYDOWN):
            mouse_x,mouse_y = pygame.mouse.get_pos();
            for square in squares:
                if (event.key == pygame.K_SPACE):
                    characters.add(Mage_Shooter(screen,square));

        elif event.type == pygame.MOUSEMOTION:
            # print event.pos
            for square in squares:
                if square.rect.collidepoint(event.pos):
                    game_settings.highlighted_square = square
                    print game_settings.highlighted_square;







def update_screen(screen,game_settings,background,dinosaurs,squares,characters,bullets,tick):
    screen.blit(background.image, background.rect)

    if game_settings.highlighted_square != 0:
        pygame.draw.rect(screen, (51, 153, 255),(game_settings.highlighted_square.rect.left,game_settings.highlighted_square.rect.top,game_settings.squares["square_width"],game_settings.squares["square_height"]),5)

    for dinosaur in dinosaurs.sprites():
        dinosaur.update();
        dinosaur.draw();

    for character in characters:
        character.draw();
        if tick % 90 == 0:
            bullets.add(Bullet(screen,character))

    for bullet in bullets.sprites():
        bullet.update(character);
        bullet.draw();

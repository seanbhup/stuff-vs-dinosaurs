import pygame

class Settings():
    def __init__(self):
        display_info = pygame.display.Info();
        self.screen_size = (display_info.current_w, display_info.current_h)
        self.bg_color = (51, 153, 255)
        self.dinosaur_speed = .5;
        self.dinosaur_health = 1;
        self.game_active = True;


        self.squares = {
            "start_left": 330,
            "start_top": 220,
            "square_width": 102,
            "square_height": 90,
            "rows": [
                220,
                310,
                400,
                490,
                580
            ]
        };
        self.highlighted_square = 0;
        self.dinosaur_in_row = [
            0,
            0,
            0,
            0,
            0,
        ];

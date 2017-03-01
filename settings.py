import pygame

class Settings():
    def __init__(self):
        display_info = pygame.display.Info();
        self.screen_size = (display_info.current_w, display_info.current_h)
        self.bg_color = (51, 153, 255)
        self.dinosaur_speed = 2;
        self.dinosaur_health = 5;

        self.squares = {
            "start_left": 330,
            "start_top": 220,
            "square_width": 102,
            "square_height": 90,
            "rows": [
                330,
                432,
                534,
                636,
                738
            ]
        };
        self.highlighted_square = 0;

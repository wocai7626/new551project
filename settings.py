class Settings():

    def __init__(self):
        # screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # screen

        # ship
        #self.ship_speed_factor = 40
        self.ship_limit = 3
        # ship

        # bullet
        #self.bullet_speed_factor = 20
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # bullet

        # alien
        #self.alien_speed_factor = 2
        self.fleet_drop_speed = 100
        #self.fleet_direction = 1
        # alien
        
        #game speed up and game score
        self.score_scale = 1.5
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        #game speed up and game score
    
    def initialize_dynamic_settings(self):
        #ship bullet alien speed
        self.ship_speed_factor = 40
        self.bullet_speed_factor = 20
        self.alien_speed_factor = 5
        #ship bullet alien speed

        #fleet direction
        self.fleet_direction = 1
        #fleet direction

        #points
        self.alien_points = 50
        #points

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
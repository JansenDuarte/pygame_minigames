import pygame as pg
import random as rng
import time
from settings import global_settings as gs
from core.game_obj import GameObject
from core.input import Input

class Ball(GameObject):
    pos = pg.Vector2(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 2)
    size = 20

    spawned_time = time.time()

    sfx_source = None

    def __init__(self):
        super().__init__(self.pos, self.size, 'red')
        pg.mixer.init()
        self.sfx_source = pg.mixer.Sound("assets/audio/sfx/8bit_hit_by_jeckkech.wav")


    def update(self):
        if Input.get_button_down(1):
            if super().detect_click(pg.mouse.get_pos()):
                self.sfx_source.play()
                self.random_pos()
                print(f"clicked on the object! new pos: {self.pos}")
                print(f"time to get to it: {time.time() - self.spawned_time}")
                self.spawned_time = time.time()
            else:
                print("hit the rocks... pickaxe got duller")


    def random_pos(self, x_max = None, y_max = None):
        half_size = int(self.size / 2)
        new_x = rng.randint(0 + half_size, gs.SCREEN_WIDTH - half_size)
        new_y = rng.randint(0 + half_size, gs.SCREEN_HEIGHT - half_size)
        self.pos = pg.Vector2(new_x, new_y)

    def draw(self, screen):
        super().draw(screen)

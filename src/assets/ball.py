import pygame as pg
import random as rng
import time
from settings import global_settings as gs
from core.game_obj import GameObject
from core.input import Input

class Ball(GameObject):

    spawned_time = time.time()

    def __init__(self):
        super().__init__(
                pg.Vector2(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 2), 
                pg.Vector2(20, 20), 
                'red', 
                None, 
                pg.mixer.Sound("assets/audio/sfx/8bit_hit_by_jeckkech.wav"))

        self.name = 'Ore #1'
        self.sprite = pg.image.load("assets/sprites/ore.png").convert_alpha()
        self.sprite = pg.transform.scale(self.sprite, (self.size.x, self.size.y))


    def update(self):
        #0 == left mouse button
        if Input.get_button_down(0):
            if super().detect_click(pg.mouse.get_pos()):
                self.sfx_source.play()
                self.random_pos()
                print(f"clicked on the object! new pos: {self.position}")
                print(f"time to get to it: {time.time() - self.spawned_time}")
            else:
                print("hit the rocks... pickaxe got duller")

        super().update()


    def random_pos(self):
        new_x = rng.uniform(0 + self.half_size.x, gs.SCREEN_WIDTH - self.half_size.x)
        new_y = rng.uniform(0 + self.half_size.y, gs.SCREEN_HEIGHT - self.half_size.y)
        self.position = pg.Vector2(new_x, new_y)

    def draw(self, screen):
        super().draw(screen)

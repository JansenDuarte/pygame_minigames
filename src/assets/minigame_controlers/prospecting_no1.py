import pygame as pg
import random as rng
import time
from utils.time import Time
from settings import global_settings as gs
from core.game_obj import GameObject
from core.game_ui import GameUI
from core.input import Input

class ProspectingMinigame_No1(GameObject):
    minigame_active = True
    timer = 0
    minigame_timer = 30

    current_boost = 0
    max_boost = 0
    min_boost = 0
    boost_inc = 60
    boost_decay = 1
    combo = 1
    boost_going_up = False

    #TODO: control UI with some other thing later
    font = None
    timer_text = ""
    timer_text_surf = None

    boost_text = ""
    boost_text_surf = None

    combo_text = ""
    combo_text_surf = None

    spawned_time = time.time()

    def __init__(self):
        super().__init__(
                position=pg.Vector2(gs.SCREEN_WIDTH / 2, gs.SCREEN_HEIGHT / 2), 
                size=pg.Vector2(40, 40), 
                color=None, 
                sprites=['assets/sprites/scrap_rocks.png',
                         'assets/sprites/ore.png'], 
                sfx_sources=["assets/audio/sfx/8bit_hit_by_jeckkech.wav"],
                bgm_sources=None
                )

        self.name = 'Ore #1'
        self.font = GameUI.Instance.load_font('arial', 16)
        self.timer_text = GameUI.Instance.create_text("", (10, 10), "white", self.font)
        self.boost_text = GameUI.Instance.create_text("", (10, 100), "white", self.font)
        self.combo_text = GameUI.Instance.create_text("", (10, 400), "white", self.font)

    def update(self):
        if self.minigame_active:
            self.process_input()
            self.process_boost()
            super().update()
            self.timer += Time.deltaTime
            if self.timer > self.minigame_timer:
                self.end_minigame()

            self.ui_refresh()


    def draw(self, screen):
        super().draw(screen)

    def ui_refresh(self):
        timer = (self.minigame_timer - self.timer)
        if timer < 0:
            timer = 0.0
        self.timer_text.text = f"Time remaining: {(timer):.2f}"
        self.boost_text.text = f"Current boost: {(self.current_boost / 1000):.2f}"
        self.combo_text.text = f"Combo: x{self.combo}"

    def random_pos(self):
        new_x = int(rng.uniform(0 + self.half_size.x, 
                            gs.SCREEN_WIDTH - self.half_size.x))
        new_y = int(rng.uniform(0 + self.half_size.y, 
                            gs.SCREEN_HEIGHT - self.half_size.y))
        self.position = pg.Vector2(new_x, new_y)

    def process_input(self):
        #0 == left mouse button
        if Input.get_button_down(0):
            if super().detect_click(pg.mouse.get_pos()):
                self.combo += 1
                self.boost_going_up = True
                self.current_boost += self.boost_inc
                #HACK: should know what sfx to play
                self.sfx_sources[0].play()
                self.random_pos()
                # print(f"clicked on the object! new pos: {self.position}")
                # print(f"time to get to it: {time.time() - self.spawned_time}")
                self.spawned_time = time.time()
            else:
                self.combo = 1
                self.boost_going_up = False
                print("hit the rocks... pickaxe got duller")

        #TODO: make this only go down after some time
        self.boost_going_up = False


    def process_boost(self)-> None:
        if self.boost_going_up:
            return None
        else:
            #TODO: this needs a better calculation
            self.current_boost -= self.boost_decay 
            if self.current_boost < self.min_boost:
                self.current_boost = self.min_boost


    def end_minigame(self):
        self.minigame_active = False
        self.position = pg.Vector2(10000, 10000)
        super().update()







import pygame as pg
from settings import global_settings as gs
from utils.time import Time
#this is kinda wierd
from assets.ball import Ball

class GameManager:
    Instance = None

    def __new__(cls):
        if cls.Instance is None:
            cls.Instance = super().__new__(cls)
        return cls.Instance

    screen = None
    clock = None
    game_objects = None
    __running = False
    __paused = False
    __quitting = False

    def init(self):
        pg.init()
        self.screen = pg.display.set_mode((gs.SCREEN_WIDTH, gs.SCREEN_HEIGHT))
        pg.display.set_caption("Prospecting Minigame")
        self.clock = pg.time.Clock()
        self.__running = True
        
        #TODO do a load scene from file or something like that

        ball = Ball()
        self.game_objects = []
        self.game_objects.append(ball)

        self.game_loop()

    def game_loop(self) -> None:
        while self.__running:
            self.screen.fill("black")

            for obj in self.game_objects:
                obj.update()
                obj.draw(self.screen)


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.__quitting = True
                    self.end_game()
                    return None


            pg.display.flip()

            pg.event.pump()

            Time.deltaTime = self.clock.tick(60) / 1000


    def end_game(self):
        # dispose of all
        pg.quit()

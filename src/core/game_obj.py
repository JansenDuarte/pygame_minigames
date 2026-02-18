import pygame as pg

class GameObject:
    enabled = True
    position = pg.Vector2(0, 0)
    size = 0

    color = pg.Color('white')

    def __init__(self, position: pg.Vector2, size: int, color: pg.Color = 'white'):
        self.position = position
        self.size = size
        self.color = color

    #TODO actualy update
    def update(self):
        pass

    def draw(self, screen): 
        # everything is a square
        r = pg.Rect(self.pos.x, self.pos.y, self.size, self.size)
        pg.draw.rect(screen, self.color, r)
 
    def detect_click(self, click_pos : pg.Vector2) -> bool:
        # always treat as a square
        if (click_pos[0] > self.pos.x - self.size and
            click_pos[0] <self.pos.x + self.size):
            
            if (click_pos[1] > self.pos.y - self.size and
                click_pos[1] < self.pos.y + self.size):
                return True

            else:
                return False
        else:
            return False

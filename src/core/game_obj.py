import pygame as pg

class GameObject:
    # settings
    enabled = True
    physics = False
    name = 'unnamed GO'
    tag = 0b0

    # transform / physics
    position = pg.Vector2()
    size = pg.Vector2()
    half_size = pg.Vector2()
    velocity = pg.Vector2()
    acceleration = pg.Vector2()

    # collision detection
    rect = pg.Rect(0, 0, 0, 0,)

    # sprite / visuals
    color = pg.Color('white')
    sprite = None

    # sound
    # FIXME: this could have room for more than one sfx
    sfx_source = None
    bgm_source = None


    def __init__(
            self, 
            position: pg.Vector2, 
            size: pg.Vector2, 
            color: pg.Color = 'white',
            sprite: pg.Surface = None,
            sfx_source: pg.mixer.Sound = None,
            bgm_source: pg.mixer.Sound = None
            ):

        self.position = position
        self.size = size
        self.half_size = pg.Vector2(int(size.x / 2), int(size.y / 2))
        self.color = color
        self.sprite = sprite
        if sfx_source or bgm_source:
            pg.mixer.init()
            self.sfx_source = sfx_source
            self.bgm_source = bgm_source


    def update(self):
        if self.physics:
            self.physics_update()

        self.rect.update(
                self.position.x - self.half_size.x, 
                self.position.y - self.half_size.y, 
                self.size.x, 
                self.size.y
                )

    def physics_update(self):
        #TODO
        pass


    def draw(self, screen): 
        if not self.sprite:
            pg.draw.rect(screen, self.color, self.rect)
        else:
            pg.Surface.blit(screen, self.sprite, self.rect)
 

    def detect_click(self, click_pos : pg.Vector2) -> bool:
        if (click_pos[0] > self.position.x - self.rect.w and
            click_pos[0] < self.position.x + self.rect.w):
            
            if (click_pos[1] > self.position.y - self.rect.h and
                click_pos[1] < self.position.y + self.rect.h):
                return True
            else:
                return False
        else:
            return False

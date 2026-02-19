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
    sprites = None

    # sound
    sfx_sources = None
    bgm_sources = None


    def __init__(
            self, 
            position: pg.Vector2, 
            size: pg.Vector2, 
            color: pg.Color = 'white',
            sprites: list() = None,
            sfx_sources: list() = None,
            bgm_sources: list() = None
            ):

        self.position = position
        self.size = size
        self.half_size = pg.Vector2(int(size.x / 2), int(size.y / 2))
        self.color = color

        if sprites:
            self.sprites = sprites
            self.prepare_sprites()

        if sfx_sources or bgm_sources:
            self.sfx_sources = sfx_sources
            self.prepare_sfx()
        if bgm_sources:
            self.bgm_sources = bgm_sources
            self.prepare_bgm()


    def prepare_sprites(self):
        for i in range(len(self.sprites)):
            self.sprites[i] = pg.image.load(self.sprites[i]).convert_alpha()
            self.sprites[i] = pg.transform.scale(self.sprites[i], (self.size.x, self.size.y))

    def prepare_sfx(self):
        if not pg.mixer.get_init():
            pg.mixer.init()

        for i in range(len(self.sfx_sources)):
            self.sfx_sources[i] = pg.mixer.Sound(self.sfx_sources[i])

    def prepare_bgm(self):
        if not pg.mixer.get_init():
            pg.mixer.init()

        for i in range(len(self.bgm_sources)):
            self.bgm_sources[i] = pg.mixer.Sound(self.bgm_sources[i])
    

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


    #TODO: verify compositing performance
    def draw(self, screen): 
        if not self.sprites:
            pg.draw.rect(screen, self.color, self.rect)
        else:
            for i in range(len(self.sprites)):
                pg.Surface.blit(screen, self.sprites[i], self.rect)
 

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

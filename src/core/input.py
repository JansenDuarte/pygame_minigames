import pygame

#FIXME:
#looping through the events is not ok
class Input:

    @staticmethod
    def get_key(k: int) -> bool:
        if pygame.key.get_pressed()[k]:
            return True
        
        return False

    @staticmethod
    def get_key_down(k: int) -> bool:
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == k:
                    return True

        return False
    

    @staticmethod
    def get_key_up(k: int) -> bool:
        for e in pygame.event.get():
            if e.type == pygame.KEYUP:
                if e.key == k:
                    return True

        return False

    @staticmethod
    def get_button(b: int) -> bool:
        if pygame.mouse.get_pressed(num_buttons=3)[b]:
            return True

        return False

    @staticmethod
    def get_button_down(b: int) -> bool:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                # indexing is weird
                if e.button == b - 1:
                    return True

        return False


    @staticmethod
    def get_button_up(b: int) -> bool:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONUP:
                # indexing is weird
                if e.button == b - 1:
                    return True

        return False

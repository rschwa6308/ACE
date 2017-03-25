from Loads import *
from Colors import *


#ENTITIES

class Player():
    def __init__(self, x_grid, y_grid):
        self.xvel = 0
        self.yvel = 0
        
        self.x = x_grid*64
        self.y = y_grid*64

        self.image = playerR_texture

        self.flipped = False

        self.climbing = False

        self.door = False

        self.key = False
        
    def get_rect(self):
        return pygame.Rect(self.x, self.y, 64, 64)

    def get_grid(self):
        return (int((self.x+32)/64),int((self.y+32)/64))

    def get_image(self):
        if not self.climbing:  #'if not self.climbing' prevents overriding of climb texture
            if self.key:  
                if self.flipped:
                    self.image = playerLK_texture
                else:
                    self.image = playerRK_texture
            else:  
                if self.flipped:
                    self.image = playerL_texture
                else:
                    self.image = playerR_texture
        else:
            if self.key:
                if self.get_grid()[1] % 2 == 0:
                    self.image = climb2K_texture
                else:
                    self.image = climbK_texture
            else:
                if self.climbing:
                    if self.get_grid()[1] % 2 == 0:
                        self.image = climb2_texture
                    else:
                        self.image = climb_texture
                    
        return self.image




class Key():
    def __init__(self, x_grid, y_grid):
        self.x = x_grid*64
        self.y = y_grid*64
        
        self.rect = pygame.Rect(self.x, self.y, 64, 64)

        self.image = key_texture

    def get_image(self):
        return self.image



class Robot():
    def __init__(self, x_grid, y_grid, direction):
        self.x = x_grid*64
        self.y = y_grid*64

        self.direction = direction  #"L" or "R"

        self.threatened = False
        
        self.rect = pygame.Rect(self.x, self.y, 64, 64)

        self.image = self.get_image()

    def get_image(self):
        if self.direction == "L":
            return robotL_texture
        else:
            return robotR_texture



#ANIMATED ROOM OBJECTS

class Door():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 64, 64)

        self.step = 0

        self.key = False

        self.image = self.get_image()


    def get_image(self):
        img = pygame.Surface((64,64))
        img.fill(background_color)
        img.blit(door_outer_texture,(0,0))
        img.blit(door_inner_texture,(0,self.step))
        if self.key:
            img.blit(key_texture,(0,self.step))
        return img





#STATIC ROOM OBJECTS

class Platform():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 64, 64)
        
        self.image = brick_texture
        



class Ladder():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 64, 64)

        self.image = ladder_texture


    

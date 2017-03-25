import pygame
import os




containing = os.path.split(os.path.abspath(__file__))[0]
assets = os.path.join(containing,"assets")



#static room textures
brick_texture = pygame.image.load(os.path.join(assets, "green_brick_64.png"))
ladder_texture = pygame.image.load(os.path.join(assets, "brown_ladder2_64.png"))
sky_texture = pygame.image.load(os.path.join(assets, "sky.png"))

#door textures
door_texture = pygame.image.load(os.path.join(assets, "entire_door_64.png"))
door_outer_texture = pygame.image.load(os.path.join(assets, "green_outsidedoor_64.png"))
door_inner_texture = pygame.image.load(os.path.join(assets, "green_insidedoor_64.png"))


#entity textures
key_texture = pygame.image.load(os.path.join(assets, "green_key_64.png"))

robotL_texture = pygame.image.load(os.path.join(assets, "green_robotL_64.png"))
robotR_texture = pygame.image.load(os.path.join(assets, "green_robotR_64.png"))


#player walk textures
playerR_texture = pygame.image.load(os.path.join(assets, "green_playerR_64.png"))
playerL_texture = pygame.image.load(os.path.join(assets, "green_playerL_64.png"))
playerRK_texture = pygame.image.load(os.path.join(assets, "green_playerRK_64.png"))
playerLK_texture = pygame.image.load(os.path.join(assets, "green_playerLK_64.png"))

#player climb textures
climb_texture = pygame.image.load(os.path.join(assets, "green_climb_64.png"))
climb2_texture = pygame.image.load(os.path.join(assets, "green_climb2_64.png"))
climbK_texture = pygame.image.load(os.path.join(assets, "green_climbK_64.png"))
climb2K_texture = pygame.image.load(os.path.join(assets, "green_climb2K_64.png"))


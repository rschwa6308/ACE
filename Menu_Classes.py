import pygame
from pygame import gfxdraw

from Colors import *
from Fonts import *





class Button():
    def __init__(self, x, y, width, height, color, txt_color, font, text, key):
        self.hover = 0
        self.bg = (255,255,255)
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x,y,width,height)

        self.color = color
        
        self.txt_color = txt_color
        self.font = font
        self.text = text
        
        self.key = key

    def get_image(self):
        img = pygame.Surface((self.width, self.height))
        img.fill((self.bg[0]-50*self.hover,self.bg[1]-50*self.hover,self.bg[2]-50*self.hover))
        bwidth = 2
        buff = bwidth - 1
        pygame.draw.rect(img, self.color, pygame.Rect(buff, buff, self.width-2*buff, self.height-2*buff), bwidth)
        
        text_img = self.font.render(self.text,1,self.txt_color)
        img.blit(text_img,(self.width/2-text_img.get_width()/2,self.height/2-text_img.get_height()/2))  #auto center text
        return img




class Slider():
    def __init__(self, start, length, x, color, bg_color):
        self.start = start
        self.length = length
        self.end = (start[0]+length,start[1])
        self.x = x
        self.color = color
        self.bg_color = bg_color

    def get_rect(self):
        return pygame.Rect(self.x-5 + self.start[0], self.start[1], 10, 40)
        
    def get_image(self):
        #print self.start
        #print self.end
        image = pygame.Surface((self.length+10,40))
        image.fill(self.bg_color)
        #draw line
        pygame.draw.line(image, self.color, (5,20), (self.length,20), 4)
        #draw rect(s)
        pygame.draw.rect(image, self.color, pygame.Rect(self.x-5, 0, 10, 40))
        return image

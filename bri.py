import pygame
import random


WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
class Brick:
    def __init__(self, posx, posy, width, height, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height

        self.color = color
        w = 20
        h = 200
        brick_count = 10
        offset_x = 800 // 2
        offset_y = 160
        bricks = []
        for row in range(1):
            for col in range(1):
                effect = None
                brick_color = (255, 0, 0)
                index = random.randint(0, 1)         

                self.brRect=pygame.Rect(posx, posy, width, height)
                self.brick=pygame.draw.rect(screen, self.color, self.brRect)  

    def display(self):
        self.brick = pygame.draw.rect(screen, self.color, self.brRect)   
    
    def getRect(self):
        return self.brRect
from bomberman import *

class Enemy(Bomberman):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load('grafika/robot_pink.png').convert_alpha()
import pygame

class Block:
    def __init__(self, pos):
        self.pos = pos
        self.width = 40
        self.height = 40
        self.block_rect = pygame.Rect(int(self.pos.x * self.width), int(self.pos.y * self.height), self.width, self.height)
        self.image = pygame.image.load('grafika/box.png').convert_alpha()

    def renderBlock(self, screen):
        self.block_rect = pygame.Rect(int(self.pos.x * self.width), int(self.pos.y * self.height), self.width, self.height)
        #pygame.draw.rect(screen, "grey", self.block_rect)
        screen.blit(self.image, self.block_rect)
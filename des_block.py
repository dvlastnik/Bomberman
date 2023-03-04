from block import *

class des_Block(Block):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load('grafika/des_block.jpg').convert_alpha()

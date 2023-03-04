import pygame

class Bomb:
    def __init__(self, pos):
        self.width = 40
        self.height = 40
        self.pos = pos
        self.start = pygame.time.get_ticks()
        self.image = pygame.image.load('grafika/bomb2.png').convert_alpha()
        self.explosion_image = pygame.image.load('grafika/explosion.png').convert_alpha()
        self.bomb_rect = pygame.Rect(int(self.pos.x * 40), int(self.pos.y * 40), self.width, self.height)

        self.exp_rects = (pygame.Rect(int(self.pos.x * 40), int(self.pos.y * 40), self.width, self.height),
                          pygame.Rect(int(self.pos.x * 40 - 40), int(self.pos.y * 40), self.width, self.height),
                          pygame.Rect(int(self.pos.x * 40 + 40), int(self.pos.y * 40), self.width, self.height),
                          pygame.Rect(int(self.pos.x * 40), int(self.pos.y * 40 + 40), self.width, self.height),
                          pygame.Rect(int(self.pos.x * 40), int(self.pos.y * 40 - 40), self.width, self.height))

    def renderBomb(self, screen):
        screen.blit(self.image, self.bomb_rect)

    def explode(self, screen):
        pygame.draw.rect(screen, (163, 226, 101), (int(self.pos.x * 40), int(self.pos.y * 40), self.width, self.height))
        for rect in self.exp_rects:
            screen.blit(self.explosion_image, rect)



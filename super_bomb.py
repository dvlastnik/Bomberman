from bomb import *

class super_Bomb(Bomb):
    def __init__(self, pos):
        super().__init__(pos)
        self.image = pygame.image.load('grafika/bomb3.png').convert_alpha()
        self.exp_rects = []
        self.isTaken = False
        for i in range(1, 20):
            for j in range(1, 20):
                self.exp_rects.append(pygame.Rect(int(i * 40), int(j * 40), self.width, self.height))

    def explode(self, screen):
        pygame.draw.rect(screen, (163, 226, 101), (int(self.pos.x * 40), int(self.pos.y * 40), self.width, self.height))
        for rect in self.exp_rects:
            screen.blit(self.explosion_image, rect)


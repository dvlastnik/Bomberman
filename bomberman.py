import sys

import pygame
from bomb import *
from pygame.math import Vector2




class Bomberman:
    def __init__(self, pos):
        self.life = True
        self.pos = pos
        self.bmb_rect = pygame.Rect(int(self.pos.x * 40), int(self.pos.y * 40), 25, 25)
        self.bomb = None
        self.superBomb = None
        self.haveSuperBomb = False
        self.isDropped = False
        self.image = pygame.image.load('grafika/robot_yellow.png').convert_alpha()

    def drawBomberman(self, screen):
        self.bmb_rect = pygame.Rect(int(self.pos.x * 40), int(self.pos.y * 40), 30, 30)
        screen.blit(self.image, self.bmb_rect)

    def dropBomb(self, screen, list, player):
        if self.haveSuperBomb is False:
            if self.isDropped:
                    self.bomb.renderBomb(screen)
                    seconds = (pygame.time.get_ticks() - self.bomb.start) / 1000
                    if seconds >= 3:
                        self.bomb.explode(screen)
                        self.collisionWithBomb(list, player)
                    if seconds >= 4:
                        seconds = 0
                        self.isDropped = False
                        self.bomb = None
        else:
            if self.superBomb != None:
                self.superBomb.renderBomb(screen)
                seconds = (pygame.time.get_ticks() - self.superBomb.start) / 1000
                if seconds >= 3:
                    self.superBomb.explode(screen)
                    self.collisionWithBomb(list, player)
                if seconds >= 4:
                    seconds = 0
                    self.isDropped = False
    def fromStart (self, pos):
        self.life = True
        self.pos = pos
        self.bmb_rect = pygame.Rect(int(self.pos.x * 40), int(self.pos.y * 40), 25, 25)
        self.bomb = None
        self.superBomb = None
        self.haveSuperBomb = False
        self.isDropped = False

    def collisionWithBomb(self, list, player):
            if self.superBomb != None:
                for rect in self.superBomb.exp_rects:
                    if self.bmb_rect.colliderect(rect):
                        player.life = False
                    for i in list:
                        if i.block_rect.colliderect(rect):
                            list.remove(i)

            elif self.bomb != None:
                for rect in self.bomb.exp_rects:
                    if self.bmb_rect.colliderect(rect):
                        self.life = False
                    for i in list:
                        if i.block_rect.colliderect(rect):
                            list.remove(i)

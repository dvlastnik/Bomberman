import random
import pygame
import sys
from pygame.math import Vector2
from bomberman import *
from bomb import *
from des_block import *
from enemy import *
from super_bomb import *
from button import *

pygame.init()

def generatingBlocks():
    for i in range(150):
        x = random.randint(1, cell_number - 2)
        y = random.randint(1, cell_number - 2)
        list_of_coords.append(Vector2(x, y))

    for i in range(0, cell_number):
        for j in range(0, cell_number):
            if i == 0 or i == cell_number - 1 or j == 0 or j == cell_number - 1 or ((i % 2 == 0) and (j % 2 == 0)):
                list_of_blocks.append(Block(Vector2(i, j)))
                for k in list_of_coords:
                    if k == Vector2(i, j) or k == Vector2(1, 1) or k == Vector2(2, 1) or k == Vector2(3,
                                                                                                      1) or k == Vector2(
                            1, 2) \
                            or k == Vector2(1, 3) or k == Vector2(19, 19) or k == Vector2(19, 18) or k == Vector2(19,
                                                                                                                  17) or k == Vector2(
                        18, 19) \
                            or k == Vector2(17, 19):
                        list_of_coords.remove(k)

    for i in list_of_coords:
        list_of_desBlocks.append(des_Block(i))


def controls(keys, player):
    if type(player) is enemy.__class__:
        if keys[pygame.K_w]:
            if player.pos.y > 1:
                player.pos.y -= vel
        elif keys[pygame.K_s]:
            if player.pos.y < cell_number - 2:
                player.pos.y += vel
        elif keys[pygame.K_d]:
            if player.pos.x < cell_number - 2:
                player.pos.x += vel
        elif keys[pygame.K_a]:
            if player.pos.x > 1:
                player.pos.x -= vel
        if keys[pygame.K_LSHIFT]:
            if player.haveSuperBomb:
                player.superBomb = super_Bomb(Vector2(player.pos.x, player.pos.y))
            else:
                if player.isDropped is False:
                    player.isDropped = True
                    player.bomb = Bomb(Vector2(player.pos.x, player.pos.y))

    else:
        if keys[pygame.K_UP]:
            if player.pos.y > 1:
                player.pos.y -= vel
        elif keys[pygame.K_DOWN]:
            if player.pos.y < cell_number - 2:
                player.pos.y += vel
        elif keys[pygame.K_RIGHT]:
            if player.pos.x < cell_number - 2:
                player.pos.x += vel
        elif keys[pygame.K_LEFT]:
            if player.pos.x > 1:
                player.pos.x -= vel
        if keys[pygame.K_SPACE]:
            if player.haveSuperBomb:
                player.superBomb = super_Bomb(Vector2(player.pos.x, player.pos.y))
            else:
                if player.isDropped is False:
                    player.isDropped = True
                    player.bomb = Bomb(Vector2(player.pos.x, player.pos.y))


def checkCollisionWithBomb(player, enemy):
    if player.bomb != None:
        if player.bmb_rect.colliderect(player.bomb.bomb_rect):
            if abs(player.bmb_rect.right - player.bomb.bomb_rect.left) <= 5:
                player.pos.x -= vel
            elif abs(player.bmb_rect.left - player.bomb.bomb_rect.right) <= 5:
                player.pos.x += vel
            elif abs(player.bmb_rect.top - player.bomb.bomb_rect.bottom) <= 5:
                player.pos.y += vel
            elif abs(player.bmb_rect.bottom - player.bomb.bomb_rect.top) <= 5:
                player.pos.y -= vel

    if enemy.bomb != None:
        if player.bmb_rect.colliderect(enemy.bomb.bomb_rect):
            if abs(player.bmb_rect.right - enemy.bomb.bomb_rect.left) <= 5:
                player.pos.x -= vel
            elif abs(player.bmb_rect.left - enemy.bomb.bomb_rect.right) <= 5:
                player.pos.x += vel
            elif abs(player.bmb_rect.top - enemy.bomb.bomb_rect.bottom) <= 5:
                player.pos.y += vel
            elif abs(player.bmb_rect.bottom - enemy.bomb.bomb_rect.top) <= 5:
                player.pos.y -= vel


def checkCollision(list, player):
    for block in list:
        if player.bmb_rect.colliderect(block.block_rect):
            if abs(player.bmb_rect.right - block.block_rect.left) <= 5:
                player.pos.x -= vel
            elif abs(player.bmb_rect.left - block.block_rect.right) <= 5:
                player.pos.x += vel
            elif abs(player.bmb_rect.top - block.block_rect.bottom) <= 5:
                player.pos.y += vel
            elif abs(player.bmb_rect.bottom - block.block_rect.top) <= 5:
                player.pos.y -= vel


def checkCollisionOfBlocks():
    checkCollision(list_of_blocks, bomberman)
    checkCollision(list_of_desBlocks, bomberman)
    checkCollision(list_of_blocks, enemy)
    checkCollision(list_of_desBlocks, enemy)


def drawWindow():
    screen.fill((163, 226, 101))
    if bomberman.bmb_rect.colliderect(s_bomb.bomb_rect):
        s_bomb.isTaken = True
        bomberman.haveSuperBomb = True
    elif enemy.bmb_rect.colliderect(s_bomb.bomb_rect):
        s_bomb.isTaken = True
        enemy.haveSuperBomb = True
    else:
        if s_bomb.isTaken is False:
            s_bomb.renderBomb(screen)
    for block in list_of_blocks:
        block.renderBlock(screen)
    for block in list_of_desBlocks:
        block.renderBlock(screen)
    bomberman.dropBomb(screen, list_of_desBlocks, enemy)
    bomberman.drawBomberman(screen)
    enemy.dropBomb(screen, list_of_desBlocks, bomberman)
    enemy.drawBomberman(screen)
    pygame.display.update()

def firstWindow():
    del list_of_blocks[:]
    del list_of_desBlocks[:]
    del list_of_coords[:]
    generatingBlocks()

def play():
    firstWindow()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if bomberman.life is False:
            run = False
        if enemy.life is False:
            run = False
        keys = pygame.key.get_pressed()
        controls(keys, bomberman)
        controls(keys, enemy)
        checkCollisionOfBlocks()
        checkCollisionWithBomb(bomberman, enemy)
        checkCollisionWithBomb(enemy, bomberman)
        drawWindow()
        FPS.tick(60)
    menu ()

def get_font(size):
    return pygame.font.Font("grafika/font.ttf", size)


def menu():
    screen.fill((163, 226, 101))
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if start_button.draw(screen):
            play()
        if exit_button.draw(screen):
            break
        if bomberman.life is False:
            print ("Ruzovy vyhral")
            PLAY_TEXT = get_font(30).render("RUZOVY VYHRAL", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 100))
            screen.blit(PLAY_TEXT, PLAY_RECT)
            bomberman.fromStart(Vector2(1,1))
        elif enemy.life is False:
            print ("Zeleny vyhral")
            PLAY_TEXT = get_font(30).render("ZELENY VYHRAL", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(400,100))
            screen.blit(PLAY_TEXT, PLAY_RECT)
            bomberman.fromStart(Vector2(1,1))
            enemy.fromStart(Vector2(cell_number - 2, cell_number - 2))
        pygame.display.update()


# how big is one cell in grid
cell_size = 40
# number of cells in grid
cell_number = 21

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
FPS = pygame.time.Clock()

bomberman = Bomberman(Vector2(1, 1))
enemy = Enemy(Vector2(cell_number - 2, cell_number - 2))
vel = 0.05

list_of_blocks = list()
list_of_desBlocks = list()
list_of_coords = list()
generatingBlocks()
s_bomb = super_Bomb(Vector2(random.choice(list_of_coords)))

isTaken = False
start_img = pygame.image.load('grafika/start_btn.png').convert_alpha()
exit_img = pygame.image.load('grafika/exit_btn.png').convert_alpha()
start_button = Button(150, 400, start_img, 0.8)
exit_button = Button(450, 400, exit_img, 0.8)
menu()

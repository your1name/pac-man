import pygame, sys, math
import math
from pygame.locals import *
from random import randrange


# 0 = empty black rectangle, 1 = dot, 2 = big dot, 3 = vertical line,
# 4 = horizontal line, 5 = top right, 6 = top left, 7 = bot left, 8 = bot right
# 9 = gate
# 36 hàng x 30 cột
board = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
[3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
[4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
[5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
[3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
[3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
[3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
[7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
         ]


TextPath = "Assetsi/TextImages/"
BoardPath = "Assetsi/BoardImages/"

PI = math.pi
WIDTH = 700
HEIGHT = 874
# 700 // 30 = 23
#805 - 23*2 - 23 // 32 = 23
PIXEL = 23
PINK = (199, 177, 149)
player_images = []
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (23, 23)))


counter  = 0
flicker = False
level = board
spriteRatio = 3/2


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

class Game:
    def __init__(self,score) :

        self.pacman = Pacman(27,15) 
        self.ghosts = [Ghost(18,12,'blue'), Ghost(18,14,'red'), Ghost(18,15,'pink'), Ghost(18,17,"orange") ]
        self.score = score
        self.lives  = 3
        self.paused = True
        self.started = False
        
    
    
    def draw_live(self):
    #pygame.draw.rect(screen,(255,255,255),(30 , 835, 23, 23),1)
        for i in range(self.lives):
            screen.blit(pygame.transform.scale(player_images[0], (25, 25)), (30 + i * 40, 830))
    
    def drawReady(self):
        ready = ["tile274.png", "tile260.png", "tile256.png", "tile259.png", "tile281.png", "tile283.png"]
        for i in range(len(ready)):
            letter = pygame.image.load(TextPath + ready[i])
            letter = pygame.transform.scale(letter, (int(23), int(23)))
            screen.blit(letter, ((11 + i) * 23, 20 * 23, 23, 23))
    
    
    def update(self):
        
        

        self.pacman.update() #pac-man di chuyển
        
        # pac-man chui hầm
        if self.pacman.col >= 29:
            self.pacman.col = 0
        
        if self.pacman.col < 0:
            self.pacman.col = len(level[0]) - 1


        for ghost in self.ghosts: # logic score
            if self.pacman.row % 1.0 == 0 and self.pacman.col % 1.0 == 0:
                if level[int(self.pacman.row)][int(self.pacman.col)] == 1:
                    level[int(self.pacman.row)][int(self.pacman.col)] = 0
                    self.score += 10

            if level[int(self.pacman.row)][int(self.pacman.col)] == 2:
                level[int(self.pacman.row)][int(self.pacman.col)] = 0
                self.score += 50
                for ghost in self.ghosts:
                        ghost.setAttacked(True)     # spooked

    
    def displayScore(self):
        textOneUp = [ "tile019.png", "tile002.png", "tile014.png", "tile018.png", "tile004.png"]
        # textHighScore = ["tile007.png", "tile008.png", "tile006.png", "tile007.png", "tile015.png", "tile019.png", "tile002.png", "tile014.png", "tile018.png", "tile004.png"]
        index = 0
        scoreStart = 11
        # highScoreStart = 11
        for i in range(scoreStart, scoreStart+len(textOneUp)):
            tileImage = pygame.image.load(TextPath + textOneUp[index])
            tileImage = pygame.transform.scale(tileImage, (20, 20))
            screen.blit(tileImage, (i * 20, 39, 23, 23))
            index += 1
        # print(board[int(self.col)][int(self.row)])
      
        score = str(self.score)
        if score == "0":
            score = "00"
        index = 0
        for i in range(0, len(score)):
            digit = int(score[i])
            tileImage = pygame.image.load(TextPath + "tile0" + str(32 + digit) + ".png")
            tileImage = pygame.transform.scale(tileImage, (20, 20))
            screen.blit(tileImage, ((scoreStart + 2 + index) * 27, 39, 23, 23))
            index += 1
    
    
    
    
    def render(self):
        if self.paused or not self.started:
            self.drawReady()
            game.paused = False
            
           
        self.displayScore()
        
        self.draw_live()
        self.pacman.draw()
        
        for ghost in self.ghosts:
             ghost.draw()

        pygame.display.update()
        
    
    def touchingPacman(self, row, col):
        if row - 0.5 <= self.pacman.row and row >= self.pacman.row and col == self.pacman.col: # cùng cột, nằm dưới , -0.5 thì đi qua pacman
            return True
        elif row + 0.5 >= self.pacman.row and row <= self.pacman.row and col == self.pacman.col:
            return True
        elif row == self.pacman.row and col - 0.5 <= self.pacman.col and col >= self.pacman.col:
            return True
        elif row == self.pacman.row and col + 0.5 >= self.pacman.col and col <= self.pacman.col:
            return True
        elif row == self.pacman.row and col == self.pacman.col:
            return True
        return False


class Pacman:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.pacSpeed = 1/16
        self.dir = 0 # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        self.newDir = 0        

    def draw(self): 
    # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        if self.dir == 0:
            screen.blit(player_images[counter // 8], (self.col*23, self.row*23))
        elif self.dir == 1:
            screen.blit(pygame.transform.flip(player_images[counter // 8], True, False), (self.col*23, self.row*23))
        elif self.dir == 2:
            screen.blit(pygame.transform.rotate(player_images[counter // 8], 90), (self.col*23, self.row*23))
        elif self.dir == 3:
            screen.blit(pygame.transform.rotate(player_images[counter // 8], 270), (self.col*23, self.row*23))     
   
    def update(self):
        if self.newDir == 2:
            if canMove(math.floor(self.row - self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row -= self.pacSpeed
                self.dir = self.newDir
                return
        elif self.newDir == 0:
            if canMove(self.row, math.ceil(self.col + self.pacSpeed)) and self.row % 1.0 == 0:
                self.col += self.pacSpeed
                self.dir = self.newDir
                return
        elif self.newDir == 3:
            if canMove(math.ceil(self.row + self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row += self.pacSpeed
                self.dir = self.newDir
                return
        elif self.newDir == 1:
            if canMove(self.row, math.floor(self.col - self.pacSpeed)) and self.row % 1.0 == 0:
                self.col -= self.pacSpeed
                self.dir = self.newDir
                return

        if self.dir == 2:
            if canMove(math.floor(self.row - self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row -= self.pacSpeed
        elif self.dir == 0:
            if canMove(self.row, math.ceil(self.col + self.pacSpeed)) and self.row % 1.0 == 0:
                self.col += self.pacSpeed
        elif self.dir == 3:
            if canMove(math.ceil(self.row + self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row += self.pacSpeed
        elif self.dir == 1:
            if canMove(self.row, math.floor(self.col - self.pacSpeed)) and self.row % 1.0 == 0:
                self.col -= self.pacSpeed
        
       
class Ghost:
    def __init__(self, row, col, color) :
        self.row = row
        self.col = col
        self.color = color

        self.attacked = False
        # thời gian power
        self.dir = randrange(4)
        self.dead = False
        self.deathTimer = 120
        self.ghostSpeed = 1/4
        
        self.target = [-1, -1]
        
        self.attackedTimer = 240
        self.attackedCount = 0
        

    def draw(self):
        ghostImage = pygame.image.load(f'assets/ghost_images/dead.png')
        if self.dead:
            ghostImage = pygame.image.load(f'assets/ghost_images/dead.png')
        elif self.attacked:
            ghostImage = pygame.image.load(f'assets/ghost_images/powerup.png') # spooked
        else:
            if self.color == "blue":
                ghostImage = pygame.image.load(f'assets/ghost_images/blue.png')
            elif self.color == "pink":
                ghostImage = pygame.image.load(f'assets/ghost_images/pink.png')
            elif self.color == "orange":
                ghostImage = pygame.image.load(f'assets/ghost_images/orange.png')
            elif self.color == "red":
                ghostImage = pygame.image.load(f'assets/ghost_images/red.png')
        
        ghostImage = pygame.transform.scale(ghostImage, (30,30))
        screen.blit(ghostImage, (self.col *23, self.row * 23))
    
    def update(self):
        pass

    def setAttacked(self, isAttacked):
        self.attacked = isAttacked

    def isAttacked(self):
        return self.attacked

    def setDead(self, isDead):
        self.dead = isDead

    def isDead(self):
        return self.dead

    def move(self):
        # print(self.target)
        # //self.lastLoc = [self.row, self.col]
        if self.dir == 3:
            self.row -= self.ghostSpeed
        elif self.dir == 0:
            self.col += self.ghostSpeed
        elif self.dir == 2:
            self.row += self.ghostSpeed
        elif self.dir == 1:
            self.col -= self.ghostSpeed

        # Incase they go through the middle tunnel
        if self.col < 0:
            self.col = len(level[0]) - 1

    
    
    def calcDistance(self, a, b):
        dR = a[0] - b[0]
        dC = a[1] - b[1]
        return math.sqrt((dR * dR) + (dC * dC))

    
# ================= end class ====================

def draw_board():

    for i in range(len(level)):
        for j in range(len(level[i])):
            #pygame.draw.rect(screen,(255,255,255),(j*PIXEL, i * PIXEL, 23, 23),1)

            if level[i][j] == 1: # tik-tak
                pygame.draw.circle(screen, (230, 200, 158), (j * PIXEL + (0.5 * PIXEL), i * PIXEL + (0.5 * PIXEL)), 4)

            if level[i][j] == 2 and not flicker : # special tik-tak
                pygame.draw.circle(screen, (230, 200, 158), (j * PIXEL + (0.5 * PIXEL), i * PIXEL + (0.5 * PIXEL)), 10)

            if level[i][j] == 3:  # line Y
                pygame.draw.line(screen, 'blue', (j * PIXEL + (0.5 * PIXEL), i * PIXEL),(j * PIXEL + (0.5 * PIXEL), i * PIXEL + PIXEL), 3) # line từ A (x,y) tới B (x,y)
                
            if level[i][j] == 4:  # line X
                pygame.draw.line(screen, 'blue', (j * PIXEL, i * PIXEL + (0.5 * PIXEL)),(j * PIXEL + PIXEL, i * PIXEL + (0.5 * PIXEL)), 3)  # line từ A (x,y) tới B (x,y)

            if level[i][j] == 5: # góc phần tư thứ 1 của Unit circle
                pygame.draw.arc(screen, 'blue', [(j * PIXEL - (PIXEL * 0.4)) - 2, (i * PIXEL + (0.5 * PIXEL)), PIXEL, PIXEL], 0, PI / 2, 3)

            if level[i][j] == 6: # góc phần tư thứ 2 của Unit circle
                pygame.draw.arc(screen, 'blue',[(j * PIXEL + (PIXEL * 0.5)), (i * PIXEL + (0.5 * PIXEL)), PIXEL, PIXEL], PI / 2, PI, 3)

            if level[i][j] == 7: # góc phần tư thứ 3 của Unit circle
                pygame.draw.arc(screen, 'blue', [(j * PIXEL + (PIXEL * 0.5)), (i * PIXEL - (0.4 * PIXEL)), PIXEL, PIXEL], PI,3 * PI / 2, 3,)

            if level[i][j] == 8: # góc phần tư thứ 4 của Unit circle
                pygame.draw.arc(screen, 'blue',[(j * PIXEL - (PIXEL * 0.4)) - 2, (i * PIXEL - (0.4 * PIXEL)), PIXEL, PIXEL], 3 * PI / 2,2 * PI, 3)

            if level[i][j] == 9: # cổng ma 
                pygame.draw.line(screen, 'white', (j * PIXEL, i * PIXEL + (0.5 * PIXEL)),(j * PIXEL + PIXEL, i * PIXEL + (0.5 * PIXEL)), 3)
     
def canMove(row, col):
    if col <= -1 or col == len(level[0]):
        return True
    if level[int(row)][int(col)] < 3:
        return True
    return False

def displayLaunchScreen():
    # Draw Pacman Title
    pacmanTitle = ["tile016.png", "tile000.png", "tile448.png", "tile012.png", "tile000.png", "tile013.png"]
    for i in range(len(pacmanTitle)):
        letter = pygame.image.load(TextPath + pacmanTitle[i])
        letter = pygame.transform.scale(letter, (int(23 * 4), int(23 * 4)))
        screen.blit(letter, ((2 + 4 * i) * 23, 2 * 23, 23, 23))

    # Draw Character / Nickname
    characterTitle = [
        #Character
        "tile002.png", "tile007.png", "tile000.png", "tile018.png", "tile000.png", "tile002.png", "tile020.png", "tile004.png", "tile018.png",
        # /
        "tile015.png", "tile042.png", "tile015.png",
        # Nickname
        "tile013.png", "tile008.png", "tile002.png", "tile010.png", "tile013.png", "tile000.png", "tile012.png", "tile004.png"
    ]
    for i in range(len(characterTitle)):
        letter = pygame.image.load(TextPath + characterTitle[i])
        letter = pygame.transform.scale(letter, (int(23), int(23)))
        screen.blit(letter, ((4 + i) * 23, 10 * 23, 23, 23))

    #Draw Characters and their Nickname
    characters = [
        # Red Ghost
        [
            "tile449.png", "tile015.png", "tile107.png", "tile015.png", "tile083.png", "tile071.png", "tile064.png", "tile067.png", "tile078.png", "tile087.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile108.png", "tile065.png", "tile075.png", "tile072.png", "tile077.png", "tile074.png", "tile089.png", "tile108.png"
        ],
        # Pink Ghost
        [
            "tile450.png", "tile015.png", "tile363.png", "tile015.png", "tile339.png", "tile336.png", "tile324.png", "tile324.png", "tile323.png", "tile345.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile364.png", "tile336.png", "tile328.png", "tile333.png", "tile330.png", "tile345.png", "tile364.png"
        ],
        # Blue Ghost
        [
            "tile452.png", "tile015.png", "tile363.png", "tile015.png", "tile193.png", "tile192.png", "tile211.png", "tile199.png", "tile197.png", "tile213.png", "tile203.png",
            "tile015.png", "tile015.png", "tile015.png",
            "tile236.png", "tile200.png", "tile205.png", "tile202.png", "tile217.png", "tile236.png"
        ],
        # Orange Ghost
        [
            "tile451.png", "tile015.png", "tile363.png", "tile015.png", "tile272.png", "tile270.png", "tile266.png", "tile260.png", "tile281.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile300.png", "tile258.png", "tile267.png", "tile281.png", "tile259.png", "tile260.png", "tile300.png"
        ]
    ]
    for i in range(len(characters)):
        for j in range(len(characters[i])):
            if j == 0:
                    letter = pygame.image.load(TextPath + characters[i][j])
                    letter = pygame.transform.scale(letter, (int(23 * spriteRatio), int(23 * spriteRatio)))
                    screen.blit(letter, ((2 + j) * 23 - 23//2, (12 + 2 * i) * 23 - 23//3, 23, 23))
            else:
                letter = pygame.image.load(TextPath + characters[i][j])
                letter = pygame.transform.scale(letter, (int(23), int(23)))
                screen.blit(letter, ((2 + j) * 23, (12 + 2 * i) * 23, 23, 23))
    # Draw Pacman and Ghosts
    event = ["tile449.png", "tile015.png", "tile452.png", "tile015.png",  "tile015.png", "tile448.png", "tile453.png", "tile015.png", "tile015.png", "tile015.png",  "tile453.png"]
    for i in range(len(event)):
        character = pygame.image.load(TextPath + event[i])
        character = pygame.transform.scale(character, (int(23 * 2), int(23 * 2)))
        screen.blit(character, ((4 + i * 2) * 23, 24 * 23, 23, 23))
    # Draw PlatForm from Pacman and Ghosts
    wall = ["tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png"]
    for i in range(len(wall)):
        platform = pygame.image.load(TextPath + wall[i])
        platform = pygame.transform.scale(platform, (int(23 * 2), int(23 * 2)))
        screen.blit(platform, ((i * 2) * 23, 26 * 23, 23, 23))

    # Press Space to Play
    instructions = ["tile016.png", "tile018.png", "tile004.png", "tile019.png", "tile019.png", "tile015.png", "tile019.png", "tile016.png", "tile000.png", "tile002.png", "tile004.png", "tile015.png", "tile020.png", "tile014.png", "tile015.png", "tile016.png", "tile011.png", "tile000.png", "tile025.png"]
    for i in range(len(instructions)):
        letter = pygame.image.load(TextPath + instructions[i])
        letter = pygame.transform.scale(letter, (int(23), int(23)))
        screen.blit(letter, ((4.5 + i) * 23, 35 * 23 - 10, 23, 23))

    pygame.display.update()


onLaunchScreen = True
displayLaunchScreen()   

game = Game(score= 0)



while True:
    timer.tick(60) # fps cua game
    if counter < 31:
        counter += 1
        if counter > 8:
            flicker = False
    else:
        counter = 0
        flicker = True
        
    screen.fill((0,0,0))
    draw_board()


    print(game.pacman.row, game.pacman.col, f'score: {game.score}')


    # game.render() # draw pac man, ghost, lives
   
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            game.paused = False
            game.started = True
            if event.key == pygame.K_RIGHT:
                if not onLaunchScreen:
                    game.pacman.newDir= 0
            if event.key == pygame.K_LEFT:
                if not onLaunchScreen:
                    game.pacman.newDir= 1
            if event.key == pygame.K_UP:
                if not onLaunchScreen:
                    game.pacman.newDir= 2
            if event.key == pygame.K_DOWN:
                if not onLaunchScreen:
                    game.pacman.newDir= 3
            if event.key == pygame.K_SPACE:
                # game.started = True
                onLaunchScreen = False
                game.paused = True
                
                # if onLaunchScreen:
                #     
                    
    
    if not onLaunchScreen:     
        game.render()    
        game.update() # update  (logic score), (pac-man di chuyển)



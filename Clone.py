import pygame, sys, math, random
import math
from pygame.locals import *
from random import randrange


# 0 = empty black rectangle, 1 = dot, 2 = big dot, 3 = vertical line,
# 4 = horizontal line, 5 = top right, 6 = top left, 7 = bot left, 8 = bot right
# 9 = gate
# 36 hàng x 30 cột
board = [
#
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
[8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
[4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, -1, -1, -1, -1, -1, -1, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, -1, -1, -1, -1, -1, -1, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, -1, -1, -1, -1, -1, -1, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
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



 # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
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


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

class Game:
    def __init__(self,score) :

        self.pacman = Pacman(27,15) 
        self.ghosts = [Ghost(18.0,12.0,'blue'), Ghost(18.0,14.0,'red'), Ghost(18.0,15.0,'pink'), Ghost(18.0,17.0,"orange") ]
        #self.ghosts = [Ghost(27.0,15.0,'blue') ]
        self.score = score
        self.lives  = 2
    
    
    def draw_live(self):
    #pygame.draw.rect(screen,(255,255,255),(30 , 835, 23, 23),1)
        for i in range(self.lives):
            screen.blit(pygame.transform.scale(player_images[0], (25, 25)), (30 + i * 40, 830))
    
    def update(self):
       

        # for ghost in self.ghosts:
        #     if not ghost.attacked and not ghost.dead:
        #         ghost.target = [self.pacman.row, self.pacman.col]

        
        
        if not self.ghosts[0].attacked and not self.ghosts[0].dead:
            self.ghosts[0].target = [self.pacman.row, self.pacman.col]
        
        

        for ghost in self.ghosts:
            ghost.update() 


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
       

    def render(self):

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
        self.ghostSpeed = 1/16

        self.lastLoc = [-1, -1]
        self.target = [-1, -1]

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
        if self.target == [-1, -1] or (self.row == self.target[0] and self.col == self.target[1]) or board[int(self.row)][int(self.col)] == -1 or self.dead:
            self.setTarget()
        self.setDir()
        self.move()

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
        print(f'targen into: {self.target}')

        self.lastLoc = [self.row, self.col]
        if self.dir == 2:
            self.row -= self.ghostSpeed
        elif self.dir == 0:
            self.col += self.ghostSpeed
        elif self.dir == 3:
            self.row += self.ghostSpeed
        elif self.dir == 1:
            self.col -= self.ghostSpeed

        # Incase they go through the middle tunnel
        if self.col < 0:
            self.col = len(level[0]) - 1
        
        if self.col > len(level[0]) - 1:
            self.col = 1

    def calcDistance(self, a, b):
        dR = a[0] - b[0]
        dC = a[1] - b[1]
        return math.sqrt((dR * dR) + (dC * dC))
 
 ########################
    def isValid(self, cRow, cCol):
        if cCol < 0 or cCol > len(board[0]) - 1:
            return True

        for ghost in game.ghosts:
            if ghost.color == self.color:
                continue
            if ghost.row == cRow and ghost.col == cCol and not self.dead:
                return False
        if not ghostGate.count([cRow, cCol]) == 0:
            if self.dead and self.row < cRow:
                return True
            elif self.row > cRow and not self.dead and not self.attacked :
                return True
            else:
                return False
        if board[cRow][cCol] >= 3 :
            return False
        return True
    
    def setTarget(self):
        if board[int(self.row)][int(self.col)] == -1 and not self.dead:
            self.target = [ghostGate[0][0] - 1, ghostGate[0][1]+1] # 15 15
            return
        elif board[int(self.row)][int(self.col)] == -1 and self.dead:
            self.target = [self.row, self.col]
        elif self.dead:
            self.target = [15, 14]
            return

        # Records the quadrants of each ghost's target
        quads = [0, 0, 0, 0]
        for ghost in game.ghosts:
            # if ghost.target[0] == self.row and ghost.col == self.col:
            #     continue
            if ghost.target[0] <= 16 and ghost.target[1] >= 14:
                quads[0] += 1
            elif ghost.target[0] <= 16 and ghost.target[1] < 14:
                quads[1] += 1
            elif ghost.target[0] > 16 and ghost.target[1] < 14:
                quads[2] += 1
            elif ghost.target[0]> 16 and ghost.target[1] >= 14:
                quads[3] += 1

        # ############### Finds a target that will keep the ghosts dispersed 
        
        while True:
            self.target = [randrange(3,36), randrange(30)]
            quad = 0
            if self.target[0] <= 16 and self.target[1] >= 14:
                quad = 0
            elif self.target[0] <= 16 and self.target[1] < 14:
                quad = 1
            elif self.target[0] > 16 and self.target[1] < 14:
                quad = 2
            elif self.target[0] > 16 and self.target[1] >= 14:
                quad = 3
            if not board[self.target[0]][self.target[1]] >= 3 and not board[self.target[0]][self.target[1]] == -1:
                break
            elif quads[quad] == 0:
                break
    
    def setDir(self): #Very inefficient || can easily refactor
        # BFS search -> Not best route but a route none the less
        dirs = [[0, 0, self.ghostSpeed],
                [1, 0, -self.ghostSpeed],
                [2, -self.ghostSpeed, 0],
                [3, self.ghostSpeed, 0]
        ]
        random.shuffle(dirs)
        best = 10000
        bestDir = -1
        for newDir in dirs:
            if self.calcDistance(self.target, [self.row + newDir[1], self.col + newDir[2]]) < best:
                if not (self.lastLoc[0] == self.row + newDir[1] and self.lastLoc[1] == self.col + newDir[2]):
                    if newDir[0] == 2 and self.col % 1.0 == 0:
                        if self.isValid(math.floor(self.row + newDir[1]), int(self.col + newDir[2])):
                            bestDir = newDir[0]
                            best = self.calcDistance(self.target, [self.row + newDir[1], self.col + newDir[2]])
                    elif newDir[0] == 0 and self.row % 1.0 == 0:
                        if self.isValid(int(self.row + newDir[1]), math.ceil(self.col + newDir[2])):
                            bestDir = newDir[0]
                            best = self.calcDistance(self.target, [self.row + newDir[1], self.col + newDir[2]])
                    elif newDir[0] == 3 and self.col % 1.0 == 0:
                        if self.isValid(math.ceil(self.row + newDir[1]), int(self.col + newDir[2])):
                            bestDir = newDir[0]
                            best = self.calcDistance(self.target, [self.row + newDir[1], self.col + newDir[2]])
                    elif newDir[0] == 1 and self.row % 1.0 == 0:
                        if self.isValid(int(self.row + newDir[1]), math.floor(self.col + newDir[2])):
                            bestDir = newDir[0]
                            best = self.calcDistance(self.target, [self.row + newDir[1], self.col + newDir[2]])
        self.dir = bestDir


    
# ================= end class ====================

def draw_board():

    for i in range(len(level)):
        for j in range(len(level[i])):
            pygame.draw.rect(screen,(255,255,255),(19*PIXEL, 21 * PIXEL, 23, 23),1)
            pygame.draw.rect(screen,(255,0,0),(18*PIXEL, 24 * PIXEL, 23, 23),1)

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

            # if level[i][j] == 9: # cổng ma 
            #     pygame.draw.line(screen, 'white', (j * PIXEL, i * PIXEL + (0.5 * PIXEL)),(j * PIXEL + PIXEL, i * PIXEL + (0.5 * PIXEL)), 3)
            pygame.draw.line(screen, 'white', (14* PIXEL, 16 * PIXEL + (0.5 * PIXEL)),(14 * PIXEL + PIXEL, 16 * PIXEL + (0.5 * PIXEL)), 3)
            pygame.draw.line(screen, 'white', (15 * PIXEL, 16 * PIXEL + (0.5 * PIXEL)),(15 * PIXEL + PIXEL, 16 * PIXEL + (0.5 * PIXEL)), 3)
     
def canMove(row, col):
    if col <= -1 or col == len(level[0]):
        return True
    if level[int(row)][int(col)] < 3:
        return True
    return False

def reset():
    global game
    game.ghosts = [Ghost(18.0,12.0,'blue'), Ghost(18.0,14.0,'red'), Ghost(18.0,15.0,'pink'), Ghost(18.0,17.0,"orange") ]
    for ghost in game.ghosts:
        ghost.setTarget()
    game.pacman = Pacman(27,15) 
    game.lives -= 1
    game.render()
    

game = Game(score= 0)
ghostGate = [[16, 14], [16, 15]]

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


    game.render() # draw pac man, ghost, lives
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.pacman.newDir= 0
            if event.key == pygame.K_LEFT:
                game.pacman.newDir= 1
            if event.key == pygame.K_UP:
                game.pacman.newDir= 2
            if event.key == pygame.K_DOWN:
                game.pacman.newDir= 3
    
    game.update() # update  (logic score), (pac-man di chuyển)
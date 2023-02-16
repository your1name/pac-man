import pygame, sys, math, random
import math
from pygame.locals import *
from random import randrange


# 0 = empty black rectangle, 1 = dot, 2 = big dot, 3 = vertical line,
# 4 = horizontal line, 5 = top right, 6 = top left, 7 = bot left, 8 = bot right
# -1 = ghost space
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



TextPath = "assets/TextImages/"
 # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
PI = math.pi
WIDTH = 700
HEIGHT = 874
# 700 // 30 = 23
#805 - 23*2 - 23 // 32 = 23
PIXEL = 23
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

        self.pacman = Pacman(27,15) # khởi tạo vị trí ban đầu của Pacman
        # khởi tạo vị trí ban đâu của các đối tượng Ghost
        self.ghosts = [Ghost(18.0,12.0,'blue'), Ghost(18.0,14.0,'red'), Ghost(18.0,15.0,'pink'), Ghost(18.0,17.0,"orange") ]
        self.score = score
        self.lives  = 2 # Nhân vật chơi có 2 mạng

        self.paused = True
        self.started = False
    
    
    def draw_live(self):
    #pygame.draw.rect(screen,(255,255,255),(30 , 835, 23, 23),1)
        for i in range(self.lives):
            screen.blit(pygame.transform.scale(player_images[0], (25, 25)), (30 + i * 40, 830))
    
    def update(self):
       
        if self.paused or not self.started:
            self.drawReady()
            pygame.display.update()
            return

        # Mục tiêu của con Ghost là pacman 
        if not self.ghosts[0].attacked and not self.ghosts[0].dead:
            self.ghosts[0].target = [self.pacman.row, self.pacman.col]
        
        for ghost in self.ghosts:
            ghost.update() # Ghost di chuyển

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
                        ghost.attackedCount = 0
                        ghost.setAttacked(True)     # spooked
                        ghost.setTarget()
        self.checkSurroundings()
        
       
    def render(self):

        self.displayScore()
        self.draw_live()
        self.pacman.draw()

        for ghost in self.ghosts:
             ghost.draw()

        pygame.display.update()
    # Kiểm tra sự va chạm giữa Pacman và Ghost
    def touchingPacman(self, row, col):
        if row - 0.5 <= self.pacman.row and row >= self.pacman.row and col == self.pacman.col:
            # cùng cột, nằm dưới , -0.5 thì đi qua pacman
            return True
        elif row + 0.5 >= self.pacman.row and row <= self.pacman.row and col == self.pacman.col:
            # cùng cột, nằm trên , +0.5 thì đi qua pacman
            return True
        elif row == self.pacman.row and col - 0.5 <= self.pacman.col and col >= self.pacman.col:
            # cùng hàng, nằm dưới , -0.5 thì đi qua pacman
            return True
        elif row == self.pacman.row and col + 0.5 >= self.pacman.col and col <= self.pacman.col:
            # cùng hàng, nằm trên , +0.5 thì đi qua pacman
            return True
        elif row == self.pacman.row and col == self.pacman.col:
            # cùng cột, cùng cột với pacman
            return True
        return False


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
    
    def drawReady(self):
        ready = ["tile274.png", "tile260.png", "tile256.png", "tile259.png", "tile281.png", "tile283.png"]
        for i in range(len(ready)):
            letter = pygame.image.load(TextPath + ready[i])
            letter = pygame.transform.scale(letter, (int(23), int(23)))
            screen.blit(letter, ((11 + i) * 23, 20 * 23, 23, 23))
    
    def checkSurroundings(self):
        # Check khi Pacman chết
        for ghost in self.ghosts:
            # Kiểm tra va chạm  của Ghost và pacman khi Ghost không ở trạng thái sợ hãi
            if self.touchingPacman(ghost.row, ghost.col) and not ghost.attacked:
                # Khi mạng = 0 thì bạn thua
                if self.lives == 0:
                    print("You lose")
                    self.gameOver = True
            
                    over = pygame.image.load(f'Media/over.png')
                    over = pygame.transform.scale(over, (700,750))
                    screen.blit(over, (0, 69))
                    pygame.display.update()
                    pause(10000000)
                    global running
                    running = False
                    return
                
                self.started = False
                reset()
            # kiểm tra nếu Pacman và Ghost va chạm khi Ghost ở trạng thái sợ hãi nhưng Ghost không chết
            elif self.touchingPacman(ghost.row, ghost.col) and ghost.isAttacked() and not ghost.isDead():
                # thì Ghost sẽ chết khi bị Pacman ăn
                ghost.setDead(True)
                ghost.setTarget() # set lại mục tiêu là quay lại vị trí ban đầu
                ghost.ghostSpeed = 1
                ghost.row = math.floor(ghost.row)
                ghost.col = math.floor(ghost.col)

# Xây dựng pacman      
class Pacman:
    def __init__(self, row, col):
        self.row = row # chỉ số hàng
        self.col = col # chỉ số cột
        self.pacSpeed = 1/8 # bước di chuyển của Pacman
        self.dir = 0 # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        self.newDir = 0 # Hướng di chuyển mới 
      
    # Vẽ nhân vật chơi Pacman
    def draw(self): 
    # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        if self.dir == 0:  # di chuyển sang bên phải thì in ra màn hình game 
            screen.blit(player_images[counter // 8], (self.col*23, self.row*23))
        elif self.dir == 1:  # di chuyển sang bên trái in màn hình game đối tượng Pacman quay sang ngang 
            screen.blit(pygame.transform.flip(player_images[counter // 8], True, False), (self.col*23, self.row*23))
        elif self.dir == 2:  # di chuyển lên trên in màn hình game đối tượng Pacman xuống dưới thì xoay một góc 90
            screen.blit(pygame.transform.rotate(player_images[counter // 8], 90), (self.col*23, self.row*23))
        elif self.dir == 3:  # di chuyển xuống dưới in màn hình game đối tượng Pacman xuống dưới thì xoay một góc 270
            screen.blit(pygame.transform.rotate(player_images[counter // 8], 270), (self.col*23, self.row*23))     
    
    # Pacman di chuyển
    def update(self):
        if self.newDir == 2: # Khi di chuyển lên trên
            # kiểm tra xem điểm tiếp theo di chuyển lên trên có đi được không
            if canMove(math.floor(self.row - self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row -= self.pacSpeed # di chuyển lên một đoạn  1 / 8
                self.dir = self.newDir # set lại hướng đi mới
                return
        elif self.newDir == 0: # khi di chuyển bên phải
            # Kiểm tra xem điểm tiếp theo di chuyển sang bên phải có đi được không
            if canMove(self.row, math.ceil(self.col + self.pacSpeed)) and self.row % 1.0 == 0:
                self.col += self.pacSpeed # di chuyển sang một đoạn  1 / 8
                self.dir = self.newDir # set lại hướng đi mới
                return
        elif self.newDir == 3: # khi di chuyển xuống dưới
             # Kiểm tra xem điểm tiếp theo di chuyển sang xuống có đi được không
            if canMove(math.ceil(self.row + self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row += self.pacSpeed # di chuyển xuống một đoạn  1 / 8
                self.dir = self.newDir # set lại hướng đi mới
                return
        elif self.newDir == 1: # khi di chuyển sang trái
             # Kiểm tra xem điểm tiếp theo di chuyển sang trái có đi được không
            if canMove(self.row, math.floor(self.col - self.pacSpeed)) and self.row % 1.0 == 0:
                self.col -= self.pacSpeed # di chuyển sang một đoạn  1 / 8
                self.dir = self.newDir
                return

        if self.dir == 2: # khi di chuyển đi lên
            if canMove(math.floor(self.row - self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row -= self.pacSpeed
        elif self.dir == 0: # khi di chuyển sang phải
            if canMove(self.row, math.ceil(self.col + self.pacSpeed)) and self.row % 1.0 == 0:
                self.col += self.pacSpeed
        elif self.dir == 3: # khi di chuyển đi xuống
            if canMove(math.ceil(self.row + self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row += self.pacSpeed
        elif self.dir == 1: # khi di chuyển đi sang trái
            if canMove(self.row, math.floor(self.col - self.pacSpeed)) and self.row % 1.0 == 0:
                self.col -= self.pacSpeed
        
# Xây dựng đối tượng Ghost     
class Ghost:
    def __init__(self, row, col, color) :
        self.row = row # chỉ số hàng trong ma trận
        self.col = col # chỉ số cột trong ma trận
        self.attacked = False # khi Ghost sợ hãi
        self.color = color # màu của các con đối tượng Ghost
        self.dir = randrange(4) # hướng đi của Ghost
        self.dead = False # đối tượng Ghost chết
        self.target = [-1, -1] # mục tiêu của ghost
        self.ghostSpeed = 1/8 # tốc độ di chuyển Ghost
        self.lastLoc = [-1, -1] # Tọa độ điểm cuối ghost
        self.attackedTimer = 240 # thời gian Ghost sợ hãi
        self.attackedCount = 0 # đếm thời gian ở trạng thái sợ hãi
        self.deathTimer = 120 # thời gian Ghost bị chết
        self.deathCount = 0 # đếm thời gian ở trạng thái chết

    # Vẽ đối tượng Ghost
    def draw(self):
        ghostImage = pygame.image.load(f'assets/ghost_images/dead.png')
        if self.dead: # Khi Ghost ở trạng thái chết
            ghostImage = pygame.image.load(f'assets/ghost_images/dead.png')
        elif self.attacked: # Khi Ghost ở trạng thái sợ hãi
            ghostImage = pygame.image.load(f'assets/ghost_images/powerup.png') # spooked
        
        # Vẽ Ghost với 4 màu "Blue", "Pink", "Orange", "Red"
        else:
            if self.color == "blue":
                ghostImage = pygame.image.load(f'assets/ghost_images/blue.png')
            elif self.color == "pink":
                ghostImage = pygame.image.load(f'assets/ghost_images/pink.png')
            elif self.color == "orange":
                ghostImage = pygame.image.load(f'assets/ghost_images/orange.png')
            elif self.color == "red":
                ghostImage = pygame.image.load(f'assets/ghost_images/red.png')
        
        # Chuyển thành đối tượng với kích thước (30,30)
        ghostImage = pygame.transform.scale(ghostImage, (30,30))
        # Vẽ lên màn hình
        screen.blit(ghostImage, (self.col *23, self.row * 23))
    
    # Ghost di chuyển
    def update(self):
        if self.target == [-1, -1] or (self.row == self.target[0] and self.col == self.target[1]) or board[int(self.row)][int(self.col)] == -1 or self.dead:
            self.setTarget() # tìm mục tiêu
        self.setDir() # tìm đường đi đến mục tiêu là ngắn nhất
        self.move() #  ghost di chuyển

        if self.attacked: # Nếu Ghost sang trạng thái sợ hãi
            self.attackedCount += 1 # đếm thời gian ghost ở trạng thái sợ hãi

        if self.attacked and not self.dead: # Nếu Ghost ở trạng thái sọ hại nhưng không chết
            self.ghostSpeed = 1/16 # di chuyển với bước nhảy là 1 / 16
        
        # khi thời gian thiết lập bằng thời gian thực Ghost trong trạng thái sợ hãi
        if self.attackedCount == self.attackedTimer and self.attacked:
            if not self.dead: # khi Ghost chết
                self.ghostSpeed = 1/8 # di chuyển với bước nhảy 1 / 8
                self.row = math.floor(self.row) 
                self.col = math.floor(self.col)
            
            # Sau đó Ghost sẽ quay về trạng thái ban đầu
            self.attackedCount = 0
            self.attacked = False
            self.setTarget()
        
        # Nếu ghost chết và trở lại vị trí ban đầu
        if self.dead and board[self.row][self.col] == -1:
            self.deathCount += 1 # đếm thời gian ghost ở trạng thái chết
            self.attacked = False
            # thời gian thiết lập bằng thời gian thực Ghost ở trạng thái chết thì quay lại trang thái ban đầu
            if self.deathCount == self.deathTimer:
                self.deathCount = 0 # khởi tạo lại thời gian chết
                self.dead = False
                self.ghostSpeed = 1/8 # di chuyển với bước nhảy 1 / 8


    def setAttacked(self, isAttacked):
        self.attacked = isAttacked

    def isAttacked(self):
        return self.attacked

    def setDead(self, isDead):
        self.dead = isDead

    def isDead(self):
        return self.dead
    
    # ghost di chuyển
    def move(self):
        self.lastLoc = [self.row, self.col]
        if self.dir == 2: # khi di chuyển lên trên
            self.row -= self.ghostSpeed
        elif self.dir == 0: # khi di chuyển sang phải
            self.col += self.ghostSpeed
        elif self.dir == 3: # khi di chuyển xuống dưới
            self.row += self.ghostSpeed
        elif self.dir == 1: # khi di chuyển sang trái
            self.col -= self.ghostSpeed

        # Trường hợp Ghost đi được qua đường hầm giữa bản đồ
        if self.col < 0:
            self.col = len(level[0]) - 1
        
        if self.col > len(level[0]) - 1:
            self.col = 1
    
    # tính khoảng cách giữa 2 điểm
    def calcDistance(self, a, b):
        dR = a[0] - b[0] # khoảng cách giữa x1 - x2
        dC = a[1] - b[1] # khoảng cách giữa y1 - y2
        return math.sqrt((dR * dR) + (dC * dC))
    
    # Kiểm tra điểm tiếp theo Ghost có thể di chuyển được không
    def isValid(self, cRow, cCol):
        # Ghost có thể di chuyển qua đường hầm
        if cCol < 0 or cCol > len(board[0]) - 1:
            return True

        for ghost in game.ghosts:
            if ghost.color == self.color:
                continue
            # Nếu điểm tiếp theo đúng bằng vị trí hiện tại và Ghost không chết thì không di chuyển được
            if ghost.row == cRow and ghost.col == cCol and not self.dead:
                return False
            # Kiểm tra xem trong list có phải cổng ma không
        if not ghostGate.count([cRow, cCol]) == 0:
            # nếu Ghost chết và nó đang ở phía trên cổng ma
            if self.dead and self.row < cRow:
                return True
            # Nếu Ghost không chết và không sợ hãi và đang phía dưới cổng ma
            elif self.row > cRow and not self.dead and not self.attacked:
                return True
            else:
                return False
        # Ghost không đi được qua các tường
        if board[cRow][cCol] >= 3 :
            return False
        return True
    
    # Tìm điểm mục tiêu của Ghost
    def setTarget(self):

        # Khi đối tượng Ghost đang ở trong nhà và bắt đầu di chuyển ra
        if board[int(self.row)][int(self.col)] == -1 and not self.dead:
            self.target = [ghostGate[0][0] - 1, ghostGate[0][1]+1] # 15 15
            return
        # Khi đối tượng Ghost chết và đã về nhà thì mục tiêu là vị trí ban đầu
        elif board[int(self.row)][int(self.col)] == -1 and self.dead:
            self.target = [self.row, self.col]
        # Khi đối tượng Ghost chết thì quay lại nhà để hồi sinh
        elif self.dead:
            self.target = [15, 14]  # 2 điểm cổng ma
            return
       
        while True:
            # Mục tiêu sẽ là một điểm ngẫu nhiên trên bản đồ
            self.target = [randrange(3,36), randrange(30)]
               # Kiểm tra xem mục tiêu có thể đi tới được hay không
               # Nếu đi được thì break  
            if not board[self.target[0]][self.target[1]] >= 3 and not board[self.target[0]][self.target[1]] == -1:
                break

    # TÌm hướng đi tốt nhất và đường đi ngắn nhất đến mục tiêu
    def setDir(self):
        # BFS search 
        dirs = [[0, 0, self.ghostSpeed],
                [1, 0, -self.ghostSpeed],
                [2, -self.ghostSpeed, 0],
                [3, self.ghostSpeed, 0]
        ]
        # xếp hướng một cách ngẫu nhiên 
        random.shuffle(dirs)
        best = 10000 # khởi tạo  khoảng cách ban đầu
        bestDir = -1 # khởi tạo hướng đi tốt nhất

        for newDir in dirs:
            # tính khoảng cách của mục tiêu với điểm di chuyển tiếp theo
            if self.calcDistance(self.target, [self.row + newDir[1], self.col + newDir[2]]) < best:
                if not (self.lastLoc[0] == self.row + newDir[1] and self.lastLoc[1] == self.col + newDir[2]):
                    # nếu đi lên và kiểm tra điểm tiếp theo có đi di chuyển được không
                    if newDir[0] == 2 and self.col % 1.0 == 0: 
                        if self.isValid(math.floor(self.row + newDir[1]), int(self.col + newDir[2])):
                            bestDir = newDir[0] 
                            # khoảng cách ngắn nhất sẽ là khoảng các giữa mục tiêu và điểm đi 
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

# Vẽ bản đồ map    
def draw_board():

    for i in range(len(level)):
        for j in range(len(level[i])):

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

            # draw cổng ma
            pygame.draw.line(screen, 'white', (14* PIXEL, 16 * PIXEL + (0.5 * PIXEL)),(14 * PIXEL + PIXEL, 16 * PIXEL + (0.5 * PIXEL)), 3)
            pygame.draw.line(screen, 'white', (15 * PIXEL, 16 * PIXEL + (0.5 * PIXEL)),(15 * PIXEL + PIXEL, 16 * PIXEL + (0.5 * PIXEL)), 3)

# Kiểm tra các điểm có thể đi của Pacman    
def canMove(row, col):
    # di chuyển được qua đường hầm
    if col <= -1 or col == len(level[0]):
        return True
    # Pacman không di chuyển được qua tường
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

def displayLaunchScreen():   
    launchScreen = pygame.image.load(f'Media/menu.png')
    launchScreen = pygame.transform.scale(launchScreen, (WIDTH-23*2,HEIGHT-23*8))
    screen.blit(launchScreen, (23, 23))
    pygame.display.update()
    
def pause(time):
    cur = 0
    while not cur == time:
        cur += 1

onLaunchScreen = True    
displayLaunchScreen()
game = Game(score= 0)
ghostGate = [[16, 14], [16, 15]]

running = True
while running:
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
    #print(game.pacman.row, game.pacman.col, f'score: {game.score}')
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            game.paused = False
            game.started = True
            
            if event.key == pygame.K_RIGHT:
                game.pacman.newDir= 0
            elif event.key == pygame.K_LEFT:
                game.pacman.newDir= 1
            elif event.key == pygame.K_UP:
                game.pacman.newDir= 2
            elif event.key == pygame.K_DOWN:
                game.pacman.newDir= 3
            elif event.key == pygame.K_SPACE:
                if onLaunchScreen:
                    onLaunchScreen = False
                    game.paused = True
                    game.started = False

    if not onLaunchScreen:  
        game.render() # draw pac man, ghost, lives
        game.update() # update  (logic score), (pac-man di chuyển)
import random
import pygame


pygame.init()

font20 = pygame.font.Font('freesansbold.ttf', 20)


# цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# параметры экрана
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
Flag = False
clock = pygame.time.Clock()
FPS = 30
from bri import Brick

# класс ракетки
class Striker:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.geekRect = pygame.Rect(posx, posy, width, height)
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    def display(self):
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    def update(self, yFac):
        self.posy = self.posy + self.speed * yFac

        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height

        self.geekRect = (self.posx, self.posy, self.width, self.height)

    def displayScore(self, text, score, x, y, color):
        text = font20.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)

        screen.blit(text, textRect)
 
    def getRect(self):
        return self.geekRect


# класс вратаря
class Goalkeeper:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.geekRect = pygame.Rect(posx, posy, width, height)
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)
 
    def display(self):
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)
 
    def update(self, yFac):
        self.posy = self.posy + self.speed * yFac

        self.geekRect = (self.posx, self.posy, self.width, self.height)
 
    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
 
        screen.blit(text, textRect)
 
    def getRect(self):
        return self.geekRect


# класс мяча
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = 0
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1
 
    def display(self):
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)   
 
    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed*self.yFac

        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1
 
        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
 
    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xFac *= -1
        self.firstTime = 1
 
    def hit(self):
        self.xFac *= -1
 
    def getRect(self):
        return self.ball


# основной код
def main():
    # начальное окно
    pygame.init()
    WIDTH1, HEIGHT1 = 900, 600
    screen = pygame.display.set_mode((WIDTH1, HEIGHT1))
    LEVEL = ''
    
    running = True
    while running:
        screen.fill("green")
        f1 = pygame.font.Font(None, 60)
        text1 = f1.render('FOOTBALL PONG', 1, (0, 0, 0))
    
        screen.blit(text1, (265, 50))
    
        f2 = pygame.font.Font(None, 30)
        text2 = f2.render('Choose level', 1, (0, 0, 0))
    
        screen.blit(text2, (360, 220))
    
        pygame.draw.rect(screen, (255, 0, 0), (190, 340, 80, 50), 0)
    
        pygame.draw.rect(screen, (255, 0, 0), (640, 340, 80, 50), 0)
    
        f3 = pygame.font.Font(None, 30)
        text3 = f3.render('EASY', 1, (255, 255, 255))
    
        screen.blit(text3, (200, 350))
    
        f4 = pygame.font.Font(None, 30)
        text4 = f4.render('HARD', 1, (255, 255, 255))
    
        screen.blit(text4, (650, 350))    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 190 and mx < 270 and my > 340 and my < 390:
                    LEVEL = 'EASY'
                    running = False
                if mx > 640 and mx < 720 and my > 340 and my < 390:
                    LEVEL = 'HARD'
                    running = False            
    
    
        pygame.display.flip()    

    running = True

    geek1 = Goalkeeper(20, 10, 10, 250, 5, GREEN)
    flagg = False

    geek2 = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN) 

    ball = Ball(WIDTH // 2, random.randint(150, 370), 7, 4, WHITE)
 
    if LEVEL == "HARD":
        brick1 = Brick(400, 150, 20, 20, RED)
        brick2 = Brick(400, 170, 20, 20, GREEN)
        brick3 = Brick(400, 190, 20, 20, RED)
        brick4 = Brick(400, 210, 20, 20, BLUE)
        brick5 = Brick(400, 230, 20, 20, RED)
        brick6 = Brick(400, 250, 20, 20, GREEN)
        brick7 = Brick(400, 270, 20, 20, BLUE)
        brick8 = Brick(400, 290, 20, 20, GREEN)
        brick9 = Brick(400, 310, 20, 20, RED)
        brick10 = Brick(400, 330, 20, 20, BLUE)
        brick11 = Brick(400, 350, 20, 20, RED)
        brick12 = Brick(400, 370, 20, 20, GREEN)
        list_bricks = [brick1, brick2, brick3, brick4, brick5, brick6, brick7,
                       brick8, brick9, brick10, brick11, brick12]        
    elif LEVEL == "EASY":
        brick3 = Brick(400, 190, 20, 20, RED)
        brick4 = Brick(400, 210, 20, 20, BLUE)
        brick5 = Brick(400, 230, 20, 20, RED)
        brick6 = Brick(400, 250, 20, 20, GREEN)
        brick7 = Brick(400, 270, 20, 20, BLUE)
        brick8 = Brick(400, 290, 20, 20, GREEN)
        brick9 = Brick(400, 310, 20, 20, RED)
        brick10 = Brick(400, 330, 20, 20, BLUE)
        list_bricks = [brick3, brick4, brick5, brick6, brick7,
                       brick8, brick9, brick10]
        

    listOfGeeks = [geek2]

    geek1Score, geek2Score = 0, 0
    geek1YFac, geek2YFac = 0, 0


 
    # сама игра
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    geek2YFac = -1
                if event.key == pygame.K_DOWN:
                    geek2YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    geek2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    geek1YFac = 0


        if geek1.posy >= -10 and geek1.posy <= 350 and flagg == False:
            geek1YFac = 1
            if geek1.posy == 350:
                flagg = True
        else:
            geek1YFac = -1
            if geek1.posy <= 0:
                flagg=False
        if pygame.Rect.colliderect(ball.getRect(), geek1.getRect()):
            ball.hit()
            Flag=True
        else:
            Flag=False

        if ball.posx < 400:
            Flag = True
        elif ball.posx > 450:
            Flag = False
        

        for geek in listOfGeeks:

            if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):

                    bally = ball.posy
                    geeky=geek.posy
                    if bally < geeky + 60 and bally > geeky + 40:
                        ball.yFac=0
                    elif bally < geeky + 20:
                        ball.yFac = -2
                    elif bally > geeky + 80:
                        ball.yFac = 2
                    elif bally < geeky + 80 and bally > geeky + 60:
                        ball.yFac = 1
                    elif bally < geeky + 40 and bally > geeky + 20:
                        ball.yFac = -1
                  
                    ball.hit()

        for x in list_bricks:
            if pygame.Rect.colliderect(ball.getRect(), x.getRect()):
                ball.hit()
                if Flag == True:
                    del list_bricks[list_bricks.index(x)]


        geek1.update(geek1YFac)
        geek2.update(geek2YFac)
        
        
        
        
        point = ball.update()
 
        if point == -1:
            geek1Score += 1
        elif point == 1:
            geek2Score += 1
 
        if point:
            ball.reset()
 
       
       
       
       
       

        geek1.display()
        
        geek2.display()
        
                
        
        ball.display()
 

        geek1.displayScore("Geek_1 : ", geek1Score, 100, 20, WHITE)
        
      
        geek2.displayScore("Geek_2 : ", geek2Score, WIDTH-100, 20, WHITE)
 

        for x in list_bricks:
            x.display()
        
        if LEVEL == "EASY" and (geek1Score == 3 or geek2Score == 3):
            f = open("record.txt", "a")
            f.write(f'{geek1Score} - {geek2Score}, level: {LEVEL} \n')
            f.close
            running = False
        if LEVEL == "HARD" and (geek1Score == 5 or geek2Score == 5):
            f = open("record.txt", "a")
            f.write(f'{geek1Score} - {geek2Score}, level: {LEVEL} \n')
            f.close            
            running = False        

            

        pygame.display.update()
        clock.tick(FPS)

 
    # конечное окно
    WIDTH2, HEIGHT2 = 900, 600
    screen = pygame.display.set_mode((WIDTH2, HEIGHT2))
        
        
    screen.fill((255, 215, 0))
    f5 = pygame.font.Font(None, 100)
    text5 = f5.render('GAME OVER', 1, (65, 105, 225))
        
    screen.blit(text5, (250, 80))
        
    f6 = pygame.font.Font(None, 250)
    text6 = f6.render(f'{geek1Score}    -    {geek2Score}', 1, (85, 107, 47))
        
    screen.blit(text6, (150, 300))

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass

 
if __name__ == "__main__":
    main()
    pygame.quit()
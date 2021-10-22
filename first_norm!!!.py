import pygame
from pygame.draw import *
from random import *
pygame.init()
font_init=pygame.font.Font(None, 36)

FPS = 70
screen = pygame.display.set_mode((800, 800))
screen.fill((0, 0, 0))


points = 0
'''количество очков'''

print('Введите ник')
name = str(input())

new = True

file = open('best_scores.txt', 'r')

lines = file.readlines()
lenght = len(lines)
tmp2 = lenght//2
'''считываем все строки'''

best_point = 0

# итерация по строкам
for i in range (0,lenght,1):
    if (lines[i].strip() == name):
        best_point = int(lines[i+1])
        new = False

players = {lines[2*i].strip(): int(lines[2*i+1]) for i in range (0,tmp2,1)}
print("Текущий список лидеров")
print(players)

file.close

f = open(r'C:\1 УЧЕБА\python\game\best_scores.txt', 'w')

number_of_aims=10
dt=4
vx=[]
vy=[]
x=[]
y=[]
r=[]
color=[]
lev=[]
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [GREEN, BLUE, RED]

for i in range (number_of_aims):

    x.append(randint(100, 700))
    y.append(randint(100, 700))
    tmp=randint(0, 2)
    color.append(COLORS[tmp])
    if color[i]==(0, 255, 0):
        r.append(randint(20, 28))
        vx.append((random()*2-1)*0.8)
        vy.append((random()*2-1)*0.8)
        lev.append(i%3)
    elif color[i]==(0, 0, 255):
        r.append(randint(15, 25))
        vx.append((random()*4-2)*0.9)
        vy.append((random()*4-2)*0.9)
        lev.append(i%3)
    elif color[i]==(255, 0, 0):
        r.append(randint(10, 20))
        vx.append((random()*6-3))
        vy.append((random()*6-3))
        lev.append(i%3)
        
def new_ball(i):
    '''рисует новый шарик'''
#    global x, y, r
    circle(screen, color[i], (x[i], y[i]), r[i])
    x[i]+=dt*vx[i]
    y[i]+=dt*vy[i]
    if x[i]<r[i] or x[i]>800-r[i]:
        x[i]-=dt*vx[i]
        vx[i]=(random()*2-1)*(lev[i]+1)*((lev[i]-1)*0.1+0.6)
    if y[i]<r[i] or y[i]>800-r[i]:
        y[i]-=dt*vy[i]
        vy[i]=(random()*2-1)*(lev[i]+1)*((lev[i]-1)*0.1+0.6)


pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    result=str(name)+'  '+str(points)
    f1 = pygame.font.Font(None, 72)
    text1 = f1.render(str(result), True, (0, 255, 0)) 
    screen.blit(text1, (50, 50))
    pygame.display.set_caption("Win It All!")
    clock.tick(FPS)
    
    for i in range (number_of_aims):
        new_ball(i)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (number_of_aims):
                if (((event.pos[0]-x[i])**2+(event.pos[1]-y[i])**2)<(r[i])**2):
                    points+=lev[i]+1
                    x[i]=randint(100, 700)
                    y[i]=randint(100, 700)
                    vx[i]=(random()*2-1)*(lev[i]+1)*((lev[i]-1)*0.1+0.6)
                    vy[i]=(random()*2-1)*(lev[i]+1)*((lev[i]-1)*0.1+0.6)


    pygame.display.update()
    screen.fill((0, 0, 0))
        

    
if ( new == True ):
    players[name.strip()] = points
else:
    if (players[name.strip()] <= points):
        players[name.strip()] = points


    
pygame.quit()
'''Конец цикла pygame'''

top_players = dict(sorted(players.items(), key = lambda val: val[1]))
print(top_players)
'''Записываем игроков в словарь и фильтруем'''

for i in top_players:
    f.write(str(i) + '\n')
    f.write(str(top_players[i]) + '\n' )
f.close()
'''Записываем результат'''

import pygame
from random import randint, choice, randrange

pygame.init()

# Color variables
GREEN = (0,255,0)
PURPLE = (106, 13, 173)
RED = (217, 33, 33)

BLACK = (0,0,0)
WHITE = (255,255,255)
colors_list = [GREEN, PURPLE, RED]
color_count = 0

# Constant variables
width = 800
height = 600
fontsize = 17
FPS = 20
clock = pygame.time.Clock()
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
font = pygame.font.SysFont('Arial', fontsize, True, False)

# Screen
wn = pygame.display.set_mode((width,height))
pygame.display.set_caption('Matrix')


class Line:
    def __init__(self):
        
        # Choose symbols
        self.simbs = []
        for _ in range(0,randint(10,20)):
            self.simbs.append(choice(abc))

        # Initial position
        self.xpos = randrange(fontsize,width - fontsize, fontsize)
        self.ypos = randrange(fontsize,height - fontsize, fontsize)

        self.charcount = 0
        self.count = 0
        self.complete = False

    # Draw the lines
    def draw(self):
        for self.char in range(0,self.charcount):
            if self.count - len(self.simbs) // 2 <= self.char:
                if self.char == self.charcount - 1:
                    self.msg = font.render(self.simbs[self.char], True, WHITE)
                if self.char < self.charcount -1:
                    self.msg = font.render(self.simbs[self.char], True, GREEN)
                wn.blit(self.msg,(self.xpos,self.ypos + (fontsize * self.char)))
        if self.charcount < len(self.simbs) - 1:
            self.charcount += 1
        self.count += 1
        if self.count >= len(self.simbs) * 3:
            self.complete = True
        
# Generate new lines
def create_new_line():
    for c in range(0,4):
        objs = Line()
        objs_list.append(objs)
objs_list = []

# Main loop
pygame.time.delay(2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
    
    clock.tick(FPS)
    create_new_line()
    for obj in objs_list:
        obj.draw()
        if obj.complete == True:
            del objs_list[objs_list.index(obj)]
    pygame.display.update()
    wn.fill((BLACK))

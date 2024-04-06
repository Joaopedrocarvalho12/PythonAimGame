import math
import random
import pygame
import time
pygame.init()


WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set.set_caption("Aim Trainer")

TARGE_INCREMENT  = 400
TARGE_EVENT = pygame.USEREVENT

class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"

    def __init__(self,x,y):
        self.x = float(x)
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False

        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)





def main():
    run = True
    target = []

    pygame.time.set_timer(TARGE_EVENT, TARGER_INCREMENT)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = false
                break
            if event.type == TARGE_EVENT
                x = random.radint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.radint(TARGET_PADDING. HEIGHT - TARGET_PADDING)
                target = Target(x,y)
                targets.append(target)



    pygame.quit()
if __name__ == "__main__":
    main()
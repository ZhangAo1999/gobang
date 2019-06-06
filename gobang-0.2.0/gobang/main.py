import pygame
from pygame.locals import *


class Pan:
    def __init__(self, screen):
        self.x = 200
        self.y = 50
        self.length = 500
        self.color = (255, 255, 150)
        self.screen = screen

    def display(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.length, self.length))
        x1, y1 = 200, 50
        x2, y2 = 700, 50
        color = (0, 0, 0)
        for i in range(26):
            pygame.draw.line(self.screen, color, (x1, y1), (x2, y2))
            y1 += 20
            y2 += 20
        x1, y1 = 200, 50
        x2, y2 = 200, 550
        for i in range(26):
            pygame.draw.line(self.screen, color, (x1, y1), (x2, y2))
            x1 += 20
            x2 += 20


class BaiQi:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = (255, 255, 255)
        self.size = 10

    def display(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size, 0)


class HeiQi:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = (0, 0, 0)
        self.size = 10

    def display(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size, 0)


def heiqi(screen):
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            x = x // 20 * 20
            y = (y - 50) // 20 * 20 + 50
            return x, y
        if event.type == MOUSEMOTION:
            x, y = event.pos
            hei_qi = HeiQi(screen, x, y)
            hei_qi.display()
        return None


def baiqi(screen):
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            x = x // 20 * 20
            y = (y - 50) // 20 * 20 + 50
            return x, y
        if event.type == MOUSEMOTION:
            x, y = event.pos
            bai_qi = BaiQi(screen, x, y)
            bai_qi.display()
        return None


def close():
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()


def check(qi_pan, qi, x, y):
    for i in range(-4, 4):
        if 0 <= x + i < 22:
            win = True
            for j in range(5):
                if qi_pan[x + i + j][y] != qi:
                    win = False
            if win:
                if qi == "hei":
                    return "黑棋胜"
                else:
                    return "白棋胜"
    for i in range(-4, 4):
        if 0 <= y + i < 22:
            win = True
            for j in range(5):
                if qi_pan[x][y + i + j] != qi:
                    win = False
            if win:
                if qi == "hei":
                    return "黑棋胜"
                else:
                    return "白棋胜"
    for i in range(-4, 4):
        if 0 <= y + i < 22 and 0 <= x + i < 22:
            win = True
            for j in range(5):
                if qi_pan[x + i + j][y + i + j] != qi:
                    win = False
            if win:
                if qi == "hei":
                    return "黑棋胜"
                else:
                    return "白棋胜"
    for i in range(-4, 4):
        if 0 <= y + i < 22 and 4 <= x + i < 26:
            win = True
            for j in range(5):
                if qi_pan[x + i - j][y + i + j] != qi:
                    win = False
            if win:
                if qi == "hei":
                    return "黑棋胜"
                else:
                    return "白棋胜"
    return None


def start():
    pygame.init()
    screen = pygame.display.set_mode((900, 600), 0, 32)
    pan = Pan(screen)
    color = (0, 150, 150)
    hei_qi_list = []
    bai_qi_list = []
    qi_pan = []
    for i in range(26):
        k = []
        for j in range(26):
            s = []
            k.append(s)
        qi_pan.append(k)
    i = 1
    result = None
    while True:
        pygame.draw.rect(screen, color, (0, 0, 900, 600))
        pan.display()
        if i % 2:
            qi = heiqi(screen)
            if qi:
                x, y = qi
                hei_qi = HeiQi(screen, x, y)
                x = (x - 200) / 20
                y = (y - 50) / 20
                x, y = int(x), int(y)
                if not qi_pan[x][y]:
                    qi_pan[x][y] = "hei"
                    result = check(qi_pan, qi_pan[x][y], x, y)
                    hei_qi_list.append(hei_qi)
                    i += 1
        else:
            qi = baiqi(screen)
            if qi:
                x, y = qi
                bai_qi = BaiQi(screen, x, y)
                x = (x - 200) / 20
                y = (y - 50) / 20
                x, y = int(x), int(y)
                if not qi_pan[x][y]:
                    qi_pan[x][y] = "bai"
                    result = check(qi_pan, qi_pan[x][y], x, y)
                    bai_qi_list.append(bai_qi)
                    i += 1
        for hei_qi in hei_qi_list:
            hei_qi.display()
        for bai_qi in bai_qi_list:
            bai_qi.display()
        if result:
            win = pygame.font.Font("./ziti/zi_ti.ttf", 36)
            color_win = (0, 0, 0) if result == "黑棋胜" else (255, 255, 255)
            win = win.render(result, 1, color_win)
            screen.blit(win, (400, 270))
            hei_qi_list = []
            bai_qi_list = []
            qi_pan = []
            pygame.display.update()
            pygame.time.delay(3000)
            for i in range(26):
                k = []
                for j in range(26):
                    l = []
                    k.append(l)
                qi_pan.append(k)
            i = 1
            result = None
        close()
        pygame.display.update()
        pygame.time.delay(100)


if __name__ == "__main__":
    start()

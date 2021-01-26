import math
import random

import pygame


class Vec2d:
    """2-мерный вектор."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Vec2d(self.x * k, self.y * k)

    def __len__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def int_pair(self):
        """Возвращает кортеж из двух целых чисел."""
        return int(self.x), int(self.y)


class Polyline:
    def __init__(self, points, speeds):
        self.points = points
        self.speeds = speeds

    def set_points(self, screen_dim):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]

            points = self.points[p].int_pair()
            speeds = self.speeds[p].int_pair()

            if points[0] > screen_dim[0] or points[0] < 0:
                self.speeds[p] = Vec2d(-speeds[0], speeds[1])

            if points[1] > screen_dim[0] or points[1] < 0:
                self.speeds[p] = Vec2d(speeds[0], -speeds[0])

    def draw_points(self, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки на экране"""
        if style == 'line':
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(
                    gameDisplay,
                    color,
                    self.points[p_n].int_pair(),
                    self.points[p_n + 1].int_pair(),
                    width
                )
        elif style == 'points':
            for p in self.points:
                pygame.draw.circle(
                    gameDisplay,
                    color,
                    # (p[0].int_pair(), p[1].int_pair()),
                    p.int_pair(),
                    width
                )


class Knot(Polyline):
    # def __init__(self, points, speeds):
    #     super().__init__(points, speeds)

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return (points[deg] * alpha) + (self.get_point(points, alpha, deg-1) * (1 - alpha))

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self, count):
        if len(points) < 3:
            return []
        res = []
        for i in range(-2, len(points) - 2):
            ptn = []
            ptn.append((points[i] + points[i + 1]) * 0.5)
            ptn.append(points[i + 1])
            ptn.append((points[i + 1] + points[i + 2]) * 0.5)

            res.extend(self.get_points(ptn, count))
        return res


SCREEN_DIM = (800, 600)

def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    points = []
    speeds = []
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(Vec2d(event.pos[0], event.pos[1]))
                speeds.append(Vec2d(random.random() * 2, random.random() * 2))
                # points.append(event.pos)
                # speeds.append((random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        polyline = Polyline(points, speeds)
        polyline.draw_points()
        knot = Knot(points, speeds=None)
        polyline.points = knot.get_knot(steps)
        polyline.draw_points(style='line', color=color)
        polyline.points = points
        # draw_points(points)
        # draw_points(get_knot(points, steps), "line", 3, color)
        if not pause:
            polyline.set_points(SCREEN_DIM)
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
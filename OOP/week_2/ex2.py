from random import random
from typing import List, Tuple

import pygame
from numpy import sqrt


class Vec2d:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return Vec2d(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return Vec2d(self.x - vector.x, self.y - vector.y)

    def __mul__(self, number):
        return Vec2d(self.x * number, self.y * number)

    def __len__(self):
        return int(sqrt(self.x ** 2 + self.y ** 2))

    def int_pair(self):
        return int(self.x), int(self.y)


class Polyline:
    def __init__(self, app):
        self.app: Application = app
        self.line_points: List[Vec2d] = []
        self.ref_points: List[Vec2d] = []
        self.speeds: List[Vec2d] = []

    def add_point(self, ref_point: Vec2d, speed: Vec2d):
        """Adding a new reference point with its speed"""
        self.ref_points.append(ref_point)
        self.speeds.append(speed)

    def set_points(self):
        """Recalculation of reference points coordinates"""
        for i in range(len(self.ref_points)):
            self.ref_points[i] += self.speeds[i]

            if self.ref_points[i].x < 0 or self.ref_points[i].x > self.app.screen_size[0]:
                self.speeds[i].x *= -1

            if self.ref_points[i].y < 0 or self.ref_points[i].y > self.app.screen_size[1]:
                self.speeds[i].y *= -1

    def draw_points(self, width=3, color=(255, 255, 255)):
        """Drawing reference points"""
        for point in self.ref_points:
            pygame.draw.circle(self.app.game_display, color, point.int_pair(), width)

    def draw_lines(self, width=3, color=(255, 255, 255)):
        """Drawing lines by lines points"""
        for i in range(-1, len(self.line_points) - 1):
            pygame.draw.line(self.app.game_display, color,
                             self.line_points[i].int_pair(), self.line_points[i + 1].int_pair(), width)


class Knot(Polyline):
    def __init__(self, app):
        super().__init__(app)
        self.__supports_count: int = 100

    @property
    def supports_count(self):
        """Number of smoothing points"""
        return self.__supports_count

    @supports_count.setter
    def supports_count(self, value: int):
        self.__supports_count = value if value > 0 else 1
        self.line_points = self.__get_knot()

    def add_point(self, ref_point, speed):
        super().add_point(ref_point, speed)
        self.line_points = self.__get_knot()

    def set_points(self):
        super().set_points()
        self.line_points = self.__get_knot()

    def __get_knot(self) -> List[Vec2d]:
        line: List[Vec2d] = []
        if len(self.ref_points) >= 3:
            for i in range(-2, len(self.ref_points) - 2):
                points = [(self.ref_points[i] + self.ref_points[i + 1]) * 0.5,
                          self.ref_points[i + 1],
                          (self.ref_points[i + 1] + self.ref_points[i + 2]) * 0.5]
                line.extend(self.get_smooth_points(points))
        return line

    def get_smooth_points(self, base_points: List[Vec2d]):
        alpha = 1 / self.supports_count
        res = []
        for i in range(self.supports_count):
            point = base_points[0]
            for j in range(0, len(base_points)):
                point = base_points[j] * i * alpha + point * (1 - i * alpha)
            res.append(point)
        return res


class Application:
    def __init__(self, screen_size: Tuple[int, int]):
        pygame.init()
        self.screen_size = screen_size
        self.game_display = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("My Refactored Screen Saver")

        self.knot = Knot(self)

    def work(self):
        working = True
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
                        self.knot.line_points.clear()
                        self.knot.ref_points.clear()
                        self.knot.speeds.clear()
                    if event.key == pygame.K_p:
                        pause = not pause
                    if event.key == pygame.K_F1:
                        show_help = not show_help
                    if event.key == pygame.K_KP_PLUS:
                        self.knot.supports_count += 1
                    if event.key == pygame.K_KP_MINUS:
                        self.knot.supports_count -= 1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.knot.add_point(Vec2d(*event.pos), Vec2d(random() * 2, random() * 2))

            self.game_display.fill((0, 0, 0))
            hue = (hue + 1) % 360
            color.hsla = (hue, 100, 50, 100)
            self.knot.draw_points()
            self.knot.draw_lines(color=color)
            if not pause:
                self.knot.set_points()
            if show_help:
                self.draw_help()

            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()
        exit(0)

    def draw_help(self):
        self.game_display.fill((50, 50, 50))
        font1 = pygame.font.SysFont("courier", 24)
        font2 = pygame.font.SysFont("serif", 24)
        data = [["F1", "Show Help"],
                ["R", "Restart"],
                ["P", "Pause/Play"],
                ["Num+", "More points"],
                ["Num-", "Less points"],
                ["", ""],
                [str(self.knot.supports_count), "Current points"]]

        pygame.draw.lines(self.game_display, (255, 50, 50, 255), True,
                          [(0, 0), (800, 0), (800, 600), (0, 600)], 5)

        for i, text in enumerate(data):
            self.game_display.blit(font1.render(text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
            self.game_display.blit(font2.render(text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


if __name__ == '__main__':
    Application((800, 600)).work()
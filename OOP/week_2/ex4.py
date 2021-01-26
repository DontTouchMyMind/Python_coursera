import pygame
import random
import math

SCREEN_DIM = (800, 600)
gameDisplay = pygame.display.set_mode(SCREEN_DIM)


class Vec2d:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __sub__(self, other):
        """возвращает разность двух векторов"""
        vec = Vec2d(self.__x - other.__x, self.__y - other.__y)
        return vec

    def __add__(self, other):
        """возвращает сумму двух векторов"""
        vec = Vec2d(self.__x + other.__x, self.__y + other.__y)
        return vec

    def __mul__(self, k):
        """возвращает произведение вектора на число"""
        return Vec2d(self.__x * k, self.__y * k)

    def __truediv__(self, k):
        return Vec2d(self.__x / k, self.__y / k)

    def __len__(self):
        """возвращает длину вектора"""
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def int_pair(self):
        """возвращает пару координат, x и y типа int"""
        return (int(self.__x), int(self.__y))

    def float_pair(self):
        """возвращает пару координат, x и y типа float"""
        return (self.__x, self.__y)


class Polyline:
    def __init__(self, points, speeds):
        self.points = points
        self.speeds = speeds

    def set_points(self, screen_dim):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            points = self.points[p].float_pair()
            speeds = self.speeds[p].float_pair()

            if points[0] > screen_dim[0] or points[0] < 0:
                self.speeds[p] = Vec2d(-speeds[0], speeds[1])

            if points[1] > screen_dim[1] or points[1] < 0:
                self.speeds[p] = Vec2d(speeds[0], -speeds[1])

    def draw_points(self, gameDisplay, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(gameDisplay, color, self.points[p_n].int_pair(),
                                 self.points[p_n + 1].int_pair(), width)

        elif style == "points":
            for p in self.points:
                pygame.draw.circle(gameDisplay, color, p.int_pair(), width)


class Knot(Polyline):
    def __init__(self, points, speeds):
        super().__init__(points, speeds)

    def __get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + self.__get_point(points, alpha, deg - 1) * (1 - alpha)

    def __get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.__get_point(base_points, i * alpha))
        return res

    def get_knot(self, count):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)

            res.extend(self.__get_points(ptn, count))
        return res


def draw_help(steps):
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
    data.append(["f", "Faster"])
    data.append(["s", "Slowly"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


if __name__ == "__main__":
    pygame.init()
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
                if event.key == pygame.K_f:
                    """клавиша f - увеличение скорости движения линии"""
                    for index, _ in enumerate(speeds):
                        speeds[index] *= 1.2
                if event.key == pygame.K_s:
                    """клавиша s - уменьшение скорости движения линии"""
                    for index, _ in enumerate(speeds):
                        speeds[index] /= 1.2

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    """левая кнопка мыши - добавление точки"""
                    points.append(Vec2d(event.pos[0], event.pos[1]))
                    speeds.append(Vec2d(random.random() * 2,
                                        random.random() * 2))
                elif event.button == 3:
                    """правая кнопка мыши - удаление опорной точки"""
                    for i, _ in enumerate(points):
                        point = points[i].float_pair()
                        if event.pos[0] + 5 >= point[0] >= event.pos[0] - 5 and \
                                event.pos[1] + 5 >= point[1] >= event.pos[1] - 5:
                            del points[i]
                            del speeds[i]
                            break

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        polyline1 = Polyline(points, speeds)
        polyline1.draw_points(gameDisplay)
        knot = Knot(points, speeds=None)
        polyline1.points = knot.get_knot(steps)
        polyline1.draw_points(gameDisplay, "line", 3, color)
        polyline1.points = points
        if not pause:
            polyline1.set_points(SCREEN_DIM)
        if show_help:
            draw_help(steps)

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
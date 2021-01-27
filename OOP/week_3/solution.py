from abc import ABC, abstractmethod


class AbstractEffect(ABC, Hero):

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect, ABC):

    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_stats(self):
        return self.base.get_stats()


class AbstractNegative(AbstractEffect, ABC):

    def __init__(self, base):
        self.base = base

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_stats(self):
        return self.base.get_stats()


class Berserk(AbstractPositive):
    """
    Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7;
    уменьшает характеристики: Восприятие, Харизма, Интеллект на 3;
    количество единиц здоровья увеличивается на 50.
    """
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['HP'] += 50
        self.stats['Strength'] += 7
        self.stats['Endurance'] += 7
        self.stats['Agility'] += 7
        self.stats['Luck'] += 7
        self.stats['Perception'] -= 3
        self.stats['Charisma'] -= 3
        self.stats['Intelligence'] -= 3
        return self.stats.copy()

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append('Berserk')
        return self.positive_effects.copy()


class Blessing(AbstractPositive):
    """
    увеличивает все основные характеристики на 2.
    """
    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] += 2
        self.stats['Perception'] += 2
        self.stats['Endurance'] += 2
        self.stats['Charisma'] += 2
        self.stats['Intelligence'] += 2
        self.stats['Agility'] += 2
        self.stats['Luck'] += 2
        return self.stats.copy()

    def get_positive_effects(self):
        self.positive_effects = self.base.get_positive_effects()
        self.positive_effects.append('Blessing')
        return self.positive_effects.copy()


class Weakness(AbstractNegative):
    """
    уменьшает характеристики: Сила, Выносливость, Ловкость на 4.
    """

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] -= 4
        self.stats['Endurance'] -= 4
        self.stats['Agility'] -= 4
        return self.stats.copy()

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append('Weakness')
        return self.negative_effects.copy()


class EvilEye(AbstractNegative):
    """
    уменьшает  характеристику Удача на 10.
    """

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Luck'] -= 10
        return self.stats.copy()

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append('EvilEye')
        return self.negative_effects.copy()


class Curse(AbstractNegative):
    """
    уменьшает все основные характеристики на 2.
    """

    def get_stats(self):
        self.stats = self.base.get_stats()
        self.stats['Strength'] -= 2
        self.stats['Perception'] -= 2
        self.stats['Endurance'] -= 2
        self.stats['Charisma'] -= 2
        self.stats['Intelligence'] -= 2
        self.stats['Agility'] -= 2
        self.stats['Luck'] -= 2
        return self.stats.copy()

    def get_negative_effects(self):
        self.negative_effects = self.base.get_negative_effects()
        self.negative_effects.append('Curse')
        return self.negative_effects.copy()


# SOLUTION FROM TEACHER
# Объявим абстрактный декоратор
# class AbstractEffect(Hero, ABC):
#
#     def __init__(self, base):
#         self.base = base
#
#     @abstractmethod
#     def get_positive_effects(self):
#         return self.positive_effects
#
#     @abstractmethod
#     def get_negative_effects(self):
#         return self.negative_effects
#
#     @abstractmethod
#     def get_stats(self):
#         pass
#
#
# # В AbstractPositive будем возвращать список наложенных отрицательных эффектов без изменений, чтобы не определять данный метод во всех положительных эффектах
# class AbstractPositive(AbstractEffect):
#
#     def get_negative_effects(self):
#         return self.base.get_negative_effects()
#
#
# # Объявим несколько положительных эффектов
# class Berserk(AbstractPositive):
#
#     def get_stats(self):
#         # Получим характеристики базового объекта, модифицируем их и вернем
#         stats = self.base.get_stats()
#         stats["HP"] += 50
#         stats["Strength"] += 7
#         stats["Endurance"] += 7
#         stats["Agility"] += 7
#         stats["Luck"] += 7
#         stats["Perception"] -= 3
#         stats["Charisma"] -= 3
#         stats["Intelligence"] -= 3
#         return stats
#
#     def get_positive_effects(self):
#         # Модифицируем список эффектов, добавив в него новый эффект
#         return self.base.get_positive_effects() + ["Berserk"]
#
#
# class Blessing(AbstractPositive):
#
#     def get_stats(self):
#         stats = self.base.get_stats()
#         stats["Strength"] += 2
#         stats["Endurance"] += 2
#         stats["Agility"] += 2
#         stats["Luck"] += 2
#         stats["Perception"] += 2
#         stats["Charisma"] += 2
#         stats["Intelligence"] += 2
#         return stats
#
#     def get_positive_effects(self):
#         return self.base.get_positive_effects() + ["Blessing"]
#
#
# # Для отрицательных эффектов неизменным останется список положительных эффектов
# class AbstractNegative(AbstractEffect):
#
#     def get_positive_effects(self):
#         return self.base.get_positive_effects()
#
#
# # Аналогично положительным эффектам, объявим отрицательные
# class Weakness(AbstractNegative):
#
#     def get_stats(self):
#         stats = self.base.get_stats()
#         stats["Strength"] -= 4
#         stats["Endurance"] -= 4
#         stats["Agility"] -= 4
#         return stats
#
#     def get_negative_effects(self):
#         return self.base.get_negative_effects() + ["Weakness"]
#
#
# class Curse(AbstractNegative):
#
#     def get_stats(self):
#         stats = self.base.get_stats()
#         stats["Strength"] -= 2
#         stats["Endurance"] -= 2
#         stats["Agility"] -= 2
#         stats["Luck"] -= 2
#         stats["Perception"] -= 2
#         stats["Charisma"] -= 2
#         stats["Intelligence"] -= 2
#         return stats
#
#     def get_negative_effects(self):
#         return self.base.get_negative_effects() + ["Curse"]
#
#
# class EvilEye(AbstractNegative):
#
#     def get_stats(self):
#         stats = self.base.get_stats()
#         stats["Luck"] -= 10
#         return stats
#
#     def get_negative_effects(self):
#         return self.base.get_negative_effects() + ["EvilEye"]
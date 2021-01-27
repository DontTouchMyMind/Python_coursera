from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(ABC):

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):

    def __init__(self, base):
        self.base = base

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_stats(self):
        return self.base.get_stats()


class AbstractNegative(AbstractEffect):

    def __init__(self, base):
        self.base = base

    def get_positive_effects(self):
        return self.base.get_positive_effects()

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


if __name__ == '__main__':
    hero = Hero()
    print(hero.get_stats())
    print(hero.get_positive_effects())
    print(hero.get_negative_effects())
    print('# накладываем эффект')
    brs = Berserk(hero)
    print(brs.get_stats())
    print(brs.get_negative_effects())
    print(brs.get_positive_effects())
    print('*' * 10)
    print('# накладываем эффекты')
    brs2 = Berserk(brs)
    print(brs.get_stats())
    cur1 = Curse(brs2)

    print(cur1.get_stats())
    print(cur1.get_positive_effects())
    print(cur1.get_negative_effects())
    print('*' * 10)
    print('# снимаем эффект Berserk')
    cur1.base = brs
    print(cur1.get_stats())
    print(cur1.get_positive_effects())
    print(cur1.get_negative_effects())

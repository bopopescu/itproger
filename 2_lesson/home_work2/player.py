from variants import Variants
import random

random_variant = random.choice(list(Variants))


# Создаем класс Player по умолчинию будет случайный выбор из Variants
class Player(object):
    def __init__(self, name="bot_player", choice=random_variant):
        self.choice = choice
        self.name = name

    def whoWins(self, obj1, obj2):
        result = ""
        if obj1.choice == obj2.choice:
            result = "Ничья"
        elif obj1.choice == Variants.SCISSORS and obj2.choice == Variants.ROCK:
            result = ("Выиграл игрок по имени: ", obj2.name)
        elif obj1.choice == Variants.SCISSORS and obj2.choice == Variants.PAPER:
            result = ("Выиграл игрок по имени: ", obj1.name)
        elif obj1.choice == Variants.PAPER and obj2.choice == Variants.ROCK:
            result = ("Выиграл игрок по имени: ", obj1.name)
        elif obj1.choice == Variants.PAPER and obj2.choice == Variants.SCISSORS:
            result = ("Выиграл игрок по имени: ", obj2.name)
        elif obj1.choice == Variants.ROCK and obj2.choice == Variants.PAPER:
            result = ("Выиграл игрок по имени: ", obj2.name)
        elif obj1.choice == Variants.ROCK and obj2.choice == Variants.SCISSORS:
            result = ("Выиграл игрок по имени: ", obj1.name)
        return result

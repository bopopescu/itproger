# HomeTask2 - Rock, Paper, Scissors - Antonov Vitalii
import
from variants import Variants


# Создаем класс на основе Player
bot = Player()

alex = Player(Variants.SCISSORS, "Alex")

print(bot.whoWins(bot, alex))




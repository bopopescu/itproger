# HomeTask2 - Rock, Paper, Scissors - Antonov Vitalii
from player import Player
from variants import Variants


# Создаем класс на основе Player
bot = Player()
print("Выбор бота: ", bot.choice)

# Создаем игроков
alex = Player("Alex", Variants.PAPER)
vit = Player("Vitalii", Variants.ROCK)
nick = Player("Nick", Variants.SCISSORS)

print(bot.whoWins(bot, alex))
print(bot.whoWins(alex, vit))
print(vit.whoWins(vit, bot))
print(vit.whoWins(vit, alex))
print(vit.whoWins(vit, nick))

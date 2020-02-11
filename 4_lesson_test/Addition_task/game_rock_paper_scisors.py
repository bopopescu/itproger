user1 = input("Введите имя первого игрока: ")
user2 = input("Введите имя второго игрока: ")
user1_answer = input(user1 + ", вы хотите выбрать камень, ножницы или бумагу: ")
user2_answer = input(user2 + ", вы хотите выбрать камень, ножницы или бумагу: ")

def compare(u1, u2):
    if u1 == u2:
        print("Ничья!")
    elif u1 == 'rock':
        if u2 == "scissors":
            return "Камень выиграл"
        else:
            return "Бумага выиграла"
    elif u1 == "scissors":
        if u2 == "paper":
            return "Ножницы выиграли"
        else:
            return "Камень выиграл"
    elif u1 == "paper":
        if u2 == "rock":
            return "Бумага выиграла"
        else:
            return "Ножницы выиграли"
    else:
        return "Неверныый ввод! Необходимо ввести одно из: rock, paper или scissors"


print(compare(user1_answer, user2_answer))
import random

rand_num = random.randint(0, 20)
guess = True

while guess:
    user_num = int(input("Guess the number from 0 to 20: "))
    if user_num == rand_num:
        print("Вы угадали число. Ваше число {} = {} загаданому".format(user_num, rand_num))
        guess = False
    else:
        print("Вы не угадали. Повторите ввод!")
        if user_num < rand_num:
            print("Число что вы пытаетесь угадать больше")
        else:
            print("Число что вы пытаетесь угадать меньше")

print("rand = ", rand_num)
print("user_num = ", user_num)


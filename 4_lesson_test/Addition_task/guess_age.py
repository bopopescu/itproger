age = -1

while age <= 0:
    try:
        age = int(input("Введите ваш возраст: "))
    except ValueError:
        print("Вы ввели не возраст, введите ваш возраст.")

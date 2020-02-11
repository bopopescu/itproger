file = open("text.txt", "wt")
file.write("Привет")
file.close()

try:
    file = open("text.txt", "x")
except FileExistsError as e:
    print("Ошибка работы с файлом: ", e)
    print("Сработате открытие через 'a'.")
    file = open("text.txt", "a")
finally:
    file.close()


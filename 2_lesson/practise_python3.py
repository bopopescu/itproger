n = input("Введите число: ")
a = int(n) * 2
print(n + str(a))

# ------------------------------------------------------
num = 46
word = "string"
word = word * 5
print(num)
print(word)
# ------------------------------------------------------
a, b, c, d = 5, "F", "Привет", 90.2

CONST = 67

print(c)
# ------------------------------------------------------
user_in = int(input("Введите число: "))
n1 = round(user_in // 1000 % 10)
n2 = round(user_in // 100 % 10)
n3 = round(user_in // 10 % 10)
n4 = round(user_in % 10)

print(n1, ",", n2, ",", n3, ",", n4)

# ------------------------------------------------------
n = 136
print(136 // 7)

# -------------------------------------------------------

number = input("Enter the number: ")
try:
    number = int(number)
    if number > 0:
        print("Number {} is positive.".format(number))
    elif number < 0:
        print("Number {} is negative".format(number))
    elif number == 0:
        print("Your namuber is 0!")
except ValueError as e:
    print("You entered not a number: ", e)
else:
    print("You enter the number")

# --------------------------------------------------------------------
user_age = int(input("Enter the user age: "))
if user_age > 18:
    print("Вам уже все можно")
elif user_age == 18:
    print("Ура!Вам 18 лет")
else:
    print("Вы еще слишком молоды.")

# -------------------------------------------------------------------
pay = int("Введите убытки: ")
profit = int(input("Введите прибыль: "))

if pay > profit:
    res = pay - profit
    print("Ваши убытки составили: ", res)
elif profit > pay:
    res = profit - pay
    print("Ваша прибыль составила: ", res)
else:
    print("Нет ни прибыли не убытков")

# -----------------------------------------------------------------------------


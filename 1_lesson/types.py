word = 'string'
number = 7
float_num = 3.14  #
bool = True  # Boolean

print()

a = z = c = 10

print(a, z, c)

w, r, b = 12, 16, 123

print(w, r, b)

# Условные операторы

a = 0

if 10 < a < 50 and a > 0:
    print('a less than 50')
elif a < 0:
    print('work elif')
else:
    print('work else')

# 3.5
b = 20
number = 0 if a > 10 else 'number less than 10'
print(number)

# 4,1

list = [1, 123, 123, 312, 123]
list2 = [1, 1, 1, 1, 1, 1, 1, 11]
print(list)
list.append(22222)
print(list)

list.extend(list2)
print(list)
item = list.pop(0)
print(item)
print(list)

list.sort()
print(list)

list.reverse()
print(list)

list.remove(22222)
print(list)

print("list reverse: ", list[::-1])
print("every second number: ", list[::2])

# tuples mutable data types

cor = (123, 32, 3, 42, 4523, 42, 2, 2, 2, 3, 4, 55, 6)

new_set = set(cor)
print(new_set)
new_set.add("sdfsdf")
print(new_set)

new_frozen = frozenset(cor)
print(new_frozen)

# dictionary

diction = {1: 'e', 2: 'qwe', 3: 'qwerty', 'key': 'gff'}
print(diction[1])

list.clear()
print(list)

# loops

lst = [6, 8, 'else', True, False]
tpl = (1, 27, "Chicago", 3.14, 742)
i = 0
j = 0

while i < len(lst):
    if i % 2 == 0:
        i += 1
        continue
    print("Значение элемента под индесом {} = {}".format(i, lst[i]))
    i += 1

while j < len(tpl):
    print("Значение элемента индесом {} = {}".format(j, tpl[j]))
    j += 1

for item in "Hello world":
    if item == 'd':
        print("Letter 'd' was found")
        break

print('------------------------------------------')


# Def labda


def func(*args):
    print("Hello world")
    print(args)


func(1, 23, "231", 157)


def print_dict(**kwargs):
    for key, item in kwargs.items():
        print(key, ": ", item)


print_dict(long="Vitalii", short="sad", some=True, a=3.14)

print("-----------------------------------------------")

# Анонимные функции

mul = lambda a, x: a * x
add = lambda a, b, c: a + b + c
div = lambda d, e: d / e
sub = lambda x, y: x - y

print("Умножение", mul(2, 6))
print("Сумма: ", add(1, 2, 3))
print("Деление: ", div(49, 7))
print("Вычитание: ", sub(47,40))


# Work with file
print("----------------------------------")

some_str = input("Enter the text: ")
some_str += '\n'

file = open('data/text.txt', 'a')
file.write(some_str)
file.close()

file = open('data/text.txt', 'rt')
print(file.read(10))
for line in file:
    print(line)
file.close()


file2 = open('data/text2.txt', "w")
file2.write('Hello Duk1e\n Matrix has you')
file2.close()

# Исключения
print("--------------------")
try:
    print(int('dsawe'))
except ValueError as e:
    print("Извините такое действие не возможно: ", e)

a = int(input("1st number: "))

user_input_b = False

while user_input_b == False:
    try:
        b = int(input("2nd number: "))
        user_input_b = True
    except ValueError:
        print("Ошибка ввода.Введите число!")

print("Результат: ", a + b)




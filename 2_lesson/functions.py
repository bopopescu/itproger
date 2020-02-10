def maximum(list):
    max_value = list[0]
    for value in list:
        if value > max_value:
            max_value = value

    return max_value


list = [123, 23, 2, 32, 23, 1, 2, 34, 99, 5000]
print(maximum(list))


def right_print(years):
    if years == 1:
        return "{} год.".format(years)
    elif 1 < years < 5:
        return "{} года.".format(years)
    elif years >= 5:
        return "{} лет.".format(years)


print(right_print(4))


def ending(num, words):
    num = num % 100
    if num > 19:
        num = num % 10
    if num == 1:
        return words[0]
    elif num == 2 or num == 3 or num == 4:
        return words[1]
    else:
        return words[2]


arr = ["год", "года", "лет"]
print("23", ending(23, arr))
print("1", ending(1, arr))
print("18", ending(18, arr))
print("211", ending(211, arr))


def around(views):
    if views < 1000:
        print(views)
        return
    hundreds = views / 1000
    print((round(hundreds * 10) / 10.0), "K")


around(1223123)
around(1272)
around(222)


# -------------------------------------------------------------
def have_or_no(arr, element):
    for item in arr:
        if item == element:
            return True
    return False


arr = [123, 3, "Missipi", 23, 3.14, "fu3k"]
print(have_or_no(arr, 23))

# -------------------------------------------------------------
lst = [34, "sd", 56, 34.34]

for i, value in enumerate(lst):
    print("index: {} = {}".format(i, value))


# ------------------------------------------------------------
def count_distance(time, speed):
    distance = time * speed
    if distance == 1:
        return lambda: "Вы пойд"
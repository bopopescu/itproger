# task1
user_input = "itproger.com"
user_out = user_input.split('.')
print(user_out[-1])

# task2
in_string = input("Enter the string: ")
count = 0

for letter in in_string:
    count += 1

print("Дллина строки: {} = {} символов".format(in_string, count))

# reverse

def reverse(string):
    rev = ''
    i = 0
    while i == len(string) - 1:
        rev += string[-1 * i]
        i += 1
    return rev

reverse("Hello")

word = input("Enter the word: ")
rve = word[::-1]
print(rve)
if word == rve:
    print("polindrome")
else:
    print("not polindrome")

print((word + " ") * 3)
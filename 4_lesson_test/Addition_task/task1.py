def delitel_chisel(n):
    del_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            del_list.append(i)

    print(del_list)


n = int(input("Enter the number: "))
delitel_chisel(n)


def fib(count):
    fib_list = [1, 1]

    if count == 1:
        return fib_list[0]
    if count == 2:
        return fib_list
    if count > 2:
        for i in range(1, count + 1):
            # print(i)
            print("{})".format(i) + str(fib_list[i]))
            fib_list.append(fib_list[i-1] + fib_list[i])



count = int(input("Enter the count of Fib numbers: "))
fib(count)




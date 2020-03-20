from datetime import datetime


def check_time(arg):
    print(arg)
    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    return outer


@check_time('Check_time1')
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l

# Быстрее чем первая
@check_time('Check_time2')
def two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l


for i in range(10):
    print(i + 1, "------------------------------------------")
    one(10000)
    # print(l1)
    two(13000)
    # print(l2)

# print(l1)
# print(l2)
# l1 = check_time(one)(10)

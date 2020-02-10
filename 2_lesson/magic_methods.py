print(dir())
print(dir(int))

# number = 10
# number ** 2

#print(number + 5)
#print(number.__add__(10))
#print(dir(number))


class Some(object):
    name = "John"
    number = 20

    def __add__(self, other):
        print("Some " + other)

    def __init__(self):
        print("Init started")

    # def __new__(self):
    #    print("New object")
    #    self.__add__(self, "new")
    #    self.__init__(self)

    def __str__(self):
        return "Name: " + self.name

    def __ge__(self, x):
        if self.number >= x:
            return True
        else:
            return False

    def __delattr__(self, item):
        print("Delete object")


obj = Some()
obj + "sadasd"
print(obj >= 10)
print(dir(obj))


print("Some some some some")

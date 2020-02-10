some_var = "This this var from my_module"

def show_module_name():
    print("My_modules called")


def print_some(sting):
    print("Result:", sting)


def summ(*args):
    sum = 0
    for i in args:
        sum += i

    return sum



def main():
    pass


if __name__ == "__main__":
    main()
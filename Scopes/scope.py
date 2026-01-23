# print("Scopes")

username = "admin"


def func():
    username = "manager"
    print(username)


# print(username)
# func()


x = 99


def calculate(num):
    def performCalculation(x):
        return x**num

    return performCalculation


result = calculate(2)
print(result(3))


def make_greeter(say):
    def greeter(name):
        return say + " " + name

    return greeter


f = make_greeter("HI")
print(f("hamza"))

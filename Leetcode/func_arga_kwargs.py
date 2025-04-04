
# *args exmaple

def fun(*args):
    return sum(args)

print(fun(1, 2, 3, 4))

# **kwargs example

# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)

def fun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Argument *argv :", arg)



fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

l = (1, 2)
print(type(l))

dict = { 1: 1, 2: 2}
fun(dict)

def functl(**kwargs):
    for k, v in kwargs.items():
        print("%s == %s" % (k, v))

functl(s1='Geeks', s2='for', s3='Geeks')

def fun1(arg1, **kwargs):
    print("first parameters: ", arg1)
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))

fun1("Hi", s1='Geeks', s2='for', s3='Geeks')


def fun2(*args, **kwargs):
    print("Positional arguments:", args)
    print("keyword arguments:", kwargs)

fun2(1, 2, 3, 6, a=4, b=5)


# Decorators
#why should you use deccortator?

def hello():
    print("hello world")

def greet(fx):
    print("Good Morning")

hello()


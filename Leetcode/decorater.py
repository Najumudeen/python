def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

def greet_with_argument(fx):
    def mfx(*args, **kwargs):
        print(f"Calling function {fx.__name__} with args={args}, kwargs={kwargs}")
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World")

hello()

@greet_with_argument
def add(a, b, c = None):
    print( a + b)

add(3, 4, c = 2)
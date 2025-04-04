class Vecotr:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vecotr(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"
    
    def __call__(self):
        print("Hello, I was called")

    
v1 = Vecotr(10, 20)
v2 = Vecotr(50, 60)

v3 = v1 + v2

v3()
# print(v3)
# print(v3.x)
# print(v3.y)
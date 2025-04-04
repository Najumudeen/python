# for _ in range(10):
#     print("Hi")

class Test3:
    def __init__(self):
        self.bar = 1
        self._bar = 2
        self.__bar = 3

t = Test3()
print(t.bar)
print(t._bar)
#print(t.__bar) # you can not call __bar variable out the class directly.

# call the __bar variable in the following way
print(t._Test3__bar)

######

class AddItems:
    def __init__(self, iterable):
        self.items = []
        self.update(iterable)
        
    def update(self, iterable):
        for i in iterable:
            self.items.append(i)
    
    def display(self):
        print(*self.items)

a = AddItems([1, 2, 3])

a.display()

#dir(AddItems)
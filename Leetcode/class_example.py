# Public Modifiers


class A:
    def __init__(self):
        self.name = "Najumudeen"
        self.grade = "A"
    
class B(A):
    def __init__(self):
        super().__init__()
        self.address = 'XYZ'

    def PrintDetails(self):
        print(f"{self.name}, {self.grade}, {self.address}")


b = B()

b.PrintDetails()

print(A().name)
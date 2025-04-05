def strip_function():
    ''' strip() method Trims leading and trailing spaces '''
    example = ",Python,,"
    print(example.strip(','))

def type_method():
    ''' type() method '''
    var = "123"
    print(type(var))

def insert_method():
    ''' insert() is mainly used to add an item at a specific index in a list '''
    list = [ 1, 2, 4]
    list.insert(2, 3)
    print(list)

def append_method():
    ''' Lists in Python are mutable and assigning y = x doesn't create a copy but rather a reference. 
    Changing y also changes x '''
    x = [ 1, 2, 3 ]
    y = x
    x.append(4)
    print(y)

def pass_method():
    ''' pass statement is used in Python as a place holder for future code.'''
    pass

def python_tips():
    string = '''
        Non-empty string in Python are considered truthy values.
        Function readline() reads a single line from the file where the file pointer is current located and moves the file pointer.
        Combine two lists in python use extend() method. 
        A tuple is a collection which is ordered and immutable, meaning it's content can't be changed once it is created.
'''
    
    lines = string.splitlines()
    stripedlines = [ line.lstrip() for line in lines ]
    result = "\n".join(stripedlines)
    print(result)

import functools
#@functools.lru_cache(maxsize=128)
def fib_func_cache(number):
    if number <= 1:
        return number
    return fib_func_cache(number-1) + fib_func_cache(number-2)


def break_keyword_func():
    ''' Break Tergit statuminates the loop immediately '''
    for num in range(5):
        if num == 3:
            print("Iteration reached number 3. So Breaking the loops .....")
            break

def isdigit_method():
    print("Python3.8".isdigit())

def string_method():
    ''' String method '''
    import string
    import random
    char_pool = string.ascii_letters + string.ascii_uppercase + string.digits
    print(''.join(random.sample(char_pool, 6)))

def main():
    strip_function()
    type_method()
    insert_method()
    pass_method()
    python_tips()
    print(fib_func_cache(6))
    break_keyword_func()
    isdigit_method()
    string_method()

if __name__ == "__main__":
    main()
    
    

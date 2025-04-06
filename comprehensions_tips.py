
options = ["any", "albany", "apple", "world", "hello", "acy"]
matrix = [[1,2,3], [4,5,6], [7,8,9], "naju"]


def append_method():
    values = []
    for i in range(10):
        values.append(i)
    print(values)

def append_list_comprehension():
    values = [ x + 1 for x in range(10) ]
    print(values)

def get_even_numbers():
    
    evens = []
    for number in range(50):
        is_even = number % 2 == 0
        if number == 0:
            continue
        elif is_even:
            evens.append(number)

def even_numbers_list_comprehension():
    evens = [ number for number in range(50) if number % 2 == 0 ]
    print(evens)


def find_string_match():
    ''' Strings that start with "a" and end in "y" '''
    valid_strings = []
    for string in options:
        if len(string) <= 1:
            continue
        elif string[0] != "a":
            continue
        elif string[-1] != "y":
            continue
        else:
            valid_strings.append(string)
    print(valid_strings)

def find_string_match_list_comprehesntion():

    valid_string = [
        string
        for string in options
        if len(string) >= 2
        if string[0] == "a"
        if string[-1] == "y"
    ]
    print(valid_string)

def nested_list():
    ''' Flattening a mstrix (list of lists) 2 Dimenstion '''
    flattened = []
    for row in matrix:
        for num in row:
            flattened.append(num)
    print(flattened)

def nested_list_comprehesntion():
    flattened = [ num for row in matrix for num in row ]
    print(flattened)


def add_function(x,y):
    return x + y

def lambda_function():
    ''' Change the above function to lambda function
        Lambda function donn't requirted return keyword '''
    add = lambda x, y: x + y
    print(add_function(5, 7))
    print((lambda x, y: x + y)(5,7))

def multiply_function(x):
    return x * 2

sequence = [ 1, 3, 5, 9 ]

def lambda_list_comprehention():
    doubled = [ multiply_function(x) for x in sequence ]
    doubled = [ multiply_function(x) for x in sequence ]

    ''' We can use map function '''
    doubled = map(multiply_function, sequence)

    ''' if want to use lambda function '''
    doubled = list(map(lambda x: x * 2, sequence))

    print(doubled)

def dictionary_comprehension():
    users = [
        (0, "Bob", "password"),
        (1, "Rolf", "bob123"),
        (2, "Jose", "longp4assword"),
        (3, "username", "1234")
    ]

    username_mapping = { user[1]: user for user in users }
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    _, username, password = username_mapping[username_input]

    print(username)
    print(password)

    if password_input == password:
        print("Your details are correct!.")
    else:
        print("Your details are incorrect.")
        

def multiply(*args):
    print(args)
    total = 1  
    for arg in args:
        total *= arg
    return total

def add(x, y):
    return x + y

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

def main():
    append_method()
    append_list_comprehension()
    get_even_numbers()
    even_numbers_list_comprehension()
    print(multiply(1, 3, 5))
    print(apply(1, 3, 6, 7, operator="*"))
    #nums = [ 3, 5, 6 ]
    nums = { "x": 15, "y": 25 }
    add(**nums)
    find_string_match()
    find_string_match_list_comprehesntion()
    nested_list_comprehesntion()
    lambda_list_comprehention()
    lambda_function()
    dictionary_comprehension()


if __name__ == "__main__":
    main()

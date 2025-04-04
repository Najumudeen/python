class Employee:

    # initializing 

    def __init__(self):
        print("Employee Created")
    
    def __del__(self):
        print("Destructor called")


def Create_onj():
    print('Making object ...')
    obj = Employee()
    print('Function End')
    return obj

print('Calling Create_obj() function ...')
obj = Create_onj()
print('Program End ...')

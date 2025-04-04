import time
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'clear')

for i in range(0,20):
    print('\n\n\n')
    print(' ' * i + '.')
    time.sleep(0.1)
    clear()
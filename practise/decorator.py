
import time
import sys

def timer(func):
    def wrapper(*args, **kargs):
        t1 = time.time()
        result = func(*args, **kargs)
        t2 = time.time()
        print(f"Function {func.__name__!r} executed in {(t2 - t1):.4f}s")
        return result
    return wrapper

@timer
def welcome():
    print("Naju is learning python")

@timer
def long_time(n): 
    # for i in range(n): 
    #     for j in range(100000): 
    #         i*j 
    value = [
        i * j 
        for i in range(n)
        for j in range(100000) 
        ]
    
    return value


if __name__ == "__main__":
    
    t = len(sys.argv)
    # print(t)
    # print(type(t))
    # print(sys.argv[1])

    if t <= 2:
        welcome()
        long_time(int(sys.argv[1]))
    else:
        sys.exit("More than one input parameters Provided")

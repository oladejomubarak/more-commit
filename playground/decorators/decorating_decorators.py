import functools
import time


def decorate(func):
    @functools.wraps(func)   #to make function get back its attributes
    def wrap(*arg, **kwargs):
        print("I am a before decorator")
        #print(func(*arg, **kwargs))
        f = func(*arg, **kwargs)
        print("I am after decorator")
# *args and **kwargs allow for passing prameter of different lenght and type
        return f

    return wrap

def performance_counter(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"the function {f.__name__} took {end - start}to run")
        return func
    return wrapper
@decorate
def hello(name):
    return f"Hello {name}"
    #return "Hello world"
@performance_counter
@decorate
def add(x, y):
    """
    adds two numbers
    """
    return x + y

# hello = decorate(hello)
#hello("Banke")
#add(2, 3)
print(hello("Banke"))
print(add(2, 3))
print(add.__name__)
print(add.__doc__)

def multiply(a,b):
    return a*b
multiply_by_5 = functools.partial(multiply, 5)

print(multiply_by_5(6))
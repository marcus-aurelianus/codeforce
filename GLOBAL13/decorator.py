
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args)
        print(func.__name__,'has been called')
        return result
    return wrapper
#add = log(add)
  
@log
def add(x, y):
    result = x+y
    return result

if __name__ == '__main__':
    print(add(1,2))
    print(add.__name__)

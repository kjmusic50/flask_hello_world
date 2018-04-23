import functools

"""def twist(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print("Shep Schwab shopped at Scott's Schnapps shop")
        function(*args, **kwargs)
    return wrapper
"""
def twist(twister):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print(twister)
            function(*args, **kwargs)
            print(twister)
        return wrapper
    return decorator
    
@twist("She sells sea shells on the sea shore")
def spoon():
    print("A well-boiled icicle")
    

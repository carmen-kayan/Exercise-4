from time import time

def my_func(a):
    return a * 3



def do_them_all(some_iterable):
    """ Do something all the time.


    This is an amazing docstring.

    
    """
    output = []
    for elem in some_iterable:
        output.append(my_func(elem))
    print(time())
    return output
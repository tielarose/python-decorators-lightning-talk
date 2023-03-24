#########################################
# EXAMPLE V1
#########################################

def print_hi():
    print(f'Hi!')


def ex_decorator(func):
    def wrapper():
        print('This happens before')
        func()
        print('This happens after')
    return wrapper


# reassign the function using the decorator
print_hi = ex_decorator(print_hi)

#########################################
# EXAMPLE V2
#########################################


def ex_decorator(func):
    def wrapper():
        print('This happens before')
        func()
        print('This happens after')
    return wrapper


@ex_decorator
def print_hi():
    print(f'Hi!')

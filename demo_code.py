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


# def ex_decorator(func):
#     def wrapper():
#         print('This happens before')
#         func()
#         print('This happens after')
#     return wrapper


# @ex_decorator
# def print_hi():
#     print(f'Hi!')

#########################################
# EXAMPLE V3
#########################################


def ex_decorator(func):
    def wrapper(*args, **kwargs):
        print('This happens before')
        func(*args, **kwargs)
        print('This happens after')
    return wrapper


@ex_decorator
def greet_someone(name):
    print(f'Hi!, {name}!')


@ex_decorator
def greet_two_people(name1, name2):
    print(f'Hi, {name1} and {name2}!')

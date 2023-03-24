#########################################
# EXAMPLE V1
#########################################

# def print_hi():
#     print(f'Hi!')


# def ex_decorator(func):
#     def wrapper():
#         print('This happens before')
#         func()
#         print('This happens after')
#     return wrapper


# # reassign the function using the decorator
# print_hi = ex_decorator(print_hi)

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


# def ex_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('This happens before')
#         func(*args, **kwargs)
#         print('This happens after')
#     return wrapper


# @ex_decorator
# def greet_someone(name):
#     print(f'Hi!, {name}!')


# @ex_decorator
# def greet_two_people(name1, name2):
#     print(f'Hi, {name1} and {name2}!')

#########################################
# EXAMPLE V4
#########################################


# def ex_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('This happens before')
#         the_function = func(*args, **kwargs)
#         print('This happens after')
#         return the_function
#     return wrapper


# @ex_decorator
# def return_a_greeting(name):
#     print('The greeting was created!')
#     return f'Hi, {name}!'

#########################################
# EXAMPLE V5
#########################################

# import functools


# def ex_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('This happens before')
#         the_function = func(*args, **kwargs)
#         print('This happens after')
#         return the_function
#     return wrapper


# @ex_decorator
# def return_a_greeting(name):
#     print('The greeting was created!')
#     return f'Hi, {name}!'

#########################################
# EXAMPLE V6
#########################################

import functools


def ex_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Something happens before the function
        the_function = func(*args, **kwargs)
        # Something happens after the function
        return the_function
    return wrapper

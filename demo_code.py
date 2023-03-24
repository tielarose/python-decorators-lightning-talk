#########################################
# EXAMPLE 1
#########################################

def print_hi():
    print(f'Hi!')


def ex_decorator(func):
    def wrapper():
        print('This happens before')
        func()
        print('This happens after')
    return wrapper

# # without the decorator
# print_hi()
# # prints 'Hi'

# # reassign the function using the decorator
# print_hi = ex_decorator(print_hi)

# # now when I call print_hi, it is wrapped in the decorator
# print_hi()
# # prints 'This happens before'
# # prints 'Hi
# # prints 'This happens after'

#########################################
# EXAMPLE 2
#########################################

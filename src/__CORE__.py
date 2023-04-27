# IMPORTS
from functools import reduce
import re


# VARIABLES
operations = {
    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b,
    '*': lambda a,b: a * b,
    '/': lambda a,b: a / b
}


# FUNCTIONS
def tokenize(arg:str):
    tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', arg)
    return tokens

# ----------------------------------------------------------------------------------------

def number_convert(tokens):
    for i in range(len(tokens)):
        if tokens[i][0] in '0123456789':
            tokens[i] = int(tokens[i])
    
# ----------------------------------------------------------------------------------------

def get_answer(operator:str, numbers:list):
    numbers = [int(i) for i in numbers]
    return reduce(operations[operator], numbers)

# ----------------------------------------------------------------------------------------

def evaluate(tokens:list[str]):
    stack = []
    for i in tokens:
        if i.isdigit():
            stack.append(i)

        elif i in ['+', '-', '*', '/', '(']:
            stack.append(i)

        elif i == ')':
            nums = []
            c = stack.pop()
            while c not in ['+', '-', '*', '/', '(']:
                nums.insert(0, c)
                c = stack.pop()
            stack.pop()
            stack.append(get_answer(c, nums))

    return stack[0]
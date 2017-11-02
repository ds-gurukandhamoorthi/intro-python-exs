import sys
from strutils import words
from LinkedStack import LinkedStack
from operator import add, mul, sub
from math import sqrt


def evaluate(string):
    operand_stack = LinkedStack()
    operator_stack = LinkedStack()
    tokens = (tok.strip() for tok in words(string))
    for tok in tokens:
        # print(tok)
        # print(operator_stack)
        # print(operand_stack)
        # print(tokens)
        if tok == '(':
            continue
        if is_operator(tok):
            operator_stack.push(tok)
        elif tok == ')':
            evaluate_single(operand_stack, operator_stack)
        else:
            operand_stack.push(float(tok))
    print(operand_stack)


def is_operator(token):
    return token in ('+', '-', '*', 'sqrt')

def get_builtin(operator):
    dic = {'+': add, '-': sub, '*': mul}
    return dic.get(operator, None)


def nb_operands(operator):
    if operator in ('sqrt',):  # unary operators
        return 1
    return 2

def evaluate_single(operand_stack, operator_stack):
    operator = operator_stack.pop()
    nb = nb_operands(operator)
    operands = [operand_stack.pop() for i in range(nb)]
    builtin = get_builtin(operator)
    if builtin is None:
        if operator == 'sqrt':
            res = sqrt(operands[0])
    else:
        print(operands)
        res = builtin(*operands)
    operand_stack.push(res)


def main():
    filename = sys.argv[1]
    with open(filename) as inp:
        exp = inp.read().split('\n')[0]
        evaluate(exp)


if __name__ == "__main__":
    main()

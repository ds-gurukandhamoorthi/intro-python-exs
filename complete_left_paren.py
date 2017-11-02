from strutils import words
from LinkedStack import LinkedStack


def evaluate(string):
    operand_stack = LinkedStack()
    operator_stack = LinkedStack()
    tokens = (tok.strip() for tok in words(string))
    for tok in tokens:
        if is_operator(tok):
            operator_stack.push(tok)
        elif tok == ')':
            evaluate_single(operand_stack, operator_stack)
        else:
            operand_stack.push(tok)
    print(operand_stack)


def is_operator(token):
    return token in ('+', '-', '*')


def evaluate_single(operand_stack, operator_stack):
    b, a = [operand_stack.pop(), operand_stack.pop()]
    op = operator_stack.pop()
    res = '( ' + ' '. join((a, op, b)) + ' )'
    operand_stack.push(res)


def main():
    exp = '1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )'
    evaluate(exp)


if __name__ == "__main__":
    main()

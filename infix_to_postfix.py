from strutils import words
from LinkedStack import LinkedStack


def infix_to_postfix(string):
    operand_stack = LinkedStack()
    operator_stack = LinkedStack()
    tokens = (tok.strip() for tok in words(string))
    for tok in tokens:
        print(operator_stack)
        print(operand_stack)
        if tok == '(':
            continue
            # operand_stack.push(tok)
        elif is_operator(tok):
            operator_stack.push(tok)
        elif tok == ')':
            b, a = operand_stack.pop(), operand_stack.pop()
            op = operator_stack.pop()
            # res = '[' + a + ' ' + b +  op + ']'
            res = a + ' ' + b + ' ' + op
            operand_stack.push(res)
        else:
            operand_stack.push(tok)
    print(operand_stack)


def is_operator(token):
    return token in ('+', '-', '*')


def main():
    #exp = '( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) )'
    #FIXME : not functioning for the expression above
    exp = '( ( 1 + 2 ) * ( 3 + 4 ) )'
    infix_to_postfix(exp)


if __name__ == "__main__":
    main()

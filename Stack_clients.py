from LinkedStack import LinkedStack


def print_reverse(array):
    s = LinkedStack()
    for val in array:
        s.push(val)
    for val in s:
        print(val)

def balanced_parentheses(string):
    def start(paren):
        dic = {']':'[', ')':'(', '}':'{'}
        return dic.get(paren, None)
    prev_parens = LinkedStack()
    for ch in string:
        print(prev_parens)
        if ch in '[({':
            prev_parens.push(ch)
        elif ch in '])}':
            p = prev_parens.pop()
            if p != start(ch):
                return False
    return not prev_parens



def main():
    print_reverse(['guru', 'kandha', 'moorthi'])
    print(balanced_parentheses('[()]{}{[()()]()}'))


if __name__ == '__main__':
    main()

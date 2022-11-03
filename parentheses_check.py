# Task: https://ibb.co/3hJTZ5Y

from collections import deque


def parentheses_check(str_to_check: str):
    open_brackets = deque()
    for bracket in str_to_check:
        if bracket in parentheses.keys() or bracket in parentheses.values():    # omission of non brackets
            if bracket in parentheses.keys():
                open_brackets.append(bracket)
            else:
                try:
                    if bracket != parentheses.get(open_brackets.pop()):
                        return False
                except IndexError:
                    return False
    if not open_brackets:
        return True
    else:
        return False


if __name__ == '__main__':
    parentheses = {'[': ']', '(': ')', '{': '}'}
    while True:
        try:
            print(parentheses_check(input()))
        except EOFError:  # Press Ctrl+D/Cmd+D or Ctrl+Z to finish input
            break

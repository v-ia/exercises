# Task: https://ibb.co/3hJTZ5Y

from collections import deque


def parentheses_check(str_to_check: str):
    parentheses = {'[': ']', '(': ')', '{': '}'}
    open_brackets = deque()
    for bracket in str_to_check:
        if bracket in parentheses or bracket in parentheses.values():    # omission of not brackets
            if bracket in parentheses.keys():
                open_brackets.append(bracket)
            else:
                try:
                    if bracket != parentheses.get(open_brackets.pop()):
                        return False
                except IndexError:
                    return False
    return not open_brackets


if __name__ == '__main__':
    while True:
        try:
            print(parentheses_check(input()))
        except EOFError:  # Press Ctrl+D/Cmd+D or Ctrl+Z to finish input
            break

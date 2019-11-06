#!/usr/bin/env python 3

def calculate(arg):
    stack = list()
    for token in arg.split():
        if token == '+':
                arg1 = stack.pop()
                arg2 = stack.pop()
                result = arg1 + arg2
                stack.append(result)

        elif token == '-':
                arg1 = stack.pop()
                arg2 = stack.pop()
                result = arg1 - arg2
                stack.append(result)
        elif token == '*':
                arg1 = stack.pop()
                arg2 = stack.pop()
                result = arg1 * arg2
                stack.append(result)
        else:
                stack.append(int(token))

        print(stack)

def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ =='__main__': #Note: that's underscore n a m e ...
    main()

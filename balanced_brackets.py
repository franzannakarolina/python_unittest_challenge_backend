#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    # Write your code here
    stack = []
    for i in brackets:
        if i == '{' or i == '[' or i == '(':
            stack.append(i)
        elif i == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return 'NO'
        elif i == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return 'NO'
        elif i == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')

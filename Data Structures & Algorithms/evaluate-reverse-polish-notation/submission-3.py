from collections import deque
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        if integer, push to stack
        if operator, pop two items, evaluate expression, then push result into stack

        last element in stack is final evaluation
        """

        stack = deque()
        operators = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : operator.truediv,
        }

        if len(tokens) <= 2:
            return int(tokens[0])

        for token in tokens:
            if token not in operators:
                stack.append(token)
                continue

            int1 = int(stack.pop())
            int2 = int(stack.pop())
            res = int(operators[token](int2, int1))

            stack.append(res)

        return stack[-1]

            
            


import operator

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
            }
        tokens_stack = []
        for token in tokens:
            if token not in ops:
                tokens_stack.append(int(token))
            else:
                val1 = int(tokens_stack.pop())
                val2 = int(tokens_stack.pop())
                result = ops[token](val2, val1)
                tokens_stack.append(result)
        return tokens_stack.pop()
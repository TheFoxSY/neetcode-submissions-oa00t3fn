class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                second, first = stack.pop(), stack.pop()
                stack.append(first + second)
            elif c == '-':
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif c == '*':
                second, first = stack.pop(), stack.pop()
                stack.append(first * second)
            elif c == '/':
                second, first = stack.pop(), stack.pop()
                stack.append(int(float(first) / float(second)))
            else:
                stack.append(int(c))
        
        return stack[-1]
            

        
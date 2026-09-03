class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        arithmetic_expression = ["+", "-", "*", "/"]

        for token in tokens:

            if token == "+":
                num1 = stack[-2]
                num2 = stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(num1 + num2))
            
            elif token == "-":
                num1 = stack[-2]
                num2 = stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(num1 - num2))

            elif token == "*":
                num1 = stack[-2]
                num2 = stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(num1 * num2))

            elif token == "/":
                num1 = stack[-2]
                num2 = stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(num1 / num2))
            
            else:
                stack.append(int(token))
        
        return stack[-1]

                

        
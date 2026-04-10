class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for element in tokens :

            if element not in '/*+-':
                stack.append(int(element))
            else:
                right = stack.pop()
                left = stack.pop()
            
                match(element):
                    case '+':
                        stack.append(left+right)
                    case '-':
                        stack.append(left-right)
                    case '*':
                        stack.append(left*right)
                    case '/':
                        stack.append(int(left/right))

        return stack.pop()    
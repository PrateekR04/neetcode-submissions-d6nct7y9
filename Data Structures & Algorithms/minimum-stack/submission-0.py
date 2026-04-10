class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []


    def push(self, val: int) -> None:
        self.stack.append(val)

        # Push to minStack if it's empty or val is smaller/equal
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()

            # If popped value is the current minimum, remove it from minStack
            if val == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

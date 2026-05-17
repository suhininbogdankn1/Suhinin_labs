class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

stack = Stack()
stack.push(22)
stack.push(33)
stack.push(44)
stack.push(11)

def stack_size(stack):
    tempstack = Stack()
    stack_size = 0
    while not stack.is_empty():
        item = stack.pop()
        tempstack.push(item)
        stack_size += 1
    while not tempstack.is_empty():
        stack.push(tempstack.pop())
    return stack_size
print(stack_size(stack))


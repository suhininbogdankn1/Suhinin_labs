class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

def rpn_calculator(expression):
    stack = Stack()
    tokens = expression.split()
    for i in tokens:
        if i not in ["+","-","/","*"]:
            stack.push(int(i))
        elif i in ["+","-","/","*"]:
            ll = stack.pop()
            l = stack.pop()
            if i == "+":
                stack.push(l+ll)
            elif i == "-":
                stack.push(l-ll)
            elif i == "*":
                stack.push(l*ll)
            elif i == "/":
                stack.push(int(l/ll))
    return stack.pop()
print(rpn_calculator(input("")))

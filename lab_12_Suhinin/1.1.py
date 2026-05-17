text = input("Введіть текст: ")

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

def reversed_string(text):
    stack = Stack()
    for char in text:
        stack.push(char)
    reversed_text = ""
    while not stack.is_empty():
        reversed_text += stack.pop()
    return reversed_text
print(reversed_string(text))

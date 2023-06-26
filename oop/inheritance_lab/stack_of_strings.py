class Stack:
    def __init__(self, data: list):
        self.data = list(data)

    def push(self, element):
        self.data.append(element)

    def pop(self):
        self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if self.data else False


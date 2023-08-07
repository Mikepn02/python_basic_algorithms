class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Cannot pop from an empty stack"
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"
    def size(self):
        return len(self.items)
    


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack size:", stack.size())  # Output: 3

print("Peek:", stack.peek())  # Output: 30

print("Pop:", stack.pop())  # Output: 30

print("Stack size:", stack.size())  # Output: 2

# A stack is a fundamental data structure that provides a simple and efficient way to manage elements following the Last In First Out (LIFO) principle. It's commonly used in various algorithms, programming languages, and applications.


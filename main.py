class Node:
    def __init__(self, data):
        self.data = data
        self.before = None

class Stack:
    def __init__(self):
        self.pointer = None

    def isEmpty(self):
        if self.pointer is None:
            return True
        else:
            return False
        
    def pop(self):
        if self.pointer is None:
            print('Empty stack.')
            return
        elif self.pointer.before is None:
            self.pointer = None
            return
        self.pointer = self.pointer.before

    def push(self, data):
        node = Node(data)
        node.before = self.pointer
        self.pointer = node
    
    def print(self):
        if self.pointer is None:
            print('Empty stack.')
            return
        node = self.pointer
        while node.before is not None:
            print(node.data, end=" ")
            node = node.before
        print(node.data, end="")

def result(toTransfer):
    result = Stack()
    while not toTransfer.isEmpty():
        result.push(toTransfer.pointer.data)
        toTransfer.pop()
        result.print()

list = input().split()
left = Stack()
right = Stack()
temp = Stack()

while not right.isEmpty():
    temp.push(right.pointer.data)
    left.pop()

left = temp

for i in list:
    if int(i) < 0:
        right.push(int(i))
    else:
        left.push(int(i))

while (not left.isEmpty()) and (not right.isEmpty()):
    r1 = left.pointer.data
    r2 = abs(right.pointer.data)
    if r1 > r2:
        right.pop()
    elif r2 > r1:
        left.pop()
    else: 
        left.pop()
        right.pop()

if left.isEmpty() and not right.isEmpty():
    result(right)
elif right.isEmpty and not left.isEmpty():
    result(left)
else:
    print('No quedaron robots!', end="")



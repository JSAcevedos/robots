class Node:
    def __init__(self, data):
        self.data = data
        self.before = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def pop(self):
        if self.isEmpty():
            print('Empty stack')
        else:
            temp = self.head.data
            self.head = self.head.before
            return temp
    
    def push(self, data):
        node = Node(data)
        node.before = self.head
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Empty stack")
        else:
            current_node = self.head
            while current_node is not None:
                if current_node.before is None:
                    print(current_node.data, end="")
                else:
                    print(current_node.data, end=" ")
                current_node = current_node.before

data = input().split()
left = Stack()
right = Stack() 
result = Stack()
temp = Stack()

for i in data:
    result.push(int(i))

while not result.isEmpty():
    if result.head.data > 0:
        temp.push(result.pop())
    elif result.head.data < 0:
        right.push(result.pop())

while not temp.isEmpty():
        left.push(temp.pop())

while not left.isEmpty() and not right.isEmpty():
    if left.head.data > abs(right.head.data):
        right.pop()
    elif left.head.data < abs(right.head.data):
        left.pop()
    else:
        left.pop()
        right.pop()

if left.isEmpty() and not right.isEmpty():
    right.print()
elif right.isEmpty() and not left.isEmpty():
    while not left.isEmpty():
        right.push(left.pop())
    right.print()
else:
    print("No quedaron robots!", end="")
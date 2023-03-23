
def printArray(array):
    for i in array:
        if i == array[-1]:
            print(i, end="")
        else:
            print(i, end=" ")

list = input().split()
left = []
right = []

for i in list:
    if int(i) > 0:
        left.append(int(i))
    elif int(i) < 0:
        right.append(int(i))

while len(left) != 0 and len(right) != 0:
    if left[-1] > abs(right[0]):
        right.pop(0)
    elif left[-1] < abs(right[0]):
        left.pop()
    else:
        right.pop(0)
        left.pop()

if len(left) == 0 and len(right) != 0:
    printArray(right)
elif len(left) != 0 and len(right) == 0: 
    printArray(left)
else:
    print("No quedaron robots!", end="")


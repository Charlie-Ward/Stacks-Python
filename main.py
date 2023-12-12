max = 3  # Make one less then the actual max
top = -1
stack = []


def isEmpty():
    if top == -1:
        return True
    else:
        return False


def isFull():
    if top == max:
        return True
    else:
        return False


def push(item):
    global top
    if isFull():
        print("Stack is full")
    else:
        top += 1
        stack.append(item)


def peek():
    global top
    if isEmpty():
        print("Stack is empty")
    else:
        print(stack[top])


def pop():
    global top
    if isEmpty():
        print("Stack is empty")
    else:
        print(stack[top])
        stack.pop(top)
        top -= 1


def report():
    print("Stack Report")
    print(f'Stack max size: {max + 1}')
    print(f'Stack current size: {top + 1}')
    print(f'Stack current values: {stack}')


print(isEmpty())
push("Strawberry")
push("Lemons")
push("Apples")
push("Pears")
push("Lime")
report()
pop()
push("Lime")
print(isFull())
report()
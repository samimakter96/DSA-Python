stack = []


def push():
    if len(stack) == n:
        print("Stack overflow")
    else:
        element = input("Enter the element: ")
        stack.append(element)
        print("Stack:", stack)


def pop_element():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        popped_element = stack.pop()
        print("Removed element:", popped_element)
        print("Stack:", stack)


n = int(input("Limit of the stack: "))

while True:
    print("Select the operation: 1. Push 2. Pop 3. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct option")

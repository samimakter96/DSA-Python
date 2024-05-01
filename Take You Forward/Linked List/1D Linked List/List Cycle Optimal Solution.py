# Optimal Solution: First and Slow / Tortoise-Hare-Approach
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# utility function to insert node at the end of the linked list
def insertNode(head, val):
    newNode = Node(val)
    if head == None:
        head = newNode
        return head
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode
    return head


# utility function to create cycle
def createCycle(head, pos):
    temp = head
    ptr = head
    cnt = 0
    while temp.next != None:
        if cnt != pos:
            ptr = ptr.next
            cnt += 1
        temp = temp.next
    temp.next = ptr


# process as per mentioned in solution

def detectCycle(head):
    if head == None or head.next == None:
        return None
    slow = head
    first = head

    # step 1: detecting a loop
    while first != None and first.next != None:
        slow = slow.next
        first = first.next.next
        if slow == first:

            # step 2: finding starting point
            slow = head
            while slow != first:
                slow = slow.next
                first = first.next
            return slow
    return None


if __name__ == "__main__":
    head = None
    head = insertNode(head, 1)
    head = insertNode(head, 2)
    head = insertNode(head, 3)
    head = insertNode(head, 4)
    head = insertNode(head, 3)
    head = insertNode(head, 6)
    head = insertNode(head, 10)
    createCycle(head, 2)
    nodeRecieve = detectCycle(head)
    if nodeRecieve == None:
        print("No cycle")
    else:
        temp = head
        pos = 0
        while temp != nodeRecieve:
            pos += 1
            temp = temp.next
        print("Tail connects at pos", pos)

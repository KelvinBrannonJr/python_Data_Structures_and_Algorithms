class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None

        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


# Stack object instantiation
print("Stack Objects")
my_stack = Stack(7)
my_stack.push(23)
my_stack.print_stack()


# Queue object instantiation
print("Queue Objects")
my_queue = Queue(1)
my_queue.enqueue(2)

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())


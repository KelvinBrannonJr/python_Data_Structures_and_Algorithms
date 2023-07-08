class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append_node(self, value):
        add_node = Node(value)
        if self.length == 0:
            self.head = add_node
            self.tail = add_node

        else:
            self.tail.next = add_node
            self.tail = add_node
        self.length += 1
        return True


my_linked_list = LinkedList(4)


print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

my_linked_list = LinkedList(1)

my_linked_list.append_node(2)

my_linked_list.print_list()




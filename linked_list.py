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

    def remove_last_node(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend_node(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def remove_first_node(self):
        if self.length == 0:
            return None

        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
        return temp

    def get_node_index(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get_node_index(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert_node_at_index(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend_node(value)
        if index == self.length:
            return self.append_node(value)

        new_node = Node(value)
        temp = self.get_node_index(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove_node_at_index(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.remove_first_node()
        if index == self.length - 1:
            return self.remove_last_node()
        prev = self.get_node_index(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse_list(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


# my_linked_list = LinkedList(4)
#
#
# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)


my_linked_list = LinkedList(1)
my_linked_list.append_node(2)
my_linked_list.append_node(3)
my_linked_list.append_node(4)

my_linked_list.reverse_list()

my_linked_list.print_list()

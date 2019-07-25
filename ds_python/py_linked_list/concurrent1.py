class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        node = Node(data)
        if self.__head is None:
            self.__head = node
        else:
            self.__tail.set_next(node)
        self.__tail = node

    def display(self):
        temp = self.__head
        while temp:
            print(temp.get_data())
            temp = temp.get_next()

    def insertNodeAtHead(self, data):
        node = Node(data)
        node.set_next(self.get_head())
        self.__head = node


my_list = LinkedList()
my_list.add(50)
my_list.add(20)
my_list.add(30)
my_list.display()
print("After inserting node at beginning: ")
my_list.insertNodeAtHead(39)
my_list.display()
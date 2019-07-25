class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next = next_node


class LinkedList:
    cnt = 1

    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        node = Node(data)

        if not self.get_head():
            self.__head = node
        else:
            self.__tail.set_next(node)
        self.__tail = node

    def display(self):
        temp = self.__head
        while temp:
            print(temp.get_data())
            temp = temp.get_next()


my_list = LinkedList()
my_list.add(50)
my_list.add(20)
my_list.display()
my_list.add(30)
my_list.display()
# print(item_node.get_data())

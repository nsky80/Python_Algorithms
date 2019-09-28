class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_next(self, next_node):
        self.__next = next_node

    def get_next(self):
        return self.__next


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def display(self):
        temp = self.get_head()
        while temp:
            print(temp.get_data())
            temp = temp.get_next()

    def add(self, data):
        new_node = Node(data)
        if not self.get_head():
            self.__head = new_node
            self.__tail = new_node
        else:
            tail = self.get_tail()
            tail.set_next(new_node)
            self.__tail = new_node


if __name__ == "__main__":
    List = LinkedList()
    List.add("Sugar")
    List.add("Vegetables")
    # item_node = Node("Sugar")

    List.display()

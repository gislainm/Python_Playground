

# working with linkedLists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search_node(self, node):
        temp = self.head
        while temp:
            if temp.data == node:
                return True
            temp = temp.next
        return False
    def delete_node(self,data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next
    def delete_tail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None


Family = LinkedList()

Family.head = Node('Bob')
wife = Node('Amy')
first_child = Node('Max')
second_child = Node('Jenny')

Family.head.next = wife
wife.next = first_child
first_child.next = second_child

Family.insert_new_header('Gislain')
Family.delete_tail()
Family.traversal()
# print(Family.search_node('Muhikira'))
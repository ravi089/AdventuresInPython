# Singly linked list in python.

class Node:
    def __init__(self, data):
        self.data = data
        self.p_next = None

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.p_next
        return '[' + ', '.join(nodes) + ']'

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        prev = None
        while curr:
            prev = curr
            curr = curr.p_next
        prev.p_next = Node(data)

    def insert(self, data, pos):
        curr = self.head
        prev = None
        while curr and pos:
            prev = curr
            curr = curr.p_next
            pos = pos - 1
        if curr is None:
            if pos == 0:
                if not self.head:
                    self.head = Node(data)
                else:
                    prev.p_next = Node(data)
            else:
                print ("please provide valid index!!!")
            return
        if prev is None:  # head
            new_node = Node(data)
            new_node.p_next = curr
            self.head = new_node
            return
        new_node = Node(data)
        prev.p_next = new_node
        new_node.p_next = curr
        
    def contains(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.p_next
        return (curr != None)

    def remove(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.p_next
        if curr is None:
            return
        if prev is None:    # head node
            self.head = curr.p_next
            return
        prev.p_next = curr.p_next
        curr.p_next = None

if __name__ == '__main__':
    lst = LinkedList()
    lst.insert(1, 0)
    lst.insert(2, 1)
    lst.insert(3, 1)
    lst.insert(4, 2)
    lst.insert(5, 4)

    lst.remove(1)
    lst.remove(5)

    lst.append(6)
    lst.append(7)
    print (lst)
            
        
        
            
            
        

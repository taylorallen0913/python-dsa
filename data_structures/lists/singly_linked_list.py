class SinglyLinkedListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class SinglyLinkedList:
    # Creates new singly linked list. If key is inputted,
    # create head with that key, if not, set head to None
    def __init__(self, key=None):
        if key is None:
            self.head = None
            self.length = 0
        else:
            self.head = SinglyLinkedListNode(key)
            self.length = 1

    def insert(self, key):
        # If head does not exist, create head with key
        if self.head is None:
            self.head = SinglyLinkedListNode(key)
            self.length += 1
            return
        node = self.head
        # Iterate until next node is None
        while node.next is not None:
            node = node.next
        node.next = SinglyLinkedListNode(key)
        self.length += 1

    # Deletes first instance of key in singly linked list
    def delete(self, key):
        # If head does not exist, return
        if self.head is None:
            return

        # If key is not in singly linked list, return
        if not self.contains(key):
            return

        node = self.head
        while node.next is not None:
            if node.next.key is key:
                if node.next.next is None:
                    node.next = None
                    self.length -= 1
                    return
                else:
                    node.next = node.next.next
                    self.length -= 1
                    return
            node = node.next

    def print(self):
        # If head does not exist, return
        if self.head is None:
            return

        node = self.head
        while node is not None:
            if node.next is not None:
                print(node.key, end=" ==> ")
            else:
                print(node.key)
            node = node.next

    # Converts singly linked list as a normal Python list
    def to_list(self):
        list = []
        node = self.head
        # Iterate through singly linked list and append to Python list
        while node is not None:
            list.append(node.key)
        return list

    # Returns if key exists in singly linked list or not
    def contains(self, key):
        # If head does not exist, return
        if self.head is None:
            return False

        node = self.head
        while node is not None:
            if node.key is key:
                return True
            node = node.next
        return False

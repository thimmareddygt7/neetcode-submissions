class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.size = 10
        self.buckets = [None] * self.size

    def add(self, key):
        index = key % self.size

        # If bucket is empty
        if self.buckets[index] is None:
            self.buckets[index] = Node(key)
            return

        # Search linked list
        current = self.buckets[index]

        while current:
            # Key already exists
            if current.key == key:
                return

            current = current.next

        # Add new node at the end
        new_node = Node(key)
        current = self.buckets[index]

        while current.next:
            current = current.next

        current.next = new_node

    def contains(self, key):
        index = key % self.size

        current = self.buckets[index]

        while current:
            if current.key == key:
                return True

            current = current.next

        return False

    def remove(self, key):
        index = key % self.size

        current = self.buckets[index]
        previous = None

        while current:

            if current.key == key:

                # Removing first node
                if previous is None:
                    self.buckets[index] = current.next

                # Removing middle/end node
                else:
                    previous.next = current.next

                return

            previous = current
            current = current.next
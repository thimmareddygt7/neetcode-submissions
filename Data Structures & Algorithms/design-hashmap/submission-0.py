class ListNode:
    """Structure for our custom Singly Linked List nodes."""
    def __init__(self, key: int = -1, value: int = -1, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node

class MyHashMap:
    def __init__(self):
        """Initializes the object with an empty map."""
        # Use a prime number size to minimize hash collisions
        self.size = 19997
        self.buckets = [None] * self.size

    def _hash(self, key: int) -> int:
        """Computes a simple hash function to map keys to bucket indices."""
        return key % self.size

    def _find_prev(self, bucket_head: ListNode, key: int) -> ListNode:
        """Helper to find the node PRIOR to the target key."""
        curr = bucket_head
        prev = None
        while curr and curr.key != key:
            prev = curr
            curr = curr.next
        return prev

    def put(self, key: int, value: int) -> None:
        """Inserts a (key, value) pair. If the key exists, updates the value."""
        index = self._hash(key)
        
        # Create a dummy head node if the bucket is empty
        if self.buckets[index] is None:
            self.buckets[index] = ListNode()
            
        prev = self._find_prev(self.buckets[index], key)
        
        if prev.next is None:
            # Key does not exist; append a new node
            prev.next = ListNode(key, value)
        else:
            # Key exists; update its value
            prev.next.value = value

    def get(self, key: int) -> int:
        """Returns the value to which the specified key is mapped, or -1 if empty."""
        index = self._hash(key)
        if self.buckets[index] is None:
            return -1
            
        prev = self._find_prev(self.buckets[index], key)
        return prev.next.value if prev.next else -1

    def remove(self, key: int) -> None:
        """Removes the key and its corresponding value if it exists."""
        index = self._hash(key)
        if self.buckets[index] is None:
            return
            
        prev = self._find_prev(self.buckets[index], key)
        if prev.next:
            # Sever the link to delete the node
            prev.next = prev.next.next

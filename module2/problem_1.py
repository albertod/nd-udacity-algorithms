
class Node:
    '''
     Node class wich hold also the key for reference on deletion of Least Recently Used
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None

class DoubleLinkedList:
    '''
    Double linked list representing a Queue where the head is the LRU element 
    '''
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.number_of_elements = 0

    def add(self, key, value):
        # add element to the head
        node = Node(key, value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.left = self.tail
            self.tail.right = node
            self.tail = node
        # Add to count
        self.number_of_elements +=1
        return node

    def removeLeastUsed(self):
        '''
        Remove the LRU used element (the head) and return the key that mapped to this node
        '''
        # The least recently used will be the head element of the linked list
        if self.head == None:
            return
        removedNode = self.head
        self.head = self.head.right
        if self.head != None:
            self.head.left = None
        self.number_of_elements -= 1
        return removedNode.key

    def updateUsage(self, node):
        '''
        Move the node to the tail of the queue
        '''
        if node.left:
            node.left.right = node.right
        if node.right:
            node.right.left = node.left
        node.left = self.tail
        node.right = None
        self.tail.right = node
        self.tail = node

class LRU_Cache:
    def __init__(self, capacity):
        self.list_ussage_value = DoubleLinkedList(capacity)
        self.map_to_list = {}
        self.capacity = capacity

    def get(self, key):
        # Check for null or emtpy key
        if key == None or key == "":
            return -1
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.map_to_list and self.map_to_list[key].value != None:
            self.list_ussage_value.updateUsage(self.map_to_list[key])
            return self.map_to_list[key].value
        return -1

    def set(self, key, value):
        # Not allow null or empty key
        if key == None or key == "":
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.list_ussage_value.number_of_elements == self.capacity:
            removedKey = self.list_ussage_value.removeLeastUsed()
            self.map_to_list.pop(removedKey)
        
        node = self.list_ussage_value.add(key, value)
        self.map_to_list[key] = node



print('LRU cache with capacity == 1')
our_cache = LRU_Cache(1)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
print(our_cache.get(1))       # returns -1
print(our_cache.get(2))       # returns -1
print(our_cache.get(3))       # return 3
print(our_cache.get(1))       # returns -1
our_cache.set(4, 4)
print(our_cache.get(2))       # return -1
print(our_cache.get(4))       # return 4
print()

print('LRU cache with capacity == 2')
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
print(our_cache.get(1))       # returns -1
print(our_cache.get(2))       # returns 2
print(our_cache.get(3))       # return 3
print()

print('LRU cache with capacity == 2 With 1 being used')
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))       # returns 1
our_cache.set(3, 3)
print(our_cache.get(2))       # returns -1
print(our_cache.get(3))       # return 3
print(our_cache.get(1))       # returns 1
our_cache.set(4, 4)
print(our_cache.get(3))       # return -1
print(our_cache.get(4))       # return 4
print()


print('LRU cache wwith edge case None and empty')
our_cache = LRU_Cache(2)
our_cache.set(None, 1)
our_cache.set("", 2)
print(our_cache.get(1))       # returns 1
our_cache.set(3, 3)
print(our_cache.get(2))       # returns -1
print(our_cache.get(3))       # return 3
print()
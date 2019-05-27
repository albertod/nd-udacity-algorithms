import sys
import heapq
import queue

class Node:
    def __init__(self, frequency, char=None):
        self.frequency = frequency
        self.char = char
        self.left = None
        self.right = None
    
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.frequency == other.frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def isLeaf(self):
        return self.right == None and self.left == None

    def __str__(self):
        return f'({self.frequency} | {self.char})'

def huffman_encoding(data):
    '''
    This funtion retunrs a tuple.
    encoded_data -> data encoded from Huffman tree
    tree -> hufman tree for the encoded data
    '''
    #edge case
    if data == None or data == "":
        return None, None, None
    # crete dict with character -> frequency
    char_frequency = {}
    for char in data:
        if char in char_frequency:
            char_frequency[char] +=1
        else:
            char_frequency[char] = 1

    if len(char_frequency) == 1:
        # we only have one character in the data
        key = data[0]
        return "0"*len(data), Node(None, key), {"0": key}
    
    # create priority queue
    node_priority = []
    for char, frequency in char_frequency.items():
        heapq.heappush(node_priority, Node(frequency, char))

    # Create Huffman tree
    while len(node_priority) > 1:
        # Remove left and right node with < frequency 
        left = heapq.heappop(node_priority)
        right = heapq.heappop(node_priority)
        # join thme in new tree with frequency == left + right
        parent_node = Node(left.frequency + right.frequency)
        parent_node.left = left
        parent_node.right = right
        # add new tree to heap
        heapq.heappush(node_priority, parent_node)

    huffman_tree_root = node_priority.pop()
    
    # Traverse the huffman tree using DFS
    # When encounter a leaf node add the path to it to the dict (codes) path -> character
    # every left is a 0 and every right is a 1
    codes = find_path_func(huffman_tree_root, {}, "")

    # construct encoded string
    encoded_data = ""
    for char in data:
        encoded_data += codes[char]
    
    # reverse the code dictionary to have the mapping (encoding -> character)
    codes = {v:k for k,v in codes.items()}

    return encoded_data, huffman_tree_root, codes

            
def find_path_func(node, codes, current_path):
    #Base case
    if node is None:
        codes 
    if node.isLeaf():
        codes[node.char] = current_path
        return codes
    # Recursion
    else:
        codes = find_path_func(node.left, codes, current_path + '0')
        codes = find_path_func(node.right, codes, current_path + '1')
        return codes

def huffman_decoding(data,tree, codes):
    if data == None or tree == None or codes == None:
        return None
    decoded_data = ""
    cursor = tree
    path = ""
    for digit in data:
        if digit == "0":
            if cursor.left:
                cursor = cursor.left
            path = path + "0"
        else:
            if cursor.right:
                cursor = cursor.right
            path = path + "1"
        if cursor.isLeaf():
            decoded_data += codes[path]
            path = ""
            cursor = tree
    
    return decoded_data

if __name__ == "__main__":

    print('Test 1')
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree, codes = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree, codes)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

    print('Test 2')
    a_great_sentence = "I like to eat tofu"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree, codes = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree, codes)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

    print('Test 3')
    a_great_sentence = "AAAAAAAA"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree, codes = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree, codes)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

    print('Edge case - None')
    a_great_sentence = None
    encoded_data, tree, codes = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree, codes)

    print('Edge case - Empty')
    a_great_sentence = ""
    encoded_data, tree, codes = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree, codes)
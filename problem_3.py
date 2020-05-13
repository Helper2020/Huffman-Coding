import sys
from collections import deque


class Node(object):

    def __init__(self, element=None, freq_value=0):
        self.element = element
        self.freq_value = freq_value
        self.left = None
        self.right = None

    def set_element(self, element):
        self.element = element

    def get_element(self):
        return self.element

    def set_freq_value(self, value):
        self.freq_value = value

    def get_freq_value(self):
        return self.freq_value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        if self.element:
            return f"{self.get_element()}({self.get_freq_value()})"
        else:
            return f"#{self.get_freq_value()}"

    def __str__(self):
        return f"Node({self.get_element()})"


class HuffmanTree:
    """
    This class creates a huffman Tree from a string of data.

    Attributes:
      self.data: A string of elements
      self.root: A node that is the root of the huffman Tree.

    """

    def __init__(self, data=None):
        self.data = data
        self.root = None
        self._create_tree()

    def get_root(self):
        return self.root

    def _create_tree(self):
        if self.data == '':
            raise ValueError("Data must not be an empty string")
        freq_dict = self._create_freq_dist()
        node_deque = self._create_nodes(freq_dict)
        self.root = self._connect_nodes(node_deque)

    def _create_freq_dist(self):
        """
        Helper function to create a frequency distribution

        Returns:
           Dictionary representing the frequency distribution.
        """
        freq_dict = dict()

        for element in self.data:
            if element in freq_dict:
                freq_dict[element] += 1
            else:
                freq_dict[element] = 1

        return freq_dict

    def _create_nodes(self, freq_dict):
        """
        Helper function to create nodes from a frequency distribution

        Returns:
           A ordered deque in ascending order.
        """
        to_return = []

        for character, freq in freq_dict.items():
            new_node = Node(character, freq)
            to_return.append(new_node)

        return deque(sorted(to_return, key=lambda x: x.get_freq_value()))

    def _connect_nodes(self, node_deque):
        """
        This function creates the huffman tree

        Args:
          A deque of node objects.

        Returns:
          A node object which is the root of the huffman tree
        """
        # Case where there is only 1 node in the test
        if len(node_deque) == 1:
            child = node_deque.pop()
            # create root for only child
            root = Node()
            root.set_freq_value(1)
            root.set_left_child(child)
            return root

        while len(node_deque) > 1:
            first_tree = node_deque.popleft()
            second_tree = node_deque.popleft()
            # The first tree is getting to big so start another
            if first_tree.get_freq_value() > second_tree.get_freq_value():
                node_deque.append(first_tree)
                first_tree = node_deque.popleft()
                # A parent node for the two children
            tree_node = Node()

            tree_node.set_left_child(first_tree)
            tree_node.set_right_child(second_tree)

            # Add the two  child frequency values to the parent node value
            total_freq = tree_node.get_left_child().get_freq_value() + tree_node.get_right_child().get_freq_value()
            tree_node.set_freq_value(total_freq)
            node_deque.appendleft(tree_node)

        return node_deque.pop()

def huffman_encoding(data):
    """
    This function encodes the data

    Args:
      data: The data to be encoded.
      root_node; The huffman tree.

    returns:
      tuple: String Encoded data, root node
    """

    tree = HuffmanTree(data)
    root = tree.get_root()
    encoded_data = ''

    for character in data:
        encoded_data += search_tree(character, root)

    return encoded_data, tree.get_root()


def search_tree(element, root):
    # Case where root is only node
    if root.get_element() == element:
        return ''

    left = None
    right = None

    # Go left
    if root.has_left_child():
        left = search_tree(element, root.get_left_child())
    # Go right
    if root.has_right_child():
        right = search_tree(element, root.get_right_child())

    if left is not None:
        return '0' + left

    if right is not None:
        return '1' + right


def huffman_decoding(code, root):
    """
    This function decodes.
    :param code: A string representing bits
    :param tree: A binary tree
    :return str: A decoded string
    """

    return _huffman_decoding(code, root, root, '', 0)


def _huffman_decoding(code, root, child, data, idx):
    if not child.has_left_child() and not child.has_right_child():
        data += child.get_element()
        return _huffman_decoding(code, root, root, data, idx)

    if idx >= len(code):
        return data

    bit = code[idx]
    if bit == '0':
        return _huffman_decoding(code, root, child.get_left_child(), data, idx + 1)
    else:
        return _huffman_decoding(code, root, child.get_right_child(), data, idx + 1)


def test_huffman(a_great_sentence):
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


print('------------------------- Test Case 1 -------------------------')
test_huffman("HUFFMAN")
# Should print HUFFMAN

print('------------------------- Test Case 2 -------------------------')
test_huffman("AAAAABBAHHBCBGCCC")
# Should print AAAAABBAHHBCBGCCC"

print('------------------------- Test Case 3 -------------------------')
# Edge case if there is a single character
test_huffman("A")
# Should print A"

print('------------------------- Test Case 4 -------------------------')
# Edge case if there is mutiple character of one type
test_huffman("AAAAA")
# Should print AAAA"

print('------------------------- Test Case 5 -------------------------')
# Edge case if empty string
test_huffman("                     ")

print('------------------------- Test Case 6-------------------------')
# Edge case if string length is 0
# test_huffman("")
# Should raise a ValueError





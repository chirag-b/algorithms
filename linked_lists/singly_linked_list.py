# -----------------------------------------------
# Author: Chirag Balakrishna
# Description: Python implementation of a singly 
# linked list
# -----------------------------------------------

# -----------------------------------------------
# Properties: 
#   - Nodes with reference to next node
#   - Head and Tail pointers point to first node
#     and last node in the list respectively
#   - The last node has a NULL reference
#
# Operations:
#   - Add node(), remove(at pos), peek, length, 
#     remove, Add(at pos), list all nodes
# -----------------------------------------------

import logging
import sys

logging.basicConfig(stream = sys.stdout, level = logging.INFO)
logger = logging.getLogger()


class Node:
    def __init__(self, value, next=None):
        self.value = value # This can be of any type int, string, float...
        self.next = next  # In other languages this will be of type 'Node'.

class SinglyLinkedList:
    def __init__(self):
        # Returns a Singly Linked List instance
        self.head = None 
        self.tail = None
        self.size = 0
        
    def get_size(self):
        # Returns the size of the list
        return self.size

    def is_empty(self):
        # Returns True if list is empty else returns False
        return self.size == 0


    def add_node(self, value):
        # Adds a node to the end of the list
        if self.is_empty():
            logger.info('Adding the first node')
            node = Node(value)
            self.head = node
            self.tail = node
            self.size += 1
        else:
            logger.info(f'Adding node {value} to the end')
            node = Node(value)
            self.tail.next = node
            self.tail = node
            self.size += 1


    def add_node_at(self, value, position):
        # Adds a node at 'position'
        pass

    def remove_node(self, value):
        # Removes a node with 'value'
        pass

    def remove_node_at(self, position):
        # Removes node at 'position'
        pass
    
    def list_all_nodes(self):
        # Lists all nodes currently in the Singly Linked List
        if self.is_empty():
            logger.info(f'The list is empty!!')
        else:
            trav = self.head
            all_nodes = ""
            for _ in range(self.get_size()):
                all_nodes += str(trav.value)
                all_nodes += " -> "
                trav = trav.next
            logger.info(all_nodes)

    def get_value_at(self, position):
        # Returns the value of a node at 'position'
        pass

    def add_first(self, value):
        # Adds a new node to the head of the list
        pass

    def remove_first(self):
        # Removes the node at the head
        pass

    def remove_last(self):
        # Removes the last node in the list
        pass

    def get_head_value(self):
        return self.head.value

    def get_tail_value(self):
        return self.tail.value

if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    newSLL = SinglyLinkedList()
    newSLL.add_node(5)
    newSLL.add_node(6)
    newSLL.add_node(7)
    newSLL.add_node(8)
    newSLL.add_node(9)
    newSLL.add_node(10)
    newSLL.add_node(11)
    logger.info(newSLL.get_size())
    logger.info(newSLL.is_empty())
    logger.info(newSLL.get_head_value())
    logger.info(newSLL.get_tail_value())
    newSLL.list_all_nodes()

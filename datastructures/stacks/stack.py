# -----------------------------------------------
# Author: Chirag Balakrishna
# Description: Python implementation of a stack 
# using a doubly linked list
# -----------------------------------------------

# -----------------------------------------------
# Properties: 
#    - LIFO -> last in first out
#    - Push nodes onto stack
#    - Remove top node from stack
#    - Size, peek, get last element
# -----------------------------------------------

import logging
import sys

from linkedlists.doubly_linked_list import DoublyLinkedList

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()


class Stack(DoublyLinkedList):
    def __init__(self):
        super().__init__()
    

    def push(self, value):
        # Pushes value onto stack
        # Running Time: O(1)
        super().add_first(value)


    def get_size(self):
        # Returns the size of the stack
        # Running Time: O(1)
        return super().get_size()


    def is_empty(self):
        # Returns True if stack is empty else returns False
        # Running Time: O(1)
        return super().is_empty()


    def pop(self):
        # Removes value from top of stack
        # Running Time: O(1)
        return super().remove_first()

    
    def peek(self):
        # Running Time: O(1)
        return super().get_head_value()


    def top(self):
        # Running Time: O(1)
        return super().get_head()

    
    def show_stack(self):
        # Running Time: O(1)
        super().list_all_nodes()

    
    def search(self, value):
        # Search for a value
        # Running Time: O(n)
        node_position = super().get_index_of(value)
        if node_position:
            logger.info(f'Found at position {node_position}')
        else:
            logger.info(f'Node not found!!')
# -----------------------------------------------
# Author: Chirag Balakrishna
# Description: Python implementation of a queue 
# using a doubly linked list
# -----------------------------------------------

# -----------------------------------------------
# Properties: 
#    - FIFO -> first in first out
#    - enqueue (a.k.a offer), dequeue (a.k.a poll)
#    - Size, peek, search
# -----------------------------------------------

import logging
import sys

from linkedlists.singly_linked_list import SinglyLinkedList

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()


class Queue(SinglyLinkedList):

    def __init__(self):
        super().__init__()


    def enqueue(self, value):
        super().add_node(value)

    
    def dequeue(self):
        super().remove_first()

    
    def search(self, value):
        position = super().get_index_of(value)
        if position != None:
            logger.info(f"Value {value} found at {position}")
        else:
            logger.info(f"Value {value} could not be found in the queue.")


    def peek(self):
        position = super().get_head_value()
        if position != None:
            logger.info(f"Value at the front of the queue: {value}")
        else:
            logger.info(f"Queue is empty!")

    def show_queue(self):
        super().list_all_nodes()
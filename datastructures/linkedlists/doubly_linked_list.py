# -----------------------------------------------
# Author: Chirag Balakrishna
# Description: Python implementation of a doubly 
# linked list
# -----------------------------------------------

# -----------------------------------------------
# Properties: 
#   - Nodes with reference to next node and the 
#     previous node
#   - Head and Tail pointers point to first node
#     and last node in the list respectively
#   - The last node has a NULL reference
# -----------------------------------------------

import logging
import sys

logging.basicConfig(stream = sys.stdout, level = logging.INFO)
logger = logging.getLogger()


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value # This can be of any type int, string, float...
        self.next = next  # In other languages this will be of type 'Node'.
        self.prev = prev  # In other languages this will be of type 'Node'.


class DoublyLinkedList:
    def __init__(self):
        # Returns a Doubly Linked List instance
        self.head = None 
        self.tail = None
        self.size = 0
        

    def get_size(self):
        # Returns the size of the list
        # Running Time: O(1)
        return self.size


    def is_empty(self):
        # Returns True if list is empty else returns False
        # Running Time: O(1)
        return self.size == 0


    def add_node(self, value):
        # Adds a node to the end of the list
        # Running Time: O(1)
        if self.is_empty():
            logger.info('List is empty, adding the first node')
            node = Node(value)
            self.head = node
            self.tail = node
            self.size += 1
        else:
            logger.info(f'Adding node {value} to the end')
            node = Node(value)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1


    def add_node_at(self, position, value):
        # Adds a node at 'position'
        # Running Time: O(n)
        if not (position <= self.size):
            logger.info('Invalid position specified!!') 
        else:
            if self.is_empty():
                logger.info('List empty adding node at head.')
                node = Node(value)
                self.head = node
                self.tail = node
                self.size += 1
            elif position == 1:
                self.add_first(value)
            else:
                trav = self.head
                for _ in range(position-2):
                    trav = trav.next
                node = Node(value, trav.next, trav)
                trav.next.prev = node
                trav.next = node
                self.size += 1


    def remove_node(self, value):
        # Removes a node with 'value'
        # Running Time: O(n)
        if self.is_empty():
            logger.info('Nothing to remove, the list is empty.')
        else:
            trav = self.head
            position = self.get_index_of(value)
            if position:
                for _ in range(position-1):
                    trav = trav.next
                trav.prev.next = trav.next
                trav.next.prev = trav.prev
                del trav 
                self.size -= 1
            else:
                logger.info('Node not found!!')


    def get_index_of(self, value):
        # Returns the index of the value in the list
        # Running Time: O(n)
        if self.is_empty():
            logger.info('The list is empty!!')
            return False
        else:
            trav = self.head
            for position in range(self.size):
                if (trav.next != None) and (trav.value != value):
                    trav = trav.next
                elif (trav.next == None) and (trav.value != value):
                    return False
                else:
                    break 
            position += 1
            return position


    def remove_node_at(self, position):
        # Removes node at 'position'
        # Running Time: O(n)
        if not (position <= self.size):
            logger.info('Invalid position specified!!') 
        else:
            if self.is_empty():
                logger.info('The list is empty!!')
            else:
                assert(position <= self.size)
                trav = self.head
                for _ in range(position-1):
                    trav = trav.next
                trav.prev.next = trav.next
                trav.next.prev = trav.prev
                del trav 
                self.size -= 1


    def list_all_nodes(self):
        # Lists all nodes currently in the Doubly Linked List
        # Running Time: O(n)
        if self.is_empty():
            logger.info(f'The list is empty!!')
        else:
            trav = self.head
            all_nodes = ""
            for _ in range(self.get_size()):
                all_nodes += str(trav.value)
                if trav.next is not None:
                    all_nodes += " <-> "  
                else:
                    all_nodes += " <-> EOL"
                trav = trav.next
            logger.info(all_nodes)


    def get_value_at(self, position):
        # Returns the value of a node at 'position'
        # Running Time: O(n)
        if not (position <= self.size):
            logger.info('Invalid position specified!!') 
        else:
            if self.is_empty():
                logger.info('The list is empty!!')
            else:
                assert(position <= self.size)
                trav = self.head
                for _ in range(position - 1):
                    trav = trav.next
                return trav.value


    def add_first(self, value):
        # Adds a new node to the head of the list
        # Running Time: O(1)
        if self.is_empty():
            logger.info('List empty adding node at head.')
            node = Node(value)
            self.head = node
            self.tail = node
            self.size += 1
        else:
            node = Node(value, self.head, None)
            self.head.prev = node
            self.head = node
            self.size += 1


    def remove_first(self):
        # Removes the node at the head
        # Running Time: O(1)
        if self.is_empty():
            logger.info('The list is empty!!')
        else:
            trav = self.head
            self.head = self.head.next
            self.size -= 1
            del trav    


    def remove_last(self):
        # Removes the last node in the list
        # Running Time: O(1)
        if self.is_empty():
            logger.info('The list is empty!!')
        else:
            trav = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            del trav
            self.size -= 1


    def get_head_value(self):
        # Running Time: O(1)
        if self.is_empty():
            logger.info('The list is empty')
        else:
            return self.head.value


    def get_tail_value(self):
        # Running Time: O(1)
        if self.is_empty():
            logger.info('The list is empty')
        else:
            return self.tail.value


# if __name__ == '__main__':
#     # import pdb; pdb.set_trace()
#     newDLL = DoublyLinkedList()
#     newDLL.add_node(5)
#     newDLL.add_node(6)
#     newDLL.add_node(7)
#     newDLL.add_node(8)
#     newDLL.add_node(9)
#     newDLL.add_node(10)
#     newDLL.add_node(11)
#     logger.info(newDLL.get_size())
#     newDLL.list_all_nodes()

#     newDLL.add_node_at(6, 66)
#     logger.info(newDLL.get_size())
#     newDLL.list_all_nodes()

#     newDLL.add_node_at(2, 555)
#     logger.info(newDLL.get_size())
#     newDLL.list_all_nodes()

#     newDLL.add_node_at(1, 4)
#     logger.info(newDLL.get_size())
#     newDLL.list_all_nodes()

#     newDLL.add_node_at(1, 3)
#     logger.info(newDLL.get_size())
#     newDLL.list_all_nodes()

#     newDLL.remove_node(6000)
#     logger.info(newDLL.get_size())
#     newDLL.list_all_nodes()

#     newDLL.add_first(2)
#     logger.info(newDLL.get_size())
#     newDLL.list_all_nodes()

#     newDLL.remove_node(6)
#     logger.info(newDLL.get_size())
#     newDLL.list_all_nodes()

#     newDLL.remove_node(555)
#     logger.info(newDLL.get_size())
#     newDLL.list_all_nodes()

#     newDLL.remove_node_at(7)
#     logger.info(newDLL.get_size())
#     newDLL.list_all_nodes()

#     newDLL.remove_first()
#     logger.info(newDLL.get_size())
#     newDLL.list_all_nodes()

#     newDLL.remove_last()
#     logger.info(newDLL.get_size())
#     newDLL.list_all_nodes()
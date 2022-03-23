# ------------------------------------------------
# Author: Chirag Balakrishna
# Description: Python implementation of a priority
# queue using binary heaps
# ------------------------------------------------
# 
# ------------------------------------------------
# Properties:
#   - The min heap property states that the value
#   of the parent node is lesser than its children
# ------------------------------------------------

import sys
import logging
import math

logging.basicConfig(stream = sys.stdout, level = logging.INFO)
logger = logging.getLogger()

class PriorityQueue():
    def __init__(self):
        self.heap = []


    def add(self, value):
        # Adds an element to the queue and
        # moves the element to the appropriate
        # position in the queue.
        self.heap.append(value)
        indexOfLastElement = self.size() - 1
        self.swim(indexOfLastElement)


    def remove():
        pass


    def poll(self):
        # Removes the element at the root of
        # the heap. Returns the next smallest
        # element in the priority queue
        indexOfLastElement = self.size() - 1
        element = self.heap[0]

        self.swap(indexOfLastElement, 0)
        del self.heap[indexOfLastElement]
        self.sink(0)
        return element


    def peek(self):
        return self.heap[0]


    def size(self):
        return len(self.heap)


    def printHeap(self):
        logger.info(self.heap)


    def heapify(self, element_list):
        self.heap = element_list

        parent = math.floor((self.size())/2)

        while(parent >= 0):
            self.sink(parent)
            parent = parent - 1


    def sink(self, index):
        # Sinks the element located at index down to
        # its correct position based on its value
        leftChildIndex = 2 * index + 1 
        rightChildIndex = 2 * index + 2
        smallest = leftChildIndex

        while(leftChildIndex <= self.size() - 1):
            if rightChildIndex < self.size() and \
                    self.heap[rightChildIndex] < self.heap[leftChildIndex]:
                smallest = rightChildIndex

            if self.heap[smallest] < self.heap[index]:
                self.swap(smallest, index)
                index = smallest
                leftChildIndex = 2 * index + 1
                rightChildIndex = 2 * index + 2
                smallest = leftChildIndex
            else:
                break


    def swap(self, index_1, index_2):
       # Swaps the value at index_1 with value
       # at index_2
       temp = self.heap[index_1]
       self.heap[index_1] = self.heap[index_2]
       self.heap[index_2] = temp


    def swim(self, index):
       # Moves element at index up the tree to 
       # the correct position based on its value
       parentIndex = math.floor((index - 1)/2)

       while(self.heap[parentIndex] > self.heap[index]):
           self.swap(parentIndex, index)

           index = parentIndex  
           if index == 0:
               # If we reached the root, we can stop.
               break
           parentIndex = math.floor((index - 1)/2)  

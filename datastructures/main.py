import logging
import sys

from stacks.stack import Stack
from queues.queue import Queue
from priority_queues.priority_queue import PriorityQueue

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

if __name__ == "__main__":
    # mystack = Stack()
    
    # for value in range(10):
    #     mystack.push(value+1)
    # mystack.show_stack()
    # logger.info(mystack.get_size())

    # mystack.pop()
    # mystack.show_stack()
    # logger.info(mystack.get_size())

    # mystack.pop()
    # mystack.show_stack()
    # logger.info(mystack.get_size())

    # my_queue = Queue()
    # for value in range(10):
        # my_queue.enqueue(value+1)
    # my_queue.show_queue()
    # logger.info(my_queue.get_size())

    # my_queue.dequeue()
    # my_queue.show_queue()

    # my_queue.dequeue()
    # my_queue.show_queue()

    # my_queue.enqueue(100)
    # my_queue.show_queue()

    # my_queue.dequeue()
    # my_queue.show_queue()
    
    pq = PriorityQueue()
    l = [7, 6, 5, 4, 3, 2, 1]
    pq.heapify(l)
    logger.info(pq.size())
    pq.printHeap()
    logger.info(pq.poll())
    pq.printHeap()
    pq.add(0)
    logger.info(pq.peek())
    pq.printHeap()


import logging
import sys

from stacks.stack import Stack

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

if __name__ == "__main__":
    mystack = Stack()
    
    for value in range(10):
        mystack.push(value+1)
    mystack.show_stack()
    logger.info(mystack.get_size())

    mystack.pop()
    mystack.show_stack()
    logger.info(mystack.get_size())

    mystack.pop()
    mystack.show_stack()
    logger.info(mystack.get_size())


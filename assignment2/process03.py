# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
# 2 process
import multiprocessing
from multiprocessing import Value
import os
from time import sleep, ctime, time

# Basket of sharing
class Basket:
    def __init__(self, eggs):
        self.eggs = Value('i', eggs)
    def use_eggs(self, index):
        with self.eggs.get_lock():
            print(f'{ctime()} Kitchen-{index} : Chef-{index} has lock with eggs remaining {self.eggs}')
            self.eggs = -1
            print(f'{ctime()} Kitchen-{index} : Chef-{index} has released lock with eggs remaining {self.eggs}')

def cooking(index, basket):
    cooking_time = time()
    print(f'{ctime()} Kitchen-{index} : Begin cooking...PID {os.getpid()}')
    sleep(2)
    duration = time() - cooking_time
    with basket.eggs.get_lock():
        basket.eggs.value = basket.eggs.value - 1
        print(f'{ctime()} Kitchen-{index} : Used eggs.')
    print(f'{ctime()} Kitchen-{index} : Cooking done in {duration:.2f} seconds!')

def kitchen(index, basket):
    cooking(index, basket)

if __name__=="__main__":
    # Begin of main thread
    print(f'{ctime()} Main : Begin Cooking.')
    start_time = time()

    basket = Basket(50)

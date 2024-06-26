# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
# share resources
import multiprocessing
import os
from time import sleep, ctime, time

# Basket of sharing
class Basket:
    def __init__(self):
        self.eggs = 50

    def use_eggs(self, index):
        print(f'{ctime()} Kitchen-{index} : Chef-{index} has lock with eggs remaining {self.eggs}')
        self.eggs -= 1
        print(f'{ctime()} Kitchen-{index} : Chef-{index} has released lock with eggs remaining {self.eggs}')

# chef cooking
def cooking(index, basket):
    # chef use eggs for cooking
    basket.use_eggs(index)
    sleep(2)

# kitchen cooking
def kitchen(index, share_eggs):
    print(f'{ctime()} Kitchen-{index} : Begin cooking...PID {os.getpid()}')
    cooking_time = time()
    cooking(index, share_eggs)
    duration = time() - cooking_time
    print(f'{ctime()} Kitchen-{index} : Cooking done in {duration:0.2f} seconds!')

if __name__ == '__main__':
    # Begin of main thread
    print(f'{ctime()} Main    : Start Cooking...PID {os.getpid()}')
    start_time = time()

    basket = Basket()
# running a function in another thread
from time import sleep, ctime
from threading import Thread

<<<<<<< HEAD
# a custom fuction that blocks for amoment
def task():
    #block for a moment
    sleep(1)
    #display a message
    print(f'{ctime()} This is from another thread')

#create a thread
thread = Thread(target=task)
#run thread
thread.start()
#wait for thread to finnish
print(f'{ctime()} Waiting for the thred...')
=======
# a custom function that blocks for a moment
def task():
    # block for a moment
    sleep(1)
    # display a message
    print(f'{ctime()} This is from another thread')

# create a thread
thread = Thread(target=task)
# run the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
>>>>>>> 3970926c92ff939fa8cee033ec5ab6e687e5eeab
thread.join()
# running a function with arguments in another thread
from time import sleep, ctime
from threading import Thread

<<<<<<< HEAD
# a custom fuction that blocks for amoment
def task(sleep_time,message):
    #block for a moment
    sleep(sleep_time)
    #display a message
    print(f'{ctime()} {message}')

#create a thread
thread = Thread(target=task,args=(1.5,'New message from another thread'))
#run thread
thread.start()
#wait for thread to finnish
print(f'{ctime()} Waitting for the thread...')
thread.join()
=======
# a custom function that blocks for a moment
def task(sleep_time, message):
    # block for a moment
    sleep(sleep_time)
    # display a message
    print(f'{ctime()} {message}')

# create a thread
thread = Thread(target=task, args=(1.5, 'New message from another thread'))
# run the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()
>>>>>>> 3970926c92ff939fa8cee033ec5ab6e687e5eeab

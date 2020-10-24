#https://stackoverflow.com/questions/20576960/python-infinite-while-loop-break-on-user-input
import time
import threading

# set global variable flag
flag = 1

def normal():
    global flag
    while flag==1:
        print('normal stuff')
        time.sleep(2)
        if flag==False:
            print('The while loop is now closing')


def get_input():
    global flag
    keystrk=input('Press a key \n')
    # thread doesn't continue until key is pressed
    print('You pressed: ', keystrk)
    flag=False
    print('flag is now:', flag)

n=threading.Thread(target=normal)
i=threading.Thread(target=get_input)
n.start()
i.start()

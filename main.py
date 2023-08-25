import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

toggle_key = KeyCode(char='p')
clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.1)

def toogle_event(key):
    if key == toggle_key:
        global clicking
        clicking = not clicking     

def main():
    clicking_thread = threading.Thread(target=clicker)
    clicking_thread.start()

if __name__ == '__main__':
    main()

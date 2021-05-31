from pynput.mouse import Button,Controller as mousec
import time
from pynput.keyboard import Key,Controller as key_cl
def main():
    mouse=mousec()
    mouse.press(Button.left)
    mouse.release(Button.left)
    for i in range(9):
        keyboard=key_cl()
        keyboard.type('。。。')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
time.sleep(8)
main()


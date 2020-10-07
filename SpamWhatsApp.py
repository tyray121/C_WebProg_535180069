from pynput.keyboard import Key, Controller
import time

Keyboard = Controller()
time.sleep(5)
while True:
    for letter in "Spam Dong":
        Keyboard.press(letter)
        Keyboard.relase(letter)
    Keyboard.press(Key.enter)
    Keyboard.relase(Key.enter)

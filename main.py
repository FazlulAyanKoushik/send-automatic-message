"""
    This project is a simple automation project
    that will send message repetitively to a contact on whatsapp, Messenger, etc.
"""

import pyautogui
import time
import random

time.sleep(5)

funny_message_list = [
    "I'm not your enemy",
    "I'm a poor guy",
    "Dont kill me",
    "Dont Fight with me",
    "I'm a good guy",
    "Be nice to me",
    "Stay safe, stay healthy, stay beautiful",
]

no_of_message = 100

while no_of_message > 0:
    message = random.choice(funny_message_list)
    pyautogui.typewrite(message)
    time.sleep(1)
    pyautogui.press("enter")
    no_of_message -= 1



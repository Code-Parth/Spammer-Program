import random
import pyautogui
from time import sleep
with open("Words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
sleep(10)
for i in range(0, 1000):
    pyautogui.write(random.choice(words))
    pyautogui.press("enter")
pyautogui.write("Sorry for spam,I was trying spam program for random words.")
pyautogui.press("enter")
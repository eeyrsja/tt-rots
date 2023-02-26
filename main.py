import pyautogui
from time import sleep
from PIL import Image, ImageChops
import pytesseract
import re
from random import randint

SPEED = 0.00001

sleep(2)
locEnter = pyautogui.locateOnScreen('Enter.png', confidence=0.7)
locDelete = pyautogui.locateOnScreen('Delete.png', confidence=0.7)
loc0 = pyautogui.locateOnScreen('0.png', confidence=0.8)
loc1 = pyautogui.locateOnScreen('1.png', confidence=0.8)
loc2 = pyautogui.locateOnScreen('2.png', confidence=0.8)
loc3 = pyautogui.locateOnScreen('3.png', confidence=0.8)
loc4 = pyautogui.locateOnScreen('4.png', confidence=0.8)
loc5 = pyautogui.locateOnScreen('5.png', confidence=0.8)
loc6 = pyautogui.locateOnScreen('6.png', confidence=0.8)
loc7 = pyautogui.locateOnScreen('7.png', confidence=0.8)
loc8 = pyautogui.locateOnScreen('8.png', confidence=0.8)
loc9 = pyautogui.locateOnScreen('9.png', confidence=0.8)
locBack = pyautogui.locateOnScreen('back.png', confidence=0.8)
locAnsbox = pyautogui.locateOnScreen('ansbox.png', confidence=0.9)

print(loc0)
print(loc1)
print(loc2)
print(loc3)
print(loc4)
print(loc5)
print(loc6)
print(loc7)
print(loc8)
print(loc9)


print("STARTING TO PLAY...")

for i in range(100):
    imgScreen = pyautogui.screenshot()
    imgQ = imgScreen.crop((locAnsbox.left+150, locAnsbox.top-75, locAnsbox.left+locAnsbox.width-150, locAnsbox.top+locAnsbox.height-75))
    imgQ = ImageChops.invert(imgQ)
    imgQ = imgQ.split()[1].point( lambda p: 255 if p > 127 else 0 )

    text = pytesseract.image_to_string(imgQ, config='--psm 6') # -c tessedit_char_whitelist=0123456789x+')
    text = text.replace("l","1")
    textre = re.match("(\d{1,3})([^0-9]*)(\d{1,3})(.*)", text)
    try:
        if "x" in textre[2] or "«" in textre[2]:
            answer = int(textre[1]) * int(textre[3])
            print("{} x {} = {}".format(int(textre[1]), int(textre[3]), answer))
        else:
            answer = int(textre[1]) / int(textre[3])
            print("{} / {} = {}".format(int(textre[1]), int(textre[3]), answer))

        answer = str(int(answer))
    except:
        answer = str(randint(0,144))
        print("DON'T KNOW ANSWER")

    for d in answer:
        if d == "0":
            pyautogui.moveTo(loc0, duration=SPEED)
            pyautogui.click()
        elif d == "1":
            pyautogui.moveTo(loc1, duration=SPEED)
            pyautogui.click()
        elif d == "2":
            pyautogui.moveTo(loc2, duration=SPEED)
            pyautogui.click()
        elif d == "3":
            pyautogui.moveTo(loc3, duration=SPEED)
            pyautogui.click()
        elif d == "4":
            pyautogui.moveTo(loc4, duration=SPEED)
            pyautogui.click()
        elif d == "5":
            pyautogui.moveTo(loc5, duration=SPEED)
            pyautogui.click()
        elif d == "6":
            pyautogui.moveTo(loc6, duration=SPEED)
            pyautogui.click()
        elif d == "7":
            pyautogui.moveTo(loc7, duration=SPEED)
            pyautogui.click()
        elif d == "8":
            pyautogui.moveTo(loc8, duration=SPEED)
            pyautogui.click()
        elif d == "9":
            pyautogui.moveTo(loc9, duration=SPEED)
            pyautogui.click()

    pyautogui.moveTo(locEnter, duration=SPEED)
    pyautogui.click()

pyautogui.moveTo(locBack, duration=SPEED)
pyautogui.click()
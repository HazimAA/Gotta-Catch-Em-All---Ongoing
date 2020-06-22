import cv2
import pytesseract
import numpy as nm
import winsound
import pyautogui
import time
from PIL import ImageGrab
from random import randint

# You can also use the screenshot command to look for buttons, I wanted to mess around with the
# pillow library myself, so I went with the method at hand

def clickonscreen(match,check,count):
    if check is False:
        print("No common elements")
        pyautogui.click()
        pyautogui.move(0, 30)

    else:
        pyautogui.move(0, 30)
        print(match)
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        pyautogui.alert('Rare Species Spotted!')
        variable = False
        return False

    pyautogui.move(0, 30)

    print('End of if-else')

    time.sleep(randint(1, 10))
    if (count % 2 == 0):
        pyautogui.moveTo(826, 309)
    else:
        pyautogui.moveTo(825, 369)

def imToString():

    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    variable = True
    check = False

    print("Enter names of the Pokemon you want to catch. Give an 'empty space' between the names of Pokemon: ")
    source = [name for name in input().split(' ')]
    print(source)

    source_normalized = [word.lower() for word in source]
    set_a = set(source_normalized)
    count = 0;


    while (variable == True):
        print('Start of While Loop')
        print('value of check at the start')
        print(check)

        # ImageGrab-To capture the screen image in a loop.
        # Bbox used to capture a specific area.
        cap = ImageGrab.grab(bbox=(748, 626, 916, 646))
        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        tesstr = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')

        split_words = tesstr.split()

        normalized_input = [word.rstrip('.,!?').lower() for word in split_words]
        set_b = set(normalized_input)
        match = set_a & set_b

        check = any(item in normalized_input for item in source_normalized)
        print('value of check at the end')
        print(check)

        clickonscreen(match, check, count)
        count = count + 1

        print(count)

        # Calling the function

imToString()
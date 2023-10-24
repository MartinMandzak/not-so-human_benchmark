from PIL import ImageGrab
import pyautogui
import cv2
import numpy as np

target_png = cv2.imread("C:/Users/mandz/Desktop/GitHub Projects/not-so-human_benchmark/assets/target.png")

def find_and_click(): 
    screenshot = ImageGrab.grab()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    result = cv2.matchTemplate(screenshot_cv, target_png, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    target_x,target_y = max_loc

    pyautogui.move(target_x,target_y)
    pyautogui.click()


find_and_click()

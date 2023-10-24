import pyautogui
from PIL import ImageGrab
import numpy as np
import time

screen_w,screen_h = pyautogui.size()
region = (0,235,screen_w,screen_h-70)
target_color = (149,195,232)

def find_and_click():
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)
    coords = np.where(np.all(screenshot_np == target_color, axis=2))
    x,y = coords[1][-1],coords[0][-1]
    pyautogui.moveTo(x+15,y-15)
    pyautogui.click()

if __name__ == "__main__":
    time.sleep(2)
    #pyautogui.moveTo(screen_w//2,screen_h//2+50)
    #pyautogui.click()
    for click in range(32):
        find_and_click()

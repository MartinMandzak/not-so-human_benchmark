import pyautogui
import numpy as np
import mss
import time

screen_w,screen_h = pyautogui.size()
target_color = (149,154,135)


def find_and_click():
    with mss.mss() as peeper:
        monitor = {"top": 235, "left" :0, "width": screen_w, "height": screen_h-50}
        screenshot = peeper.grab(monitor)
        screenshot = screenshot.rgb
       #screenshot_np = np.array(screenshot)
        coords = np.where(np.all(screenshot == target_color))
        x,y = coords[1][-1],coords[1][-1]
        pyautogui.moveTo(x+15,y-15)
        pyautogui.click()
        

if __name__ == "__main__":
    time.sleep(2)
    #pyautogui.moveTo(screen_w//2,screen_h//2-55)
    #pyautogui.click()
    for click in range(32):
        find_and_click()

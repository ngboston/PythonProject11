from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
import time

#643 697 - restartbtn
#292 705 - dino

class DinoBot:
    def __init__(self, replaybtn, dino):
        self.replaybtn = replaybtn
        self.dino = dino
        self.delay = 0.1

    def restartgame(self):
        pyautogui.click(self.replaybtn)

    def jump(self):
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')
        time.sleep(self.delay)
        pyautogui.keyDown('down')
        time.sleep(0.05)
        pyautogui.keyUp('down')
        self.delay += 0.1

    def grabImage(self):
        box = (self.dino[0] + 35, self.dino[1], self.dino[0] + 75, self.dino[1] + 30)
        image = ImageGrab.grab(box)
        grayimage = ImageOps.grayscale(image)
        a = array(grayimage.getcolors())
        return a.sum()

    def start(self):
        self.restartgame()
        while True:
            print(self.grabImage()) #1477 white
            if self.grabImage() != 1447:
                self.jump()




def main():
    bot = DinoBot((474, 462), (268, 463))
    bot.start()

if __name__ == "__main__":
    main()
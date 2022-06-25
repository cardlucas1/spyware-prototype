import pyautogui as gui
import cv2
import numpy as np
import time
import pygame
import pygame.camera

def take_screenshot(a):
    img = gui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.imwrite("image" + str(a+1) + ".png", img)

def take_photo(a, cam):
    cam.start()
    image = cam.get_image()
    cam.stop()
    pygame.image.save(image, "pic" + str(a+1) + ".jpg")

def main():
    a = 0
    pygame.init()
    pygame.camera.init()
    cam = pygame.camera.Camera("/dev/video0", (640,480))
    while True:
        take_photo(a, cam)
        take_screenshot(a)
        a+=1
        time.sleep(0.5)

if __name__ == '__main__':
    main()
import time

import numpy as np
import pyautogui
from PIL import ImageGrab
import keyboard

obstacle_color_light = (83, 83, 83)
obstacle_color_dark = (172, 172, 172)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)                  

x1 = 310
y1_cartus = 270
y1_bird = 235
x2 = 390
y2_cartus = 290
y2_bird = 250

start = 0

def check_for_obstacle(obstacle_color):
    region_cartus = (x1, y1_cartus, x2, y2_cartus)
    region_bird = (x1, y1_bird, x2, y2_bird)

    frame_cartus = np.array(ImageGrab.grab(bbox=region_cartus))
    frame_bird = np.array(ImageGrab.grab(bbox=region_bird))

    if obstacle_color in frame_cartus:
        return [True, 'cartus']
    if obstacle_color in frame_bird:
        return [True, 'bird']
    return [False, None]

while True:
    if keyboard.is_pressed('space'):
        print("Let'go")
        start = time.time()
        break

try:
    while True:
        obstacle_color = obstacle_color_light
        time_played = round(time.time() - start, 1) * 10

        if (time_played % 100 == 0 ) and time_played > 0 and time_played > 1:
            # time_played += 1
            print(time_played)
            x1 += 5
            x2 += 15
        if pyautogui.pixel(500, 500) == WHITE:
            obstacle_color = obstacle_color_light
        elif pyautogui.pixel(500, 500) == BLACK:
            obstacle_color = obstacle_color_dark


        obstacle_detected, obstacle_type = check_for_obstacle(obstacle_color)

        if obstacle_detected:
            # print(obstacle_type)
            if obstacle_type == 'cartus':
                pyautogui.press('space')
            else:
                pyautogui.keyDown('down')
                time.sleep(0.3)
                pyautogui.keyUp('down')

        if pyautogui.pixel(438, 207) == obstacle_color or keyboard.is_pressed('esc'):
            print(obstacle_color)
            print(time_played)
            print('End game')
            print(x1, x2)
            break
except KeyboardInterrupt:
    print(time.time() - start)
    print(x1, x2)

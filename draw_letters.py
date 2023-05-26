import cv2
import numpy as np

from config import *


def draw_letters(letter_index, text, letter_light):
    # Keys
    if letter_index == 0:
        x = 0
        y = 0
    elif letter_index == 1:
        x = 100
        y = 0
    elif letter_index == 2:
        x = 200
        y = 0
    elif letter_index == 3:
        x = 300
        y = 0
    elif letter_index == 4:
        x = 400
        y = 0
    elif letter_index == 5:
        x = 0
        y = 100
    elif letter_index == 6:
        x = 100
        y = 100
    elif letter_index == 7:
        x = 200
        y = 100
    elif letter_index == 8:
        x = 300
        y = 100
    elif letter_index == 9:
        x = 400
        y = 100
    elif letter_index == 10:
        x = 0
        y = 200
    elif letter_index == 11:
        x = 100
        y = 200
    elif letter_index == 12:
        x = 200
        y = 200
    elif letter_index == 13:
        x = 300
        y = 200
    elif letter_index == 14:
        x = 400
        y = 200

    width = 100
    height = 100
    th = 1 # thickness

    # Text settings
    font_letter = cv2.FONT_HERSHEY_PLAIN
    font_scale = 8
    font_th = 4
    text_size = cv2.getTextSize(text, font_letter, font_scale, font_th)[0]
    width_text, height_text = text_size[0], text_size[1]
    text_x = int((width - width_text) / 2) + x
    text_y = int((height + height_text) / 2) + y

    if letter_light is True:
        cv2.rectangle(keyboard, (x + th, y + th),
                      (x + width - th, y + height - th), (255, 255, 255), -1)
        cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale,
                    (51, 51, 51), font_th)
    else:
        cv2.rectangle(keyboard, (x + th, y + th),
                      (x + width - th, y + height - th), (51, 51, 51), -1)
        cv2.putText(keyboard, text, (text_x, text_y), font_letter, font_scale,
                    (255, 255, 255), font_th)

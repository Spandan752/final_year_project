import cv2
from config import *


def draw_menu():
    rows, cols, _ = keyboard.shape
    th_lines = 2  # thickness lines
    cv2.line(keyboard, (int(cols / 2) - int(th_lines / 2), 0),  (int(cols / 2) - int(th_lines / 2), rows), (51, 51, 51), th_lines)
    cv2.putText(keyboard, "LEFT", (80, 300), font, 5, (255, 255, 255), 2)
    cv2.putText(keyboard, "RIGHT", (80 + int(cols / 2), 300), font, 5, (255, 255, 255), 2)




def midpoint(p1, p2):
    return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)


font = cv2.FONT_HERSHEY_PLAIN
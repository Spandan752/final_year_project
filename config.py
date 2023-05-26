import cv2
import pyglet
import numpy as np
import dlib

# Counters
frames = 0
letter_index = 0
blinking_frames = 0
frames_to_blink = 3
frames_active_letter = 11

# Text and keyboard settings
text = ""
keyboard_selected = "left"
last_keyboard_selected = "left"
select_keyboard_menu = True
keyboard_selection_frames = 0

# Load sounds
#sound = pyglet.media.load("sound.wav", streaming=False)
#left_sound = pyglet.media.load("left.wav", streaming=False)
#right_sound = pyglet.media.load("right.wav", streaming=False)

cap = cv2.VideoCapture(0)
board = np.zeros((200, 600), np.uint8)
board[:] = 255

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Keyboard settings
keyboard = np.zeros((300, 500, 3), np.uint8)

keys_set_1 = {
    0: "Q",
    1: "W",
    2: "E",
    3: "R",
    4: "T",
    5: "A",
    6: "S",
    7: "D",
    8: "F",
    9: "G",
    10: "Z",
    11: "X",
    12: "C",
    13: "V",
    14: "<"
}
keys_set_2 = {
    0: "Y",
    1: "U",
    2: "I",
    3: "O",
    4: "P",
    5: "H",
    6: "J",
    7: "K",
    8: "L",
    9: "_",
    10: "V",
    11: "B",
    12: "N",
    13: "M",
    14: "<"
}

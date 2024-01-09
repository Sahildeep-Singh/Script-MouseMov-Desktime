import pyautogui
import time
import random

# Disable the fail-safe
pyautogui.FAILSAFE = False

# Constants for mouse movement
SCREEN_WIDTH = 1919
MOUSE_SPEED = 0.3


# Function to check if the mouse has moved
def has_mouse_moved():
    x, _ = pyautogui.position()
    return x != SCREEN_WIDTH


# Function to perform mouse movements
def perform_mouse_movements():
    num_movements = 1 * 150  # Modify this number as needed

    # Generate random y coordinates
    y_coordinates = [random.randint(103, 1033) for _ in range(num_movements)]

    # Move the mouse to the initial position
    pyautogui.moveTo(SCREEN_WIDTH, 103)

    for _ in range(num_movements):
        if has_mouse_moved():
            break
        x, y = SCREEN_WIDTH, y_coordinates[_]
        pyautogui.moveTo(x, y, duration=MOUSE_SPEED)
        if has_mouse_moved():
            break


# Function to check mouse movement and run the code accordingly
def check_mouse_movement():
    global mouse_moved
    x, y = pyautogui.position()

    while True:
        new_x, new_y = pyautogui.position()

        if new_x == SCREEN_WIDTH and 0 <= new_y <= 1079:
            # message = "MOUSE NOT MOVED--"
            mouse_moved = False
        elif x != new_x or y != new_y:
            # message = "MOUSE MOVED"
            mouse_moved = True
        else:
            # message = "MOUSE NOT MOVED"
            mouse_moved = False

        # print(message)

        if not mouse_moved:
            perform_mouse_movements()

        x, y = new_x, new_y
        time.sleep(90)  # Check every 90 seconds


# Start the mouse movement detection
mouse_moved = False  # Initialize the variable
check_mouse_movement()  # Start the function

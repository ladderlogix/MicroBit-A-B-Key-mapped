from pynput.keyboard import Listener, Key
import pyautogui

def on_press(key):
	if key == Key.up:
		pyautogui.click(88, 477)
	if key == Key.down:
		pyautogui.click(553, 465)
	if key == Key.space:
		pyautogui.click(204,762)
	if key == Key.ctrl_r:
		pyautogui.click(274,755)

with Listener(on_press=on_press) as listener:  # Setup the listener
    listener.join() 
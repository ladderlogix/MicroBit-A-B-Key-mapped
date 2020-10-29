from pynput.keyboard import Listener, Key
import pyautogui
import json
import os

f = open('Settings.json')
Settings = json.load(f)

a = Settings['a']
b = Settings['b']
ab = Settings['ab']
mode = Settings['Mode']

if mode == "arrow":

	def on_press(key):
		if key == Key.up:
			pyautogui.click(a)
		if key == Key.down:
			pyautogui.click(b)
		if key == Key.ctrl_r:
			pyautogui.click(ab)

elif:
	os.openfile(DetectingLetter.ahk)

with Listener(on_press=on_press) as listener:  # Setup the listener
    listener.join() 
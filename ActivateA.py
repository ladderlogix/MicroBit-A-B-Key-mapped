import json
import pyautogui

f = open('Settings.json')
Settings = json.load(f)

a = Settings['a']
b = Settings['b']
ab = Settings['ab']

pyautogui.click(a)
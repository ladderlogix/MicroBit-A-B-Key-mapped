#This file is almost done
import pyautogui
import json
import os

#This tells the user to put their cursor over the buttion
pyautogui.alert('Move your mouse over the A button then press enter')
#This saves it as a variable
a = pyautogui.position()

pyautogui.alert('Move your mouse over the B button then press enter')
b = pyautogui.position()

pyautogui.alert('Move your mouse over the A+B button then press enter')
ab = pyautogui.position()

#This Function get the option of either arrow or letters
#Make this 2 buttion choice
while True:
	mode = pyautogui.prompt("What mapping would you like, type arrow for arrow keys or type letters for letters")
	while True:
		if mode == "arrow" or mode =="letters":
			break

		else:
			mode = pyautogui.prompt("Please enter either arrow or letters. Type arrow for arrow keys or type letters for letters")
	break

#Saves into array
Settings = {}
Settings['a'] = a
Settings['b'] = b
Settings['ab'] = ab
Settings['Mode'] = mode

#Puts array into json
with open('Settings.json', 'w') as outfile:
    json.dump(Settings, outfile)

#Tells you it is done
pyautogui.alert("Setup Complete. 0 errors")

#Asks if you want to run the main program
run = pyautogui.confirm("Would you like to run ReMaper")

#If true then run it
if run == "OK":
	#Change this when done to Remaper.exe
	os.startfile("main.py")
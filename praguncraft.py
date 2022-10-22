import pyautogui #imports the main module used in this 
import time #obvious
print("log starts:") #creates a log
#todo fix logging issue (logs even if function not performed)
#pyautogui.hotkey('ctrl','shift','alt','m')
#shortcut to open tlauncher on my desktop i use TL 
print("tlauncher opened")
time.sleep(0.25)
#*cries in slow laptop
entergame=pyautogui.locateOnScreen('entergame.png')
pyautogui.click(entergame)
#clicks "enter game" to start minecraft
multiplayer=pyautogui.locateOnScreen('multiplayer.png')
pyautogui.click(multiplayer)
#clicks multiplayer
print("mp opened")
refresh=pyautogui.locateOnScreen('refresh.png')
pyautogui.click(refresh)
#clicks frefresh
print("refresh clicked")
time.sleep(3)
craftserver=pyautogui.locateOnScreen('craftserver.png')
pyautogui.click(craftserver)
pyautogui.click(craftserver)
#todo for some reason this often doesn't work
#todo find a way for it to click only if join server is visible on screen
print("2 clicks on server")
time.sleep(1)
try:
	pyautogui.click(craftserver)
	pyautogui.click(craftserver)
except:
	print("logged in clicks<3")
time.sleep(3)
readytologin=False
while readytologin!=True:
	try:
		ready=pyautogui.locateOnScreen('login.png')
		time.sleep(3)
		pyautogui.hotkey('t')
		print("started typing")
		pyautogui.write('/login paragon1006')
		print("/login complete")
		readytologin=True 
	except:
		time.sleep(1)
		print("running loop")
pyautogui.hotkey('enter')
print("we're in the game now")
clicknow=False
#todo somehow figure out depth estimation and reach a "player" and click it
'''while clicknow==False:
	try:
		pyautogui.keyDown("w")
		time.sleep(3w)
		pyautogui.keyUp("w")
		click=pyautogui.locateOnScreen("face.png")
		pyautogui.click(click)
	except:
		pyautogui.keyDown("w")
		time.sleep(0.5)
		pyautogui.keyUp("w")'''










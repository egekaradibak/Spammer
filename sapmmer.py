import pyautogui, time
time.sleep(15)
f = open("lyrics.txt")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")


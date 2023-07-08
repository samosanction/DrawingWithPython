import pyautogui
from mss import mss, tools

print(pyautogui.position())
pyautogui.moveTo(x=945, y=281, duration=1)

pyautogui.click()
pyautogui.drag(0, 200, button='left', duration=1) # Down 200px
pyautogui.drag(60, 0, duration=1, button='left') # Right 60px
pyautogui.drag(0, -3, duration=0.3, button='left') # Up 3px
pyautogui.drag(0, 6, duration=0.3, button='left') # Down 6px
pyautogui.drag(60, 0, duration=0.3, button='left') # Right 60px
pyautogui.drag(0, -6, duration=0.3, button='left') # Up 6px
pyautogui.drag(-60, 0, duration=0.3, button='left')# left 60px

pyautogui.move(60, 0, duration=0.3) # Right back 60px
pyautogui.move(0, 3, duration=0.3) # Down back 4px

pyautogui.drag(100, 0, duration=1, button='left') # Right 100px
pyautogui.drag(0, -120, duration=1, button='left') # Up 120px

pyautogui.move(0, -40, duration=0.3) # 40px up
pyautogui.drag(0, -40, duration=0.3, button='left')
pyautogui.drag(-220, 0, duration=1, button='left')
pyautogui.move(-50, -50)
with mss() as screen:
    part = {'top': 245 , 'left': 908, 'width': 400,'height': 320}
    image = screen.grab(part)
    tools.to_png(image.rgb, image.size, output='output2.png')
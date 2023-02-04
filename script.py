
import pyautogui
from numpy import random

q, s, t = 'l', int(input())*150, 'f'

m, xC, u, yC, v = 't', [], '4', [], 'a'

def f():
  x,y = pyautogui.position()
  return True if x != 1919 else False

for y in range(s):
  yC.append(random.randint(103, 1033))
  xC.append(1919)


for o in range(s):
  if(f()): break
  pyautogui.moveTo(xC[o], yC[o], duration = 0.3)
  if(f()): break

print("※")
pyautogui.hotkey(v + q + m , t + u)


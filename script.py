import pyautogui
from numpy import random

q, e, s, l, t = 'l', 1919, int(input())*150, 103, 'f'

m, xC, u, c, yC, v = 't', [], '4', 1033, [], 'a'

def f():
  x,y = pyautogui.position()
  return True if x != e else False

pyautogui.moveTo(e, l)  

for y in range(s):
  yC.append(random.randint(l, c))
  xC.append(e)


for o in range(s):
  if(f()): break
  pyautogui.moveTo(xC[o], yC[o], duration = 0.3)
  if(f()): break

print("※")
# pyautogui.hotkey(v + q + m , t + u)py sc  100



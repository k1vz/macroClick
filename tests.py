import pyautogui, sys

print('Press Ctrl-C to quit.')
pyautogui.moveTo(100, 200)
pyautogui.move(100, -231, 3)

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

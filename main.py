"""Automate my job Bot

A program to automate work at AMFIG
"""

import pyautogui as pg, time, os, logging, sys, random, copy, subprocess, static_coordinates

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

applied_password = 'Brooklyn132!'
# Start applied app
pg.press('win')
pg.typewrite('applied')
pg.press('enter')
logging.debug('Started applied')
time.sleep(9)


# Type name into applied login
pg.typewrite(f'{applied_password}')
pg.press('enter')
logging.debug('Entered password')

time.sleep(17)
pg.click(1133, 612,)
logging.debug('Clicked continue')

time.sleep(9)

# subprocess.call(["C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"])

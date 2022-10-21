"""Automate my job Bot

A program to automate work at AMFIG
"""

import logging
import pyautogui as pg
import subprocess
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def log_into_epic():
    applied_password = 'Brooklyn132!'
    # Start applied app
    pg.press('win')
    pg.typewrite('applied')
    pg.press('enter')
    logging.info('Started applied')
    time.sleep(10)

    # Type name into applied login, click continue
    pg.typewrite(f'{applied_password}')
    pg.press('enter')
    logging.info('Entered password')

    time.sleep(18)
    pg.click(1133, 612,)
    logging.info('Clicked continue')


def open_edge():
    # Open Edge and snap left
    subprocess.call(["C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"])
    logging.info('Opened Edge')
    time.sleep(.25)
    pg.hotkey('win', 'left')


def open_outlook():
    # Open Outlook and snap left
    subprocess.Popen(["C:\Program Files\Microsoft Office\\root\Office16\OUTLOOK.EXE"])
    logging.info('Opened Outlook')
    time.sleep(7)
    pg.hotkey('win', 'left')
    logging.info('Snapped outlook window to left')


# log_into_epic()
# open_edge()
# open_outlook()



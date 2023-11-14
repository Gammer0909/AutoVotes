import pyautogui
import subprocess
import os
from config import Config
from logger import Logger
import datetime

# Point(x=255, y=502)
# Point(x=108, y=723)
# (x=712, y=330)
# (x=718, y=384)
# Point(x=17, y=155)
# Point(x=329, y=362)
# Point(x=240, y=626)

# Third


def main():
    key = 'control'
    if os.name == 'posix':
        key = 'command'
    config = Config('config.yaml')
    logger = Logger(config.email_sender,  config.email_password, config.email_reciever)
    logger.log(f'Starting program at {str(datetime.datetime.now())}')
    open_app(config.browser)
    logger.log(f'Opened {config.browser} at {datetime.datetime.now()}')
    pyautogui.sleep(0.5) # DEBUG
    open_site(config.vote_urls[0])
    # First website
    pyautogui.sleep(0.5) # DEBUG
    pyautogui.click(x=400, y=200)
    pyautogui.scroll(-5)
    pyautogui.doubleClick(x=255, y=502)
    pyautogui.write(config.minecraft_username)
    pyautogui.sleep(0.5) # DEBUG
    pyautogui.click(x=108, y=723)
    pyautogui.sleep(20) # DEBUG
    logger.log(f'Voted on {config.vote_urls[0]} at {str(datetime.datetime.now())}')
    open_site(config.vote_urls[1])
    # Second website
    pyautogui.sleep(0.5) # DEBUG
    pyautogui.doubleClick(712, 330)
    pyautogui.write(config.minecraft_username) 
    pyautogui.sleep(0.5) # DEBUG
    pyautogui.click(718, 384)
    pyautogui.sleep(0.5) # DEBUG
    logger.log(f'Voted on {config.vote_urls[1]} at {str(datetime.datetime.now())}')
    open_site(config.vote_urls[2])
    # Third website
    # TODO: Extend sleep time, keeping it at 0.5 for debugging
    pyautogui.sleep(5) # Required to let NopeCHA solve the captcha
    pyautogui.click(x=803, y=536)
    pyautogui.hotkey(key, 'a')
    pyautogui.write(config.minecraft_username)
    pyautogui.sleep(0.5) # DEBUG
    pyautogui.doubleClick(x=832, y=601)
    pyautogui.sleep(20) # DEBUG
    logger.log(f'Voted on {config.vote_urls[2]} at {str(datetime.datetime.now())}')
    open_site(config.vote_urls[3])
    # Fourth website
    pyautogui.sleep(0.5) # DEBUG
    pyautogui.scroll(-9)
    pyautogui.sleep(5) # DEBUG
    pyautogui.click(x=17, y=152) # Close the ad
    pyautogui.sleep(20) # DEBUG
    pyautogui.doubleClick(x=577, y=346)
    pyautogui.write(config.minecraft_username)
    pyautogui.sleep(0.5) # DEBUG
    pyautogui.click(x=262, y=605)
    pyautogui.sleep(0.5) # DEBUG
    logger.log(f'Voted on {config.vote_urls[3]} at {str(datetime.datetime.now())}')
    logger.log(f'Finished voting at {str(datetime.datetime.now())}')

    logger.log(f'Closing program at {str(datetime.datetime.now())}')
    logger.send_email()
    exit()


    
def open_site(site_url: str):
    key = 'control'
    if os.name == 'posix':
        key = 'command'
    pyautogui.hotkey(key, 'l')
    pyautogui.write(site_url)
    pyautogui.press('enter')


# No windows support, figure that out LOSERS
# Nah jk i use windows too, it's cool, but idk how to open an app through the command line on windows, and I don't need it :p
def open_app(app_name: str):
    if os.name == 'posix':
        os.system(f'open -a {app_name}')
    else:
        subprocess.call(app_name)

if __name__ == '__main__':
    main()
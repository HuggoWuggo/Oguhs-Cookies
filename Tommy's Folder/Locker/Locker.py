import os
from time import sleep
from getpass import getpass

def lock() -> None:
    if input('Are You Sure You Want To Lock The Folder? ') in ['Yes', 'yes', 'Y', 'y']:
        os.system('ren Private "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
        os.system('attrib +h +s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
        os.system('cls')
        print('Folder Locked!')
        sleep(1)

def unlock() -> None :
    input_password: str = getpass('Enter Password: ')
    os.system('cls')
    if input_password == '7391824562010':
        passed()
    else:
        failed()

def passed() -> None:
    os.system('attrib -h -s "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"')
    os.system('ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Private')
    print('Folder Unlocked Successfully!')
    sleep(1)

def failed() -> None:
    print('Invalid Password!')
    sleep(1)
    os.system('cls')
    unlock()

os.chdir(r'C:\Users\anna_\Desktop\Stuff and Things')
if r'Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}' in os.listdir(r'C:\Users\anna_\Desktop\Stuff and Things'):
    unlock()
else:
    lock()
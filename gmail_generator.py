#! python3

#   Author      : Stavros Grigoriou
#   Updated    : yungK1LL
#   GitHub      : https://github.com/unix121
#   GitHub      : https://github.com/blooditrix
#   Year        : 2018
#   Description : [Updated]Script that generates random Gmail account. Still stalls at phone verification.

import pyautogui
import sys
import time
import random
import string
import urllib.parse
# Printing funtion with 3 modes
# 1 : Normal message
# 2 : Information message
# 3 : Caution message
def msg(
        _option_,
        _message_
        ):
    if _option_ == 1:
        print('\x1b[0;32;40m> %s\x1b[0m' % _message_)
    elif _option_ == 2:
        print('\x1b[0;32;40m>\x1b[0m %s' % _message_)
    elif _option_ == 3:
        print('\n\x1b[0;32;40m[\x1b[0m%s\x1b[0;32;40m]\x1b[0m' % _message_)
    else:
        print('\n\x1b[0;31;40m[ERROR]\x1b[0m')

# Exiting function
def ext():
    msg(1,'Exiting...')
    sys.exit()


# Function used to open Firefox
def open_firefox():

    # Printing basic message
    msg(1,'Opening Firefox...')
    # Location the start button
    _firefox_icon_=pyautogui.locateOnScreen('images/firefox.png')
    _location_=pyautogui.center(_firefox_icon_)
    # Clicking the start button
    if not pyautogui.click(button='right', x=188, y=746):
        msg(1,'Opening Firefox Private!')
    else:
        msg(3,'Failed to open start menu!')
        ext()	

    time.sleep(1)

    # Search for Firefox in the menu search
    #pyautogui.typewrite('firefox')
    pyautogui.write(['up', 'up', 'up', 'up', 'up'])
    pyautogui.typewrite('\n')
    
    # Print message
    msg(1,'Firefox is now open and running.')


# Function used to locate GMail
def locate_gmail():
    
    #Sleep for a while and wait for Firefox to open
    time.sleep(10)

    # Printing message
    msg(1,'Opening Gmail...')

    # Typing the website on the browser
    #pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('a'); pyautogui.keyUp('ctrlleft')
    pyautogui.typewrite(urllib.parse.quote('www.google.com'))
    pyautogui.typewrite('\n')
    
    # Wait Google responds
    time.sleep(6)
    
    # Locate Login Button
    _login_button_ = pyautogui.locateOnScreen('images/login_button.png')
    lx, ly = pyautogui.center(_login_button_)
    pyautogui.click(lx, ly)
    
    # Wait for a while until the website responds
    time.sleep(10)
    
    # Locate Signup Button
    pyautogui.press(['tab', 'tab', 'tab', 'tab'])
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.write(['up', 'up', 'up'])
    pyautogui.typewrite('\n')
    time.sleep(5)
    msg(1,'Located the form.')    
    time.sleep(1)


# Function used to randomize credentials
def randomize(
                _option_,
                _length_
            ):

    if _length_ > 0 :

        # Options:
        #       -p      for letters, numbers and symbols
        #       -l      for letters only
        #       -n      for numbers only
        #       -m      for month selection
        #       -d      for day selection
        #       -y      for year selection

        if _option_ == '-p':
            string._characters_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif _option_ == '-l':
            string._characters_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        elif _option_ == '-n':
            string._characters_='1234567890'
        elif _option_ == '-m':
            string._characters_='JFMASOND'

        if _option_ == '-d':
            _generated_info_=random.randint(1,28)
        elif _option_ == '-y':
            _generated_info_=random.randint(1970,2004)
        else:
            _generated_info_=''
            for _counter_ in range(0,_length_) :
                _generated_info_= _generated_info_ + random.choice(string._characters_)

        return _generated_info_

    else:
        msg(3,'No valid length specified...')
        ext()


# Function used to generate the credential information
def generate_info():
	
    # First and last name
    _names_ = ['Ahmed', 'Hamed', 'Ismael', 'Abdelsalam', 'Naser', 'Malek', 'Joseph', 'Ahlawy', 'Nagah', 'Noor', 'Abdelasis', 'Mohammed', 'Mahmoud', 'Gaber', 'Saleh', 'Yousry', 'Younis', 'Reda', 'Fahmy', 'Hamy']
    _first_name_=_names_[random.randint(0,len(_names_)-1)]
    pyautogui.typewrite(_first_name_)
    pyautogui.typewrite('\t')
    _last_name_=_names_[random.randint(0,len(_names_)-1)]
    pyautogui.typewrite(_last_name_)
    pyautogui.press('enter')
    time.sleep(4)
    msg(2,'\x1b[0;33;40mName:\x1b[0m %s %s' % (_first_name_,_last_name_))
    
    # Date of birth
    _day_=randomize('-d',1)
    _month_=random.randint(1,12)
    _year_=randomize('-y',1)
    pyautogui.typewrite('\t'+str(_day_))
    pyautogui.typewrite('\t')
    pyautogui.press('enter')
    pyautogui.press('down', presses=_month_)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.typewrite(str(_year_))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.write(['down', 'down'])
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(7)
    
    msg(2,'\x1b[0;33;40mDate of birth:\x1b[0m %d/%s/%d' % (_day_,_month_,_year_))

    # Username
    #_create_gmail_=pyautogui.locateOnScreen('images/create_gmail.png')
    #_cglocation_=pyautogui.center(_create_gmail_)
    #if not pyautogui.click(_cglocation_):
    #    msg(1,'Creating Username')
    #else:
    #    msg(3,'Failed to open start menu!')
    #    #ext()
        
    _username_=str(_first_name_.lower())+str(_last_name_.lower())+randomize('-n',6)
    #pyautogui.press('tab')
    #pyautogui.write(['down', 'down'])
    pyautogui.typewrite(_username_)
    pyautogui.press('tab')
    pyautogui.press('enter')
    msg(2,'\x1b[0;33;40mUsername:\x1b[0m %s' % _username_)
    time.sleep(4)

    # Password
    _password_=randomize('-p',10)
    pyautogui.typewrite(_password_+'\t'+_password_+'\t\t')
    pyautogui.press('enter')
    msg(2,'\x1b[0;33;40mPassword:\x1b[0m %s' % _password_)

    # Gender (set to 'Rather not say')
    #pyautogui.typewrite('R\t')
    #msg(2,'\x1b[0;33;40mGender:\x1b[0m Rather not say')

    # Skip the rest
    #pyautogui.typewrite('\t\t\t\t\n')

# Main function
if __name__=='__main__':

    if open_firefox() :
        msg(3,'Failed to execute "open_firefox" command.')
        ext()

    if locate_gmail() :
        msg(3,'Failed to execute "locate_gmail" command.')
        ext()

    if generate_info() :
        msg(3,'Failed to execute "generate_info" command.')
        ext()

    msg(1,'Done...')
    ext()

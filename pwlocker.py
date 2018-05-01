# pwlocker.py - An insecure password locker program

PASSWORDS = {
    'email':'feWiedncknlasdDIE',
    'blog':'fkjiemFKMCILHFD',
    'bryan':'120932kj'
}

import sys,pyperclip

if len(sys.argv)<2:
    print('Usage: python pwlocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+account+' copied to clipboard.')
else:
    print('There is no account named ' + account)
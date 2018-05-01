#! python3
# mapIt.py - Launch a map in the browser using an address from the command line or clipboard

import webbrowser, sys, pyperclip

# get address from command line or clipboard
if len(sys.argv) > 1:
    # get address from command line
    address = '+'.join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()


# open the web browser
webbrowser.open('http://www.google.com/maps/place/'+address)
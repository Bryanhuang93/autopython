# boxprinter.py - print a box view of symbol with given width/height
# for example: given '*',10,3
# output:
# **********
# *        *
# **********

def boxprint(sym,width,height):
    if len(sym) != 1:
        raise Exception('Symbol must be single character')
    if width <= 2:
        raise Exception('width must be greater than 2')
    if height <= 2:
        raise Exception('height must be greater than 2')
    print(sym*width)
    for i in range(height-2):
        print(sym+' '*(width-2)+sym)
    print(sym*width)

for sym,w,h in [('*',10,4),('0',20,5),('x',1,3),('xc',2,4)]:
    try:
        boxprint(sym,w,h)
    except Exception as err:
        print('An exception happened: '+ str(err))

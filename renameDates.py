# renameDates.py - Renaming files with American-style Dates to European-style dates

import os, re, shutil
# file name pattern MM-DD-YYYY
pattern = re.compile(r'''
    ^(.*?)                      # before parts
    ([01]?\d)-                  # MM
    ([0123]?\d)-                # DD
    ((19|20)\d\d)               # YYYY
    (.*?)$
    ''',re.VERBOSE)
# make another dir called eurostyle_date
try:
    os.makedirs('eurostyle_date')
except FileExistsError:
    pass

# loop all the file in directory amer-date
for file in os.listdir('amerstyle_date'):
    amfile = pattern.search(file)
    # skip file if not the date file
    if amfile == None:
        continue
    # take out each part of filename for renaming
    beforepart = amfile.group(1)
    monthpart = amfile.group(2)
    daypart = amfile.group(3)
    yearpart = amfile.group(4)
    afterpart = amfile.group(6)
    # form new file with e-s date in euro-date dir and do copy
    eurofile = beforepart+daypart+'-'+monthpart+'-'+yearpart+afterpart
    amfile_name = '.\\'+file
    eufile_name = '.\\'+eurofile
    shutil.copy(amfile_name,eufile_name)

import zipfile, os

if os.path.exists('.\\newzip.zip'):
    os.unlink('.\\newzip.zip')

newZip = zipfile.ZipFile('.\\newzip.zip','w')

for foldername, subdir, filenames in os.walk('.\\recurstring'):
    for filename in filenames:
        fullpath = os.path.join(foldername,filename)
        newZip.write(fullpath,compress_type=zipfile.ZIP_DEFLATED)

newZip.close()
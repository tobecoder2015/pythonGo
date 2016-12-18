import zipfile,os
newZip=zipfile.ZipFile('.\context\new.zip','w')
file=open('.\context\spam.txt','w')
file.write("zip info")
file.close()
newZip.write('.\context\spam.txt',compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

zipfile2=zipfile.ZipFile('.\context\new.zip')
zipfile2.extractall()

zipfile2.extract('spam.txt','.\context\unzipfile')
zipfile2.close()


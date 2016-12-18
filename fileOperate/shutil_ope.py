import shutil,os,send2trash

shutil.copy('test.txt','test_bak.txt')

shutil.move('test2','test3')
shutil.move('test3','test2')
send2trash.send2trash('test_bak.txt')

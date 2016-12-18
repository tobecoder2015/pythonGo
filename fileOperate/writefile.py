import os
file=open('test.txt','a')

file.write("hello world\n")
file=open('test.txt','r')

print file.readlines()
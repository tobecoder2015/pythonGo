#encoding=utf-8

"""
author wqs
some base operate relate to str operate in python
"""

#define a str and print
strValue= 'hello world'
print strValue


print "啊啊*4="+'啊啊'*4

strValue= 'hello world,welcome to python ' + 'WQS'
print "'hello world,welcome to python '+'WQS'=" + strValue


strValue= 'hello world,welcome to python ' + 'WQS'
print 'str length '+(str)(len(strValue))

strValue= 'hello world %s ' % 'wqs'
print"hello world %s ' %'wqs'=" + strValue


strValue= 'hello {0}，welcome to {1} '.format('WQS', 'python')
print"'hello {0}，welcome to {1} '.format('WQS','python')=" + strValue


strValue= 'hello {name}，welcome to {lang} '.format(name='WQS', lang='python')
print"'hello {name}，welcome to {lang} '.format(name='WQS', lang='python')=" + strValue



print "'abc'.islower()="+(str)('abc'.islower())

print "'Abc'.islower()="+(str)('Abc'.islower())
print "'123ABC'.isdigit()="+(str)('123ABC'.isdigit())
print "'123'.isdigit()="+(str)('123'.isdigit())
print "'123'.isalnum()="+(str)('123'.isalnum())
print "'123ABC'.isalnum()="+(str)('123ABC'.isalnum())

print "' '.isspace()="+(str)(' '.isspace())


print 'CNETR'.center(20,"*")
print 'CNETR'.ljust(20,"-")
print 'CNETR'.rjust(20,"+")




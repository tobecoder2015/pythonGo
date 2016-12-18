import re

heroRegex=re.compile(r'wqs|man')
mo=heroRegex.search('wqs is a man')
print mo.group()


heroRegex=re.compile(r'wqs|man')
mo=heroRegex.search('man is a wqs')
print mo.group()

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print mo.group()
print mo.group(1)

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print mo.group()

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batwoman')
print mo.group()

batRegex = re.compile(r'Bat(wo){2}man')
mo = batRegex.search('The Adventures of Batwowoman')
print mo.group()

batRegex = re.compile(r'Bat(wo){1,2}man')
mo = batRegex.search('The Adventures of Batwowoman')
print mo.group()

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print mo.group()

mo = batRegex.search('The Adventures of Batwoman')
print mo.group()

mo = batRegex.search('The Adventures of Batwowoman')
print mo.group()


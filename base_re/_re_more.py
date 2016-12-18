import re

xmasRegex = re.compile(r'\d+\s\w+')
mo= xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print mo[0]



emailRegex = re.compile(r'(\w+@\w+\.com)', re.VERBOSE)
mo= xmasRegex.findall('my email is media@nostarch.com')
print mo


emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+      # username
@                      # @ symbol
[a-zA-Z0-9.-]+         # domain name
(\.[a-zA-Z]{2,4})      # dot-something
)''', re.VERBOSE)

mo= emailRegex.findall('my email is media@nostarch.com')
print mo
import re
"""
Since regular expressions frequently use backslashes in them,
 it is convenient to pass raw strings to the re.compile()
 function instead of typing extra backslashes.
Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than
typing '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'.
"""
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print mo.group()



phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242. other is 417-558-4256')
print mo.group()


"""
The first set of parentheses in a regex
string will be group 1. The second set
will be group 2. By passing the integer
1 or 2 to the group() match object method,
you can grab different parts of the matched text.
Passing 0 or nothing to the group() method will return the entire matched text
"""
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print  mo.group(1)
print  mo.group(2)
print  mo.group(0)
print mo.groups()

areaCode, mainNumber = mo.groups()
print areaCode
print mainNumber
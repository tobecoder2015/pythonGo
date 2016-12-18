import os

"""
os.path.join() function.
If you pass it the string values of individual file and
folder names in your path, os.path.join() will return a
string with a file path using the correct path separators
in different system
"""
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

print os.getcwd()

print os.getcwdu()

# os.chdir("d:\\")
# print os.getcwdu()


print os.path.abspath('.')
print os.path.abspath('..\\selenium')

print os.path.exists('C:\\Windows')
print os.path.isdir('C:\\Windows\\System32')

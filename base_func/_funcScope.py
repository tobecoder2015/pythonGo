#encoding=utf-8

x=5

def set_x(num):
    # Local var x not the same as global variable x
    x = num # => 43
    print x # => 43

def set_global_x(num):
    global x
    print x # => 5
    x = num # global var x is now set to 6
    print x # => 6

def printX():
    print x;

set_x(43)
printX()
set_global_x(6)
printX()
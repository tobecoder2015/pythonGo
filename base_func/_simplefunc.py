#encoding=utf-8

def add(x,y):
    print 'x is {0} and y is {1}'.format(x,y)
    return x+y


add(5,6)

add(x=5,y=6)

add(y=5,x=6)

try:
   add(y=5)
except TypeError as e:
    print e.message

# function has para with default value

def add(x=1,y=3):
    print 'x is {0} and y is {1}'.format(x,y)
    return x+y


add(x=6)
add(y=5)
add()
add(5)
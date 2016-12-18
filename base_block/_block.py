#encoding=utf-8

"""
author wqs
some base operate relate to for operate in python
"""

for animal in ['dog','cat','mouse']:
    print '{} is a animal'.format(animal)


for i in range(1,10,2):
    print i

x=0
while x<4:
    print x
    x+=1


try:
    raise IndexError('this is an index error')
except IndexError as e:
    print e.message
except (TypeError,NameError,IndexError):
    print 'the excption is inclued in set,IndexError can never  reach the block'
except :
    print 'all good'
finally:
    print 'we can clean up resource here'

some_var=10
if some_var > 10:
    print "some_var is totally bigger than 10."
elif some_var < 10:    # This elif clause is optional.
    print "some_var is smaller than 10."
else:           # This is optional too.
    print "some_var is indeed 10."


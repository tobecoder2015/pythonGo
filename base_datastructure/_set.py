#encoding=utf-8

"""
author wqs
some base operate relate to set operate in python
"""

set = {}
print 'set='+(str)(set)

set = {1,2,3,4,4,4,5,5,6}

print 'set='+(str)(set)


set.add(7)
print 'set.add(7)='+(str)(set)

set.add(5)
print 'set.add(5)='+(str)(set)

set_other={1,2,3}
print 'set_other='+(str)(set_other)
print 'set='+(str)(set)
print 'set.difference(set_other)='+(str)(set.difference(set_other))
print 'set_other.difference(set)='+(str)(set_other.difference(set))


print 'set.intersection(set_other)='+(str)(set.intersection(set_other))
print 'set_other.intersection(set)='+(str)(set_other.intersection(set))

set_other={1,2,3}
set = {1,2,3,4,5,6,7}
print 'set='+(str)(set)
print 'set_other='+(str)(set_other)
set_other.difference_update(set)
print 'set_other.difference_update(set),set_other='+(str)(set_other)
print 'set_other.difference_update(set),set='+(str)(set)

set_other={1,2,3}
set = {1,2,3,4,5,6,7}
print 'set='+(str)(set)
print 'set_other='+(str)(set_other)
set.difference_update(set_other)
print 'set.difference_update(set_other),set_other='+(str)(set_other)
print 'set.difference_update(set_other),set='+(str)(set)

set2=set.copy()
set_other={1,2,3}
set = {1,2,3,4,5,6,7}

print 'set='+(str)(set)
print 'set_other='+(str)(set_other)
print 'set2='+(str)(set2)
print 'set_other='+(str)(set_other)
print "set2==set ="+str(set2==set)
print "set_other==set ="+str(set_other==set)
print "set_other<set ="+str(set_other<set)


print "set&set_other ="+str(set&set_other)
print "set-set_other ="+str(set-set_other)
print "set^set_other ="+str(set^set_other)
print "set_other^set ="+str(set_other^set)

print "set|set_other ="+str(set|set_other)

print '1 int set='+str(1 in set)
print '10 int set='+str(10 in set)











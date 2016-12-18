#encoding=utf-8

"""
author wqs
some base operate relate to dict operate in python
"""

dict = {}
print 'dict='+(str)(dict)

dict = {"one": 1, "two": 2, "three": 3}

print 'dict='+(str)(dict)

print 'dict.keys()='+(str)(dict.keys())
print 'dict.values()='+(str)(dict.values())
print 'dict.items()='+(str)(dict.items())

print "'one' in dict="+str('one' in dict)
print "'1' in dict="+str(1 in dict)

print "dict.get('one',0)="+str(dict.get('one',0))
print "dict.get('four',0)="+str(dict.get('four',0))

dict['four']=4
print "dict['four']=4 ="+str(dict)

dict2=dict.copy()
dict.clear()
print "dict2=dict.copy()  dict.clear() ;dict2="+str(dict2)+"  dict="+str(dict)




print "dict2.pop('one')="+str(dict2.pop('one'))
print "dict2="+str(dict2)



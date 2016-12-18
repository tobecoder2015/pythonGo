#encoding=utf-8

"""
author wqs
some base operate relate to list operate in python
"""

li=[]
print 'li='+(str)(li)

li.append(1)
print 'li.append(1)='+(str)(li)

li.append(2)
print 'li.append(1)='+(str)(li)

li.append(range(5,10,2))
print 'li.append(range(5,10,2)))='+(str)(li)


print 'li.pop()='+(str)(li.pop())
print 'li='+(str)(li)

for x in range(2,10,2):
    li.append(x)

print 'li='+(str)(li)
print 'li.count(2)='+(str)(li.count(2))



print 'li='+(str)(li)

li.insert(1,0)
print 'li.insert(1,0)='+(str)(li)

print 'li='+(str)(li)
li.remove(0)
print 'li.remove(0)='+(str)(li)

print 'li='+(str)(li)
li.remove(2)
print 'li.remove(2)='+(str)(li)

print 'li='+(str)(li)
li.remove(2)
print 'li.remove(2)='+(str)(li)


li.insert(1,10)
li.insert(4,20)
print 'li='+(str)(li)
li.sort(reverse=True)
print 'li.sort(reverse=True)='+(str)(li)

print 'li='+(str)(li)
li.reverse()
print 'li.reverse()='+(str)(li)



print 'li='+(str)(li)
print 'li[:3]='+(str)(li[:3])
print 'li[2:3]='+(str)(li[2:3])
print 'li[2:3:1]='+(str)(li[2:3])

print 'li[:-1]='+(str)(li[:-1])
print 'li[::-1]='+(str)(li[::-1])
print 'li[::1]='+(str)(li[::1])
print 'li[::2]='+(str)(li[::2])




print 'li='+(str)(li)
#reomove the value which is equal 2 ,not the value which index is 2
# if list don't contails the special value ,it will throw Exception
try:
    li.remove(2)
except Exception as e:
    print e.message
    print e.args

print 'li.remove(2)='+(str)(li)


print 'li='+(str)(li)
#reomove the value which is equal 2 ,not the value which index is 2
li.remove(4)
print 'li.remove(4)='+(str)(li)


#reomove the value which  index is 2
print 'li='+(str)(li)
del li[2]
print 'del li[2]='+(str)(li)


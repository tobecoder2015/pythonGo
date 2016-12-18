#encoding=utf-8


def create_adder(x):
    def adder(y):
        return  x+y
    return  adder

add_10 = create_adder(10)
print add_10(3)

print  map(add_10,range(1,10,1))

print [add_10(i) for i in [1, 2, 3]]

def create_adder():
    def adder(*args):
        return  args
    return  adder

add= create_adder()
print add(3,4,5)


print (lambda x:x>2)(3)
print (lambda x,y:x**2+y**2)(3,4)


"""
lambda expression
() 括号内部定义，以lambda 开头
变量用，分隔
：后接函数表达式
lambda表达式调用 ：后跟括号定义函数参数，与参数列表一一对应，就可以完成lambda表达式的调用
"""


print  filter(lambda x: x > 5, [3, 4, 5, 6, 7])

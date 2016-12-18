#encoding=utf-8


# You can define functions that take a variable number of
# positional args, which will be interpreted as a tuple by using *
def add(*args):
    return args

print add()
print add(5)
print add(5,6)

# You can define functions that take a variable number of
# keyword args, as well, which will be interpreted as a dict by using **
def add(**kwargs):
    return kwargs

print add()
print add(name='WQS')
print add(name='WQS',age=27)


def all_the_args(*args, **kwargs):
    print args
    print kwargs

all_the_args(1, 2, a=3, b=4)


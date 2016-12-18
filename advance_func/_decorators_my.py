from functools import wraps

def check(target_function):
    @wraps(target_function)
    def decorate(*args,**kwargs):
        if args.__len__()==0:
            print 'para is empty'
        if  'one' in kwargs:
            print 'map contains one'
        return target_function(*args,**kwargs)
    return decorate

@check
def log1(name,one=1,two=2):
    print '{} ,sum={}'.format(name,(str)(one+two))

@check
def log2(*args,**kwargs):
    print 'ok'

log1('WQS',1,2)
log2()
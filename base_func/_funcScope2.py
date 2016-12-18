def spam():
    # global eggs
    print(eggs) # ERROR! if   global eggs is commment
    eggs = 'spam local'

eggs = 'global'
spam()
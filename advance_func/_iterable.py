# Generators
# A generator "generates" values as they are requested instead of storing
# everything up front

# The following method (*NOT* a generator) will double all values and store it
# in `double_arr`. For large size of iterables, that might get huge!
def double_numbers(iterable):
    double_arr=[]
    for i in iterable:
        double_arr.append(i+1)
    print double_arr.__len__()
    return double_arr

# Running the following would mean we'll double all values first and return all
# of them back to be checked by our condition
for value in double_numbers(range(1000000)):
    print value
    if(value>5):
        break


# We could instead use a generator to "generate" the doubled value as the item
# is being requested
def double_numbers_genetator(iterables):
    for i in iterables:
        yield i+1


# Running the same code as before, but with a generator, now allows us to iterate
# over the values and doubling them one by one as they are being consumed by
# our logic. Hence as soon as we see a value > 5, we break out of the
# loop and don't need to double most of the values sent in (MUCH FASTER!)
for value in double_numbers_genetator(xrange(1000000)):
    print value
    if value > 5:
        break
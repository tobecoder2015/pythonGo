import logging
logging.basicConfig(filename='log.log',level=logging.DEBUG,format=
'%(asctime)s-%(levelname)s-%(message)s')
logging.debug('start of program')

def factorial(n):
    logging.info('start of factorial(%s)'%(n))
    total=1
    for i in range(n+1):
        total*=1
        logging.debug('i is'+str(i)+',total is '+str(total))
    logging.info('End of factorial(%s)'%(n))
    return total

for i in [1,2,3,4,5,6]:
    factorial(i)
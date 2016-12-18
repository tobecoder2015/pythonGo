import shelve
shelvefile=shelve.open('test2')
cats = ['Zophie', 'Pooka', 'Simon']
shelvefile['cats']=cats
shelvefile.close()


shelfFile = shelve.open('test2')
print shelfFile['cats']
shelvefile.close()

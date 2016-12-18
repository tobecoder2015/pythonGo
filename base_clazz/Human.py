#encoding=utf-8

class Human(object):
    # A class attribute. It is shared by all instances of this class
    nation = "CHINA"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by python but that live in user-controlled
    # namespaces. You should not invent such names on your own.
    def __init__(self,name):
        # Assign the argument to the instance's name attribute
        self.name=name
        self.age=0

    # An instance method. All methods take "self" as the first argument
    def say(self,msg):
        print "{0}:{1}".format(self.name,msg)

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_nation(cls):
        print cls.nation;

    # A static method is called without a class or instance reference
    @staticmethod
    def sleep():
        print 'now to sleep'

    def age(self,age):
        self.age=age

    def age(self):
        del self.age


i=Human(name='wqs')
i.say("hello world")
i.get_nation();
i.sleep()

Human.sleep()
Human.get_nation()

Human.nation='American'
print "Human.nation='American'"
i.say("hello world")
i.get_nation();
i.sleep()

Human.sleep()
Human.get_nation()


i.age=27
print i.age

del i.age
try:
   print i.age
except Exception as e:
    print e.message
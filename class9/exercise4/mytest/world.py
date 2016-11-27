
'''
4. Create a class MyClass in world.py.

    a. This class should require that three variables be passed in upon initialization.
    b. Write two methods associated with this class 'hello' and 'not_hello'. Have both
    these methods print a statement that uses all three of the initialization variables.
'''
1
def func1():
    print "World"

class MyClass(object):

    def __init__(self, ip, username, version):
        self.ip = ip
        self.username = username
        self.version = version

    def hello(self):
        print 'telnet -l {} {}'.format(self.username, self.ip)

    def not_hello(self):
        print 'ssh -l {} -v{} {}'.format(self.username, self.version, self.ip)

if __name__ == "__main__":
    print "This is the main program of world.py"

    obj=MyClass('10.1.1.1', 'eaboytes', '2')
    obj.hello()
    obj.not_hello()


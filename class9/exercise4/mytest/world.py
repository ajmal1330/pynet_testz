
def func1():
    print "World"

class MyStuff(object):

    def __init__(self, ip, username, version):
        self.ip = ip
        self.username = username
        self.version = version

    def user_same(self):
        print 'ssh {}'.format(self.ip)

    def user_diff(self):
        print 'ssh -l {} -v{} {}'.format(self.username, self.version, self.ip)

if __name__ == "__main__":
    print "This is the main program of world.py"

    obj=MyStuff('10.1.1.1', 'eaboytes', '2')
    obj.user_same()
    obj.user_diff()


'''
Write a Python script in a different directory (not the one containing mytest).

    a. Verify that you can import mytest and call the three functions func1(), func2(), and func3().
    b. Create an object that uses MyClass. Verify that you call the hello() and not_hello() methods.
'''
from mytest import func1, func2, func3, MyClass

def main():
    '''Testing Function import'''
    func1()
    func2()
    func3()
    print 'If you see World, Simple and Whatever on the 3 lines above this is successful'

    print '#' * 40
    print 'Should see telnet and ssh commands below'
    obj = MyClass('10.4.4.4', 'lastuser', '4044')
    obj.hello()
    obj.not_hello()
if __name__ == '__main__':
    main()


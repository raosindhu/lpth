class Parent(object):
    def override(self):
        print "this is parent function"


class Child(Parent):
    print "This is child class"
    def override(self):
        print self
        print "This is child class"
        super(Child, self).override()
        print "this is child function again"


dad = Parent()
son = Child()
#
dad.override()
son.override()

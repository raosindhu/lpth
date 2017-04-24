# trying delete

a = [1, 2, 3, 4, 5, 6]
b = range(1, 10)  # another way to create a list
print "First list:", a
y = a.pop(0)
print "The number removed is", y, "\n The list is now", a

sliceb = slice(1, 6, 2)
z = b[sliceb]
print "Second list:", b
print "The numbers sliced are", z


def func1():
    global x
    x = 3

    def func2():
        print "x=", x, "func2"
        y = 4

        def func3():
            global x
            print "x=", x, "func3"
            print "y=", y, "func3"
            z = 5
            print "z=", z, "func3"
            x = 10

        func3()

    func2()
    print "x=", x, "func1"


func1()


the_list = [2**x for x in range(5)]
# Type check: yes, it's a list

#<class 'list'>
print the_list
print type(the_list)
# Iterate over items and print them
for element in the_list:
    print(element)
print "Number of elements in list", len(the_list)

# Ok, now a generator.
# As easy as list comprehensions, but with '()' instead of '[]':
the_generator = (x+x for x in range(3))
# Type check: yes, it's a generator

# Iterate over items and print them
for element in the_generator:
    print(element)
print type(the_generator)
#print the_generator
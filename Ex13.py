from sys import argv
print "This is the name of the script: ", argv[0]
prompt = '>'

arguments = raw_input("enter the arguments separated by comma")
arguments_list = arguments.split(',')

print arguments_list
argv[1:] = arguments_list
print prompt
print argv
print len(argv)

script, first, second = argv


print argv[0]
print argv[1]


print "The script is called:", script

print "The first variable is:", first

print "The second variable is:", second

#print "The third variable is:", third


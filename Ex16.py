from sys import argv

print len(argv)

script, filename = argv

print argv[0]
print argv[1]

print "I'M GOING TO ERASE THE FILE"

raw_input("?")

print "OPENING THE FILE..."

target = open(filename, 'w')

print "Now i'm entering three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "write these lines to the file"

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n") # write all 3 lines each in a new line at a time to the file
#target.write(line1 + "\n")
#target.write("\n")
#target.write(line2 + "\n")
#target.write("\n")
#target.write(line3 + "\n")
print "close the file"

target.close()

print "Now i'm opening the file in append mode"

target = open(filename, 'a')

#print "Truncating the file"
#target.truncate()

print "Now i'm entering three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "write these lines to the file"

target.write(line1 + "\n")
#target.write("\n")
target.write(line2 + "\n")
#target.write("\n")
target.write(line3 + "\n")

print "close the file"

target.close()
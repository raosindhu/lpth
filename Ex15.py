from sys import argv

print "This is the name of the script: ", argv[0]

filename = raw_input("Enter the file name")

print filename

txt = open(filename)

print txt.read()

print "Enter file name again"

#file_name2 = raw_input(">")

txt_again = open(raw_input(">"))

#print txt_again.read()

print txt_again.readline()

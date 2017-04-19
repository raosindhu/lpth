from sys import argv

script, input_file = argv

def print_file(f): # function to print the file
    print f.read()

def rewind(f): # function to rewind the already read file to first line
    f.seek(0)

def print_line(no_of_lines, f):  # print specific number of lines from a file
    print no_of_lines, f.readline(), # readline reads a single line from the file and returns \n at the end of the line. this adds space betweent he lines printed by this function.
# comma is added to remove the extra line between the printed lines

input_open = open(input_file)

print "1.print the entire file"
print_file(input_open)
print "2.rewind the file \n"
rewind(input_open)
print "3.print each single line"
current_line = 1
print_line(current_line, input_open)

current_line += 1
print_line(current_line, input_open)

current_line += 1
print_line(current_line, input_open)



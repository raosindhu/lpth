from sys import argv

script, inputfile, outputfile = argv

print "inputfile",  inputfile

print "outputfile", outputfile

print "reading the input file"

source = open(inputfile)

read_text = source.read()

print "the text file has:", read_text

print "writing to the output file"



print "opening the file in write mode"

target = open(outputfile, 'w')

target.write(read_text)

print "closing input and output files"

source.close()

target.close()

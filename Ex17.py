from sys import argv
from os.path import exists

script, inputfile, outputfile = argv

print "inputfile",  inputfile

print "outputfile", outputfile

print "reading the input file"

source = open(inputfile)

read_text = source.read()

print """
the text file has:, %r 

does the output file exist? %r 

writing to the output file

opening the file in write mode

""" %(read_text, exists(outputfile))

target = open(outputfile, 'w')

target.write(read_text)

print "closing input and output files"

source.close()

target.close()



read_text = open(inputfile).read() # if this is used, source.close() is not needed. file is closed automatically and hence no control over when to close then file

import os.path
os.path.isfile(fname)

from pathlib import Path

my_file = Path("/path/to/file")
if my_file.is_file():
"""
@author: Colin

a simple python function to perform a regular expression pattern replacement in an input file and writes to an output file.
"""

def regexPy(pattern, replacement, inputfile, outputfile):
    with open(inputfile, "r", encoding='utf-8-sig') as readfile:
        with open(outputfile,"w") as writefile:
            for line in readfile:
                newline = line.replace(pattern, replacement)
                writefile.write(newline)

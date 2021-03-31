"""
@author: Colin

Simple function to convert a table to a standard LaTex table format
"""
def table2Latex(csvfile, header = True, sep = ",", dividedRows = True):
     with open(csvfile, "r") as csvtable:
        with open((csvfile[0:-4] + "_LaTex.txt"),"w") as latex:
            latex.write("\hline\n")
            if (header == True):
                line = csvtable.readline()
                l = line.strip().split(sep)
                latexLine = " & ".join(l) + "\\\\ [0.5ex]\n"
                latexLine = LaTexSyntax(latexLine)
                latex.write(latexLine)
                latex.write("\hline\hline\n")            
            for line in csvtable:   #loop through all the lines starting at line 2
                l = line.strip().split(sep)
                latexLine = " & ".join(l) + "\\\\\n"
                latexLine = LaTexSyntax(latexLine)
                latex.write(latexLine)
                if (dividedRows == True):
                    latex.write("\hline\n")

"""
function to fix common latex syntax errors in text conversion. Cannot 
be used to fix incomplete latex documents. currently only fixes % signs.
Will update to include all common latex symbols.
"""
def LaTexSyntax(inputstring):
    inputstring = inputstring.replace(">", "\textgreater")
    inputstring = inputstring.replace("<", "\textless")
    inputstring = inputstring.replace("$", "\$")
    inputstring = inputstring.replace("_", "\_")
    inputstring = inputstring.replace("%", "\%")
    inputstring = inputstring.replace("#", "\#")
    return(inputstring)

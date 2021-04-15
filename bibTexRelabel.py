"""
@author: Colin

simple function to automatically make custom labels for a BibTex formatted bibliography.
can currently make labels with any combination or order of author, journal, 
D, and year article information.
"""


def bibTexRelabel(bibLibrary, labelFormat = "ajpy", fieldsep = ""):
    with open(bibLibrary, "a",encoding='utf-8-sig') as bib:   #adds a "\n" to end of file
        bib.write("\n")
    labelList = list(labelFormat)
    with open(bibLibrary, "r", encoding='utf-8-sig') as bib:
        with open((bibLibrary[0:-4] + "_LaTex.txt"),"w") as latex:
            label = bib.readline()
            while "@" in label:   #loop to read each entry
                refLine = True
                refEntry = []
                refDict = {"a":"","j":"","p":"","y":""}
                while refLine == True:   #loop to read each line in each entry
                    line = bib.readline()
                    refEntry.append(line)
                    if ("author" in line.split(" = ")[0]):
                        bracket = line.index("{") + 1
                        author = line.split(",")[0]
                        refDict["a"] = author[bracket:]
                    if ("journal" in line.split(" = ")[0]):
                        bracket = line.index("{") + 1
                        journal = line.split("}")[0]
                        refDict["j"] = journal[bracket:]
                    if ("pmid" in line.split(" = ")[0]):
                        bracket = line.index("{") + 1
                        pmid = line.split("}")[0]
                        refDict["p"] = pmid[bracket:]
                    if ("year" in line.split(" = ")[0]):
                        bracket = line.index("{") + 1
                        year = line.split("}")[0]
                        refDict["y"] = year[bracket:]
                    if (line[0] == "}"):
                        refLine = False
                incomplete = 0
                for i in labelList:   #Detects incomplete fields for new label
                    if (refDict.get(i) == ""):
                        incomplete += 1
                if (incomplete == 0):   #writes new label if complete label can be made
                    newlabel = []
                    for i in labelList:
                        newlabel.append(refDict.get(i))
                    newlabel = fieldsep.join(newlabel)
                    labbracket = label.index("{") + 1
                    newline = label[0:labbracket] + newlabel + ",\n"
                    latex.write(newline)
                    for j in refEntry:
                        latex.write(j)
                else:   #rewrites existing entry if fields are incomplete
                    latex.write(label)
                    for j in refEntry:
                        latex.write(j)
                latex.write("\n")
                next(bib)
                label = bib.readline()

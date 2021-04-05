"""
@author: Colin

simple function to automatically make custom labels for a BibTex formatted bibliography.
can currently make labels with any combination or order of author, journal, PMCID, and year article information.
"""


def bibTexRelabel(bibLibrary, labelFormat = "ajpy", fieldsep = ""):
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
                    if (line.split(" = ")[0][3:] == "author"):
                        bracket = line.index("{") + 1
                        author = line.split(",")[0]
                        refDict["a"] = author[bracket:]
                    if (line.split(" = ")[0][3:] == "journal"):
                        bracket = line.index("{") + 1
                        journal = line.split("}")[0]
                        refDict["j"] = journal[bracket:]
                    if (line.split(" = ")[0][3:] == "pmcid"):
                        bracket = line.index("{") + 1
                        pmcid = line.split("}")[0]
                        refDict["p"] = pmcid[bracket:]
                    if (line.split(" = ")[0][3:] == "year"):
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

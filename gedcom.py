sampleDude = ["0 @P1@ INDI ", "1 BIRT ", "2 DATE 3 November 1957", "2 PLAC Spånga, Stockholm, Sweden", "1 NAME Hans /Lundgren/", "1 SEX M", "1 OBJE", "2 FILE doplp.jpg", "2 FORM jpg", "2 TITL Dolph", "1 OBJE", "2 FILE dolph2.jpg", "2 FORM jpg", "2 TITL profile", "1 OBJE", "2 FILE dolph3", "2 FORM jpg", "2 TITL Ivan Drago", "1 OBJE", "2 FILE dolph4.jpg","2 FORM jpg", "2 TITL Bridge of Dragons", "1 FAMC @F3@", "1 FAMS @F1@"]

def gedcomTrans(lineofData):
    level = lineofData[:lineofData.find(" ")]
    if lineofData.count(" ") > 1:
        type = lineofData[2:lineofData.find(" ",lineofData.find(" ")+1)]
        text = lineofData[lineofData.find(" ",lineofData.find(" ")+1):]
    else:
        type = lineofData[2:]
        text = ""        

def importPerson(newPerson):
    gdcName = ""
    fullName = []
    title = ""
    first = ""
    middle = ""
    last = ""
    suffix = ""
    gender = ""
    dateOfBirth = ""
    dateOfDeath = ""
    placeOfBirth = ""
    placeOfDeath = ""
    infoCounter = 0
    while infoCounter < newPerson.len():
        if newPerson[infoCounter][:7] = "1 NAME ":
            fullName.append(eachline[7:])
        if newPerson[infoCounter][:7] = "1 BIRT ":
            infoCounter+= 1


def importTree(tree):
    famlist[] = ""
    postHeader = False
    for each in tree:
        if each[:4] == "0 @P":
            if postHeader:
                famlist[].append(importPerson(newPerson))
            postHeader = True
            newPerson = []
        if postHeader:
            newPerson += each
    return 
    
def importRelation(parent, child):
    
def flexiDate():
    
def place():

def event():

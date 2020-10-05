<<<<<<< HEAD
import re

def choiceSelector(selection):
    """Allows search for titles of choices"""
    filepath = 'dataDump.txt'
    cnt=0
    firstOption=False
    with open(filepath, 'r', encoding='utf8') as fp:
        line = fp.readline()
        while line:
            test="{}".format( line.strip())
            option=re.findall(selection, test)
            print(option)
            if(option != []):
                if(firstOption ):
                    return(lineReader(cnt))
                else:
                    firstOption=True
            line = fp.readline()
            cnt += 1

def lineReader(lineNum):
    """Gets dialog and choices  from specific line number"""
    filepath = 'dataDump.txt'
    output=[]
    cnt=0
    with open(filepath, 'r', encoding='utf8') as fp:
        line = fp.readline()
        while line:
            if( cnt>=lineNum):
                test="{}".format(line.strip())
                option=re.findall(r"\[\[(.*?)\]\]", test)
                if(option!=[]):
                    output.append(test)
                    output += option
                    output.append(cnt)
                    return output
                else:
                    output.append(test)
            line = fp.readline()
            cnt += 1

def choiceSelectorAndNum(selection,lineNum):
    """Gets dialog and choices from specific line number and choice"""
    filepath = 'dataDump.txt'
    cnt=0
    with open(filepath, 'r', encoding='utf8') as fp:
        line = fp.readline()
        while line:
            if( cnt>lineNum):
                test="{}".format(line.strip())
                option=re.findall(selection, test)
                if(option != []):
                    return(lineReader(cnt))
            line = fp.readline()
            cnt += 1


#Note, choices are case sensitive.
print(choiceSelectorAndNum("next", 56))
#output eg. ['Sunny', 'Vincent was sunbathing inside the local park as Jules pumped into him', 'excited about a new idea that he’s determined to share Vincent with. [[next]]', 'next', 52]
=======
def readFile(filepath):
#opens file and writes every line into a list
    file = []
    with open(filepath, 'r', encoding='utf8') as fp:
       line = fp.readline()
       cnt = 1
    while line:
           file.append(line)
           line = fp.readline()
           cnt += 1

#joins all elements in list into 1 element
    file = [''.join(file)]

#Iterates through every letter and finds [ or ]. No indexing however
    for letter in file:
        for char in letter:
            if char == "[":
                print("Here is a [")
                #print(file.index(char))
                
            elif char == "]]":
                print("Here is a ]")
                #print(file.index(char))
                
            else:
                print("0")

    print(file)


#readFile("dataDump.txt")'
>>>>>>> 22198c0133cc2339e65e4fe7a367d78bece667b2


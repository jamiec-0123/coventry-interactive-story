import re
def lineReader(lineNum):
    filepath = 'dataDump.txt'
    output=[]
    cnt=0
    with open(filepath, 'r', encoding='utf8') as fp:
        line = fp.readline()
        while line:
            if( cnt>=lineNum):
                print(" {}".format(line.strip()))
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
def choiceSelector(selection):
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
                    print(lineReader(cnt))
                    print("here")
                    return(lineReader(cnt))
                else:
                    firstOption=True
            line = fp.readline()
            cnt += 1


print(choiceSelector("Sunny"))
#output eg. Line 2: The Fly on Doritos

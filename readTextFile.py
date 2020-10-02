import re
def lineReader(lineNum):
    filepath = 'dataDump.txt'
    output=[]
    cnt=0
    with open(filepath, 'r', encoding='utf8') as fp:
        line = fp.readline()
        while line:
            if( cnt>=lineNum):
                print("Line {}: {}".format(cnt, line.strip()))
                test="Line {}: {}".format(cnt, line.strip())
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
            test="Line {}: {}".format(cnt, line.strip())
            option=[""]
            if selection in test:
                print("HERE")
                return lineReader(cnt)
            line = fp.readline()
            cnt += 1


print(choiceSelector("he checked their photos and some videos"))
#output eg. Line 2: The Fly on Doritos

import checkInput, readTextFile

filename = "dataDump.txt"

# function to count the number of lines in dataBumb.txt
def txtHowManyLines(filename):
    file = open(filename,"r", encoding="utf8") 
    Counter = 0

    Content = file.read()
    CoList = Content.split("\n")

    for i in CoList:
        if i:
            Counter += 1
    return(Counter)
          
dataDumbLinesCount = txtHowManyLines(filename)

# function to get the requested line from dataBumb.txt back
def testLineOutput(line_number):
    with open(filename, 'r', encoding='utf8') as filehandle:
        current_line = 1
        for line in filehandle:
            if current_line == line_number:
                return(line)
            current_line += 1

# function to compare the the return from the functions "testLineOutput" and "readTextFile.lineReader"
i = 1
while i < dataDumbLinesCount:
    data=readTextFile.lineReader(i)
    lineNumberOfFile=data[len(data)-1]
    print("Testing:"+str(lineNumberOfFile)+" against:"+str(i))
    if testLineOutput(i) == readTextFile.lineReader(i):
        print("Line " + str(i) + " is identical, FAIL")
        i+=1
    else:
        print("Line " + str(i) + " is not identical, PASS")
        i+=1
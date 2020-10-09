#Main program
import checkInput, readTextFile

#print("Fly of The Dorito")
p=1
paragraph1 = readTextFile.lineReader(0)
print(paragraph1[0])
print(paragraph1[1])
print(paragraph1[2])


'''
psudo code
lineNum=0
userChoice=""
while True:
    numberOfChoices=0
    if(lineNum !=187):
        data=readTextFile.getLine(lineNum)
        lengthOfText=data[data.length()-1]-lineNum
        while x in range(lengthOfText):
            if(data[x].contains("(")):
                print(data[x])
            elif(type(data[x]) != int ):
                numberOfChoices +=1
                outputChoiceses +="["+(x+1)+"]"+ data[x] + ","
            else:
                lineNum=data[x]
        print(ouptChoices)
        number=0
        while(selected == False):
            if(validateChoice(number,options) !=0):
                data=findChoice(number-1)
            else:
                number= input(choice)
    elif(userChoice =="start"):
        lineNum=0
    else:
        break
'''
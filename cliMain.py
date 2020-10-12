#Main program
import checkInput, readTextFile, re

#print("Fly of The Dorito")
p=0
paragraph = readTextFile.lineReader(p)
while(True):
    optionOutput="Your options are "
    foundOptions = False
    optionNum=0
    option=""
    choicesList=[]
    for index in range(len(paragraph)-1):
        try:
            int(paragraph[index+1])
            optionNum+=1
            optionOutput+=" ("+str(optionNum)+"): "+str(paragraph[index])
            choicesList.append(str(paragraph[index]))
            choicesList.append(paragraph[index+1])
        except:
            try:
                int(paragraph[index])
            except:
                try:
                    option=re.findall(r"\((.*?)\)", paragraph[index])
                    if(option != []):
                        option= str(option[0]).split(", ")
                        otherNum =0
                        for subIndex in range(len(option)):
                            otherNum=subIndex+1+optionNum
                            optionOutput+=" ("+str(otherNum)+"): "+str(option[subIndex])
                            choicesList.append(str(option[subIndex]))
                            choicesList.append(otherNum)
                            
                        optionNum=otherNum 
                except:
                    pass   
                if (paragraph[index] in optionOutput or paragraph[index]=="Start"):
                    pass
                else:
                    print(paragraph[index])
    errorNoOption=False
    if(optionOutput=="Your options are "):
        while(not(errorNoOption)):
            noUserOptions=input("You've run out of options, try again? Y/N")
            if(noUserOptions.upper() =='Y' or noUserOptions.upper() == "Y"):
                lineSelected=0
                errorNoOption=True
            elif(noUserOptions.upper()=='N' or noUserOptions.upper() == "N"):
                exit(0)
                break
            else:
                pass
    else:  
        validUserInput=0
        while( validUserInput ==0):
            userInput=input(optionOutput)
            validUserInput=checkInput.checkInput(userInput,optionNum)
            if(validUserInput!=0):
                if(choicesList[(validUserInput-1)*2]!="Start"):
                    testParagraph =readTextFile.choiceSelectorAndNum(choicesList[(validUserInput-1)*2],choicesList[(validUserInput)*2-1])
                    if(testParagraph is None):
                        paragraph = readTextFile.lineReader(paragraph[len(paragraph)-1])
                        
                    else:
                        paragraph=testParagraph
                else:
                    p=0
                    paragraph = readTextFile.lineReader(p)
            else:
                print("ERROR WITH INPUT, ENTER VALID VALUES")
                
    
        

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
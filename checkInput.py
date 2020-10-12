def checkInput(userChoice, choices):
    option=0
    limmit = 0
    try:
        """Ensures that the input is an integer"""
        option =int(userChoice)
        limmit = int(choices)
    except:
        return 0
    if(option>0 and option<=limmit):
        return option
    else:
        return 0

#never gunna give you up


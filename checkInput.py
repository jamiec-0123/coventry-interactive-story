def checkInput(input, choices):
    option=0
    limmit = 0
    try:
        option =int(input)
        limmit = int(choices)
    except:
        return 0
    if(option>0 and option<limmit):
        return option
    else:
        return 0



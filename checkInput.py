def checkInput(input, choices):
    try:
        option =int(input)
        limmit = int(choices)
        if(option>0 and option<limmit):
            return option
        else:
            return 0
    except:
        return 0



def checkInput(input, choices):
    option=0
    limmit = 0
    try:
        """Ensures that the input is an interger"""
        option =int(input)
        limmit = int(choices)
        if(type(option) != type(input) or type(limmit) != type(choices)):
            return 0
    except:
        return 0
    if(option>0 and option<limmit):
        return option
    else:
        return 0



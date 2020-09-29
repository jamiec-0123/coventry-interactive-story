def checkInput(input, choices):
    try:
        option =int(input)
        if(option>0 and option<choices):
            return option
        else:
            return 0
    except:
        return 0



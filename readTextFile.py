def readFile(filepath):
#opens file and writes every line into a list
    file = []
    with open(filepath, 'r', encoding='utf8') as fp:
       line = fp.readline()
       cnt = 1
    while line:
           file.append(line)
           line = fp.readline()
           cnt += 1

#joins all elements in list into 1 element
    file = [''.join(file)]

#Iterates through every letter and finds [ or ]. No indexing however
    for letter in file:
        for char in letter:
            if char == "[":
                print("Here is a [")
                #print(file.index(char))
                
            elif char == "]]":
                print("Here is a ]")
                #print(file.index(char))
                
            else:
                print("0")

    print(file)


#readFile("dataDump.txt")


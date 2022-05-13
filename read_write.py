#writing a list to file
places = ['Berlin', 'Cape Town', 'Sydney', 'Moscow'] 
with open('listfile.txt', 'w') as filehandle: 

    for listitem in places: 

        filehandle.write('%s\n' % listitem) 

#reading the file
# define an empty list 
places = [] 
# open file and read the content in a list 
with open('listfile.txt', 'r') as filehandle: 
    for line in filehandle: 
        # remove linebreak which is the last character of the string 
        currentPlace = line[:-1] 
        # add item to the list 
        places.append(currentPlace) 

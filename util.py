    #isInList Function
    #Inputs: a list and an object
    #Returns: a boolean value
    #Description: Returns True if object is in the list, false otherwise

def isInList(list, object):
    out = False
    for obj in list:
        if obj == object:
            out = True
    return(out)

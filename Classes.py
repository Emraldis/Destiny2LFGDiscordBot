import util

#--Useful Comment Formats--#

    # Function
    #Inputs:
    #Returns:
    #Description:

    ####-WIP FUNCTION-###

#-----------------------------
#NAME Class
#-----------------------------

#-----------------------------
#Player Class
#-----------------------------
class Player:
    def __init__(self, name, ID):
        self.name = name
        self.playerID = ID
        self.availabilities = list()

    #addAvailability Function
    #Inputs: a tag object
    #Returns: Nothing
    #Description: Adds a tag object to the player's list of availabilities.

    def addAvailability(self, tag):
        self.availabilities.append(tag)

    #removeAvailability Function
    #Inputs: a tag object
    #Returns: Nothing
    #Description: Removes a tag object to the player's list of availabilities.

    def removeAvailability(self, tag):
        self.availabilities.remove(tag)

    #clearAvailabilities Function
    #Inputs: Nothing
    #Returns: Nothing
    #Description: clears a player's list of availabilities.

    def clearAvailabilities(self):
        self.availabilities.clear()

    #printTags Function
    #Inputs: Nothing
    #Returns: A formatted string of the player's tags
    #Description: Formats and returns the player's tags as a string

    def printTags(self):
        out = self.name + " is available for: "
        length = len(self.availabilities)
        if length == 0:
            out = out + "No Activities"
        else if length == 1:
            out = out + self.availabilities[0].name
        else:
            iter = 1
            for tag in self.availabilities:
                if iter < length:
                    out = out + tag.name + ", "
                else:
                    out = out + "and " + tag.name
        return(out)

    #printSelf Function
    #Inputs: Nothing
    #Returns: A formatted string of the player's information
    #Description: Formats and returns the player's information as a string (for debugging)

    def printSelf(self):
        out = "Name: " + self.name + " ID: " + self.playerID
        return(out)

#-----------------------------
#Tag Class
#-----------------------------

class Tag:
    def __init__(self, name):
            self.name = name
            self.parent = self
            self.children = list()
            self.players = list()

    #assignPlayer Function
    #Inputs: a Player object
    #Returns: Nothing
    #Description: Assigns a player object to an availability tag

    def assignPlayer(self, player):
        self.players.append(player)

    #removePlayer Function
    #Inputs: a Player object
    #Returns: Nothing
    #Description: Removes a player object from an availability tag

    def removePlayer(self, player):
        self.players.remove(player)

    #clearPlayers Function
    #Inputs: Nothing
    #Returns: Nothing
    #Description: Clears all player objects from an availability tag

    def clearPlayers(self):
        self.players.clear()

    #getPlayers Function
    #Inputs: Nothing
    #Returns: A list of assigned Player Objects
    #Description: Returns a list of assigned player objects

    def getPlayers(self):
        return(self.players)

    #addChildTag Function
    #Inputs: a Tag object
    #Returns: Nothing
    #Description: Adds a child tag to an availability tag

    def addChildTag(self, tag):
        tag.parent = self
        self.children.append(tag)

    #removeChildTag Function
    #Inputs: a tag object
    #Returns: Nothing
    #Description: Removes a given tag object from a tag's children list (Primarily for use in deleting a tag and all of its children)
    def removeChildTag(self, tag):
        self.children.remove(tag)

    #deleteTag Function
    #Inputs: Nothing
    #Returns: Nothing
    #Description: Deletes the tag and all its child tags

    def deleteTag(self):
        for tag in self.children:
            tag.deleteTag()
        self.parent.removeChildTag(self)
        del self

    #gatherAvailablePlayers Function
    #Inputs: Nothing
    #Returns: A list of available Player Objects
    #Description: Returns a list of available player objects

    def gatherAvailablePlayers(self):
        out = list()
        for player in self.players:
            out.append(player)
        if self.parent != self:
            for player in self.parent.gatherAvailablePlayers():
                if not util.isInList(out, player):
                    out.append(player)

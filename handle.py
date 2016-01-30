import json
import bnet
import random

LINK_FILE_NAME = 'links.txt'
MEMES_FILE_NAME = 'memes.txt'

def readJsonFile(filename):
    out = json.load(open(filename))
    return out

def addToJsonFile(filename, tag, content):
    data = readJsonFile(filename)
    data[tag] = content
    json.dump(data, open(filename, 'w'))

def removeFromJsonFile(filename, tag):
    data = readJsonFile(filename)
    if tag in data:
        del data[tag]
        json.dump(data, open(filename, 'w'))

#Display, add or remove links. Add + remove are moderator only.
def links(message):
    args = message.content.split()

    #Display links
    if len(args) == 1:
        data = readJsonFile(LINK_FILE_NAME)
        out_message = "\n"
        for key in data:
            out_message += key + ":\n" + data[key] + "\n"
        return out_message

    #Have extra args, check for privs and parse
    else:
        #Check for mod role
        roles = message.author.roles
        flag = 0
        for role in roles:
            if role.name == "Moderator":
                flag = 1
        if flag==0:
            return "You do not have the required permissions to edit links."

        #Add link
        if args[1] == 'add':
            if len(args)==4:
                addToJsonFile(LINK_FILE_NAME, args[2], args[3])
                return "Added " + args[2] + " -- " + args[3]
            else:
                return "Incorrect usage"

        #Remove link
        elif args[1] == 'delete':
            if len(args)==3:
                removeFromJsonFile(LINK_FILE_NAME, args[2])
                return "Removed " + args[2]
            else:
                return "Incorrect usage"

        #Send help info
        else:
            #Add helpful stuff here.
            return "Incorrect usage"

#Get ilevel from blizz and display
def ilevel(message):
    name = message.content.split()[1]
    realm = message.content.split()[2]
    ilevel = bnet.ilevelReq(realm, name)
    out_message = name + "-" + realm + " has an average equipped ilevel of " + str(ilevel)
    return out_message

#Get achievement points from blizz and display
def achieve(message):
    name = message.content.split()[1]
    realm = message.content.split()[2]
    points = bnet.achievementReq(realm, name)
    out_message = name + "-" + realm + " has " + str(points) + " achievement points."
    return out_message
  
#Boss Fights 
def mhfc(message):
    diff = message.content.split()[1]
    fight = message.content.split()[2]
    video = mythicHFC.mythicbossfights(fight, diff)
    print(diff,fight)
    out_message = diff + " " + fight + "  " + str(video)
    return out_message

#dankmemes
def memes(message):
    args = message.content.split()

    #display a random dank meme
    if len(args) == 1:
        data = readJsonFile(MEMES_FILE_NAME)
        out_message = random.choice(list(data.values()))
        return out_message

    #display a specific dank meme
    elif len(args) == 2:
        data = readJsonFile(MEMES_FILE_NAME)
        if args[1] in data:
            return data[args[1]]
        else:
            return "Meme not found!"

    #delete a dank meme
    elif len(args) == 3:
        if args[1] == "delete":
            data = readJsonFile(MEMES_FILE_NAME)
            if args[2] in data:
                removeFromJsonFile(MEMES_FILE_NAME, args[2])
            else:
                return "Meme not found!"
        else:
            return "Incorrect usage"

    #add a dank meme
    elif len(args) == 4:
        if args[1] == 'add':
            addToJsonFile(MEMES_FILE_NAME, args[2], args[3])
        else:
            return "Incorrect usage"

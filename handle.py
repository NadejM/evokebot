import json
import bnet

LINK_FILE_NAME = 'links.txt'

def readLinksFile():
    out = json.load(open(LINK_FILE_NAME))
    return out

def addToLinks(tag, url):
    data = readLinksFile()
    data[tag] = url
    json.dump(data, open(LINK_FILE_NAME, 'w'))

def removeFromLinks(tag):
    data = readLinksFile()
    if tag in data:
        del data[tag]
        json.dump(data, open(LINK_FILE_NAME, 'w'))

def links(message):
    args = message.content.split()

    if len(args) == 1:
        data = readLinksFile()
        out_message = "\n"
        for key in data:
            out_message += key + ":\n" + data[key] + "\n"
        return out_message
    else:
        roles = message.author.roles
        flag = 0
        for role in roles:
            if role.name == "Moderator":
                flag = 1
        if flag==0:
            return "You do not have the required permissions to edit links."
        if args[1] == 'add':
            if len(args)==4:
                addToLinks(args[2], args[3])
                return "Added " + args[2] + " -- " + args[3]
            else:
                return "Incorrect usage"
        elif args[1] == 'delete':
            if len(args)==3:
                removeFromLinks(args[2])
                return "Removed " + args[2]
            else:
                return "Incorrect usage"
        else:
            #Add helpful stuff here.
            return "Incorrect usage"

def ilevel(message):
    name = message.content.split()[1]
    realm = message.content.split()[2]
    ilevel = bnet.ilevelReq(realm, name)
    out_message = name + "-" + realm + " has an average equipped ilevel of " + str(ilevel)
    return out_message

def achieve(message):
    name = message.content.split()[1]
    realm = message.content.split()[2]
    points = bnet.achievementReq(realm, name)
    out_message = name + "-" + realm + " has " + str(points) + " achievement points."
    return out_message
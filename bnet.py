#! /usr/bin/env python

# standard Python modules
import sys
import os
import requests
import json

# load your key if existing
PUBLIC_KEY = os.environ.get('BNET_PUBLIC_KEY')
PRIVATE_KEY = os.environ.get('BNET_PRIVATE_KEY')

def achievementReq(realm, name):
    request = "https://us.api.battle.net/wow/character/" + realm + "/" + name + "?fields=achievements&locale=en_US&apikey=" + PUBLIC_KEY
    r = requests.get(request)
    out = r.json()
    return (out['achievementPoints'])

def ilevelReq(realm, name):
    request = "https://us.api.battle.net/wow/character/" + realm + "/" + name + "?fields=items&locale=en_US&apikey=" + PUBLIC_KEY
    r = requests.get(request)
    out = r.json()
    return (out['items']['averageItemLevelEquipped'])

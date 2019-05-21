import json
from difflib import get_close_matches
data=json.load(open("data.json"))


def dict(key):
    if key in data.keys():
        return data[key]
    elif len(get_close_matches(key,data.keys()))>0:
        wrd=input("Do you Mean %s if Yes type 'Y' else Type 'N' : " %(get_close_matches(key,data.keys())[0]))
        if(wrd=='Y'):
            return data[get_close_matches(key,data.keys())[0]]
        elif wrd=='N':
            return "the word does not exist"
        else:
            return "Sorry please try again"
    else:
        return "the word does not exist"

key=input("Please enter a word to search: ")

item=dict(key)

if type(item)==list:
    for i in item:
        print(i)
else:
    print(item)

import json
from difflib import get_close_matches
data=json.load(open("datafiles/data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]

    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean %s instead? Enter y if yes or n if no "%get_close_matches(w,data.keys())[0])
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=='n':
            return "word does not exist,please check"
        else:
            return "We did not understand your input"
    else:
        print("Word does not Exit, please check")

word=input("Enter the word : ")

output=translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
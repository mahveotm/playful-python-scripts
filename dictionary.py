print("""
    A script that checks a word from merriam webster dictionary
""")


import requests

def accept_name():
    name = str(input('Please enter the word: '))
    
    if not name:
        print('Error: Nothing  entered')
        return accept_name()
    
    else:

        return name

def api_dance(name):
    name = accept_name()
    name = name.replace(" ", "_")
    #begin link formation
    link = 'https://dictionaryapi.com/api/v3/references/collegiate/json/'
    #key - your key, can be gotten from https://dictionaryapi.com
    key ="key"
    url = link + name + key
    #json requests
    json_data = requests.get(url).json()
    json_id = json_data[0]['shortdef'][0]
    print(json_id)
    

if __name__ == "__main__":
    api_dance(accept_name)
print("""
        A python script that uses your name to guess your age,
        API derived from Agify.io. Essentially for tests and fun
""")


import requests

def accept_name():
    name = str(input('Please enter your name: '))
    
    if not name:
        print('Error: Nothing  entered')
        return accept_name()
    
    else:

        return name

def api_dance(name):
    name = accept_name()
    name = name.replace(" ", "&")
    #begin link formation
    link = 'https://api.agify.io/?name='
    url = link + name
    #json requests
    json_data = requests.get(url).json()
    json_age = json_data['age']
    print(json_age)

if __name__ == "__main__":
    api_dance(accept_name)
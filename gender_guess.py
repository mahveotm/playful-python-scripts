print("""
        A python script that uses your name to guess your Gender based on your name,
        API derived from Genderize.io. Essentially for tests and fun
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
    link = 'https://api.genderize.io/?name='
    url = link + name
    #json requests
    json_data = requests.get(url).json()
    json_gender = json_data['gender']
    print(json_gender)

if __name__ == "__main__":
    api_dance(accept_name)
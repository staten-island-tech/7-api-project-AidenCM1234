import requests

def getPoke(poke):
    url = f"https://api.chess.com/pub/player/{poke.lower()}"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    avatar_usage =False
    data = response.json()
    for i in data:
        if i == "avatar":
            avatar_usage =True
    return {
        "username": data["username"], 
        if avatar_usage==True:
            "avatar": data["avatar"] ,
        "followers": data["followers"]
    }

pokemon = getPoke("bulbasaur")
print(pokemon)
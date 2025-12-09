import requests

def getPlayer():
    response = requests.get(f"curl -v https://api.chess.com/pub/player/{player}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }
getPlayer("hikaru")
player = getPlayer("hikaru")
print(player)
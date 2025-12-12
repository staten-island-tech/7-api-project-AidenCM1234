import requests

def getPlayer(user):
    url = f"https://api.chess.com/pub/player/{user.lower()}"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    avatar_usage =False
    data = response.json()
    

    basic_infomation={"username": data["username"], 
            "followers": data["followers"]}
    varible_infomation="e"
    return basic_infomation #and varible_infomation

    for i in data:
            print(i)
            print("  ")
            if i =="avatar":
                 avatar_usage=True
    if avatar_usage == True:
         return {"avatar": data["avatar"]}
    
    

player = getPlayer("bob")
print(player)
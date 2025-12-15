import requests

def getPlayers(user):
    url = f"https://api.chess.com/pub/player/{user.lower()}"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()

    url2 = f"https://api.chess.com/pub/player/{user.lower()}/stats"
    headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response2 = requests.get(url2, headers=headers2)
    if response2.status_code != 200:
        print("Error fetching data!")
        return None
    data2 = response2.json()

    avatar_usage =False
    for i in data:
            print(i)
            print("  ")
            if i =="avatar":
                 avatar_usage=True
    if avatar_usage == True:
         print (f"avatar: {data}[avatar]")
    else:
         print("No avatar")
    for i in data2:
            print(i)
            print("  ")
            """if i =="avatar":
                 avatar_usage=True
    if avatar_usage == True:
         print (f"avatar: {data}[avatar]")
    else:
         print("No avatar")"}:"""
    
    basic_infomation={
         "username": data["username"], 
          "followers": data["followers"],
          "best": data2["rating"]}
    return basic_infomation 

player = getPlayers("bob")#,"erik")
print(player)
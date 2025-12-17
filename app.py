import requests

def getPlayers(user,userb):
    url = f"https://api.chess.com/pub/player/{user.lower()}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()

    url2 = f"https://api.chess.com/pub/player/{user.lower()}/stats"
    headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response2 = requests.get(url2, headers=headers2)
    if response2.status_code != 200:
        print("Error fetching data!")
        return None
    data2 = response2.json()

    avatar_usage =False
    for i in data:
            if i =="avatar":
                 avatar_usage=True
    if avatar_usage == True:
         print (f"avatar: {data}[avatar]")
    else:
         print("No avatar")
    one_win=data2["chess_daily"]["record"]["win"]
    one_lose=data2["chess_daily"]["record"]["loss"]
    one_best=data2["chess_daily"]["best"]["rating"]
    basic_infomation_player1={
        "1username": data["username"], 
          "1followers": data["followers"],
          "1chess_daily_record_win": data2["chess_daily"]["record"]["win"],
          "1chess_daily_record_loss": data2["chess_daily"]["record"]["loss"],
          "1chess_daily_best_rating": data2["chess_daily"]["best"]["rating"]}
    ###
    ###
    url = f"https://api.chess.com/pub/player/{userb.lower()}"
    response = requests.get(url, headers=headers)
    data = response.json()

    url2 = f"https://api.chess.com/pub/player/{userb.lower()}/stats"
    response2 = requests.get(url2, headers=headers)
    data2 = response2.json()
    two_win=data2["chess_daily"]["record"]["win"]
    two_lose=data2["chess_daily"]["record"]["loss"]
    two_best=data2["chess_daily"]["best"]["rating"]

    basic_infomation_player2 = {
        "2username": data["username"],
        "2followers": data["followers"],
        "2avatar": data.get("avatar"),
        "2chess_daily_record_win": data2["chess_daily"]["record"]["win"],
        "2chess_daily_record_loss": data2["chess_daily"]["record"]["loss"],
        "2chess_daily_best_rating": data2["chess_daily"]["best"]["rating"],
    }
    return basic_infomation_player1 and basic_infomation_player2

player = getPlayers("bob","erik")
print(player)
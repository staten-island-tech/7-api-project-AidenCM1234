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
    one_win=data2["chess_daily"]["record"]["win"]
    one_lose=data2["chess_daily"]["record"]["loss"]
    one_best=data2["chess_daily"]["best"]["rating"]
    basic_infomation_player1={
        "1username": data["username"], 
          "1followers": data["followers"],
          "1chess_daily_record_win": data2["chess_daily"]["record"]["win"],
          "1avatar": data.get("avatar"),
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
    user_value=0
    userb_value=0
    if one_win>=two_win:
         user_value+=2
    else:
        userb_value+=2
    if one_lose<=two_lose:
         user_value+=1
    else:
        userb_value+=1
    if one_best>=two_best:
         user_value+=2
    else:
        userb_value+=2
    if one_win/(one_win+one_lose)>=two_win/(two_win+two_lose):
         user_value+=1
    else:
        userb_value+=1
    
    winner = user if user_value >= userb_value else userb
        
    return winner, basic_infomation_player1, basic_infomation_player2

player = getPlayers("bob","bulbasaur")
print(player)

import tkinter as tk
from tkinter import messagebox

def compare_players():
    user1 = entry_user1.get().strip()
    user2 = entry_user2.get().strip()

    if not user1 or not user2:
        messagebox.showerror("Error", "Enter both usernames")
        return

    try:
        winner, p1, p2 = getPlayers(user1, user2)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return

    output.delete("1.0", tk.END)

    output.insert(tk.END, f"Probable Winner: {winner}\n\n")

    output.insert(tk.END, f"Player 1({user1}):\n")
    for k, v in p1.items():
        output.insert(tk.END, f"{k}: {v}\n")

    output.insert(tk.END, f"\nPlayer 2({user2}):\n")
    for k, v in p2.items():
        output.insert(tk.END, f"{k}: {v}\n")


# ---------------- GUI SETUP ----------------

root = tk.Tk()
root.title("Chess.com Player Comparator")
root.geometry("500x600")

tk.Label(root, text="Player 1 Username").pack()
entry_user1 = tk.Entry(root)
entry_user1.pack()

tk.Label(root, text="Player 2 Username").pack()
entry_user2 = tk.Entry(root)
entry_user2.pack()

tk.Button(root, text="Compare Players", command=compare_players).pack(pady=10)

output = tk.Text(root, height=30, width=60)
output.pack()


root.mainloop()
#Some players may not have a chess_daily try erik and bob
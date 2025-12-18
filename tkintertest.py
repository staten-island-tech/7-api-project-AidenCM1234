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

    output.insert(tk.END, f"Winner: {winner}\n\n")

    output.insert(tk.END, "Player 1:\n")
    for k, v in p1.items():
        output.insert(tk.END, f"{k}: {v}\n")

    output.insert(tk.END, "\nPlayer 2:\n")
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
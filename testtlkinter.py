import tkinter as tk
from PIL import Image, ImageTk
import os

AVATAR_DIR = "data/avatar"
DEFAULT_AVATAR = "default.png"


class AvatarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Avatar Viewer")

        # Input fields
        tk.Label(root, text="Input 1:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(root, text="Input 2:").grid(row=0, column=1, padx=5, pady=5)

        self.entry1 = tk.Entry(root)
        self.entry2 = tk.Entry(root)

        self.entry1.grid(row=1, column=0, padx=5)
        self.entry2.grid(row=1, column=1, padx=5)

        # Button
        tk.Button(root, text="Show Avatars", command=self.show_avatars)\
            .grid(row=2, column=0, columnspan=2, pady=10)

        # Image labels
        self.img_label1 = tk.Label(root)
        self.img_label2 = tk.Label(root)

        self.img_label1.grid(row=3, column=0, padx=10, pady=10)
        self.img_label2.grid(row=3, column=1, padx=10, pady=10)

        self.img1 = None
        self.img2 = None

    def load_avatar(self, name):
        filename = f"{name}.png"
        path = os.path.join(AVATAR_DIR, filename)

        if not os.path.exists(path):
            path = os.path.join(AVATAR_DIR, DEFAULT_AVATAR)

        image = Image.open(path).resize((128, 128))
        return ImageTk.PhotoImage(image)

    def show_avatars(self):
        name1 = self.entry1.get().strip()
        name2 = self.entry2.get().strip()

        self.img1 = self.load_avatar(name1)
        self.img2 = self.load_avatar(name2)

        self.img_label1.config(image=self.img1)
        self.img_label2.config(image=self.img2)


if __name__ == "__main__":
    root = tk.Tk()
    app = AvatarApp(root)
    root.mainloop()
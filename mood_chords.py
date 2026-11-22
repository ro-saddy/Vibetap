import tkinter as tk
from PIL import Image, ImageTk

n = {"C": "cmajor", "B": "bmajor", "Em": "eminor", "Bm": "bminor",
     "Fmaj7": "fmaj7", "D": "dmajor", "Am7": "amin7", "G": "gmajor",
     "F": "fmajor", "A": "amjor", "Am": "aminor", "Cadd9": "cadd9"}

d = {
    "Happy": [
        (["C", "G", "Am", "F"],
         ["Let It Be - The Beatles",
          "I'm Yours - Jason Mraz",
          "No Woman No Cry - Bob Marley"])
    ],
    "Sad": [
        (["Am", "F", "C", "G"], ["Let Her Go - Passenger"]),
        (["C", "Am", "F", "G"], ["Hallelujah - Jeff Buckley"])
    ],
    "Chill": [
        (["C", "Am", "F", "G"],
         ["Stand By Me - Ben E. King",
          "Earth Angel - The Penguins"])
    ],
    "Romantic": [
        (["G", "Em", "C", "D"], ["Perfect - Ed Sheeran"]),
        (["C", "Em", "Am", "F"], ["Can't Help Falling in Love - Elvis Presley"])
    ],
    "Energetic": [
        (["D", "G", "A"], ["Twist and Shout - The Beatles"]),
        (["Bm", "G", "D", "A"], ["Despacito - Luis Fonsi"])
    ]
}

r = tk.Tk()
r.geometry("900x700")
t = tk.Frame(r)
t.pack(pady=10)
b = tk.Frame(r)
b.pack()
a = []


def show(m):
    for w in b.winfo_children():
        w.destroy()
    a.clear()
    for p, s in d[m]:
        f = tk.Frame(b)
        f.pack(pady=10)
        row = tk.Frame(f)
        row.pack()
        for c in p:
            i = ImageTk.PhotoImage(Image.open("chords/" + n[c] + ".png").resize((120, 120)))
            a.append(i)
            tk.Label(row, image=i).pack(side="left")
        for x in s:
            tk.Label(f, text=x).pack()


for m in d:
    tk.Button(t, text=m, width=12, command=lambda x=m: show(x)).pack(side="left", padx=5)

r.mainloop()

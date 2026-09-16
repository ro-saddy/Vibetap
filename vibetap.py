import json
import tkinter as tk

with open("progressions.json", "r", encoding="utf-8") as f:
    PROGRESSIONS = json.load(f)

CHORD_SHAPES = {
    "C": [-1, 3, 2, 0, 1, 0],
    "G": [3, 2, 0, 0, 0, 3],
    "D": [-1, -1, 0, 2, 3, 2],
    "E": [0, 2, 2, 1, 0, 0],
    "A": [-1, 0, 2, 2, 2, 0],
    "B": [-1, 2, 4, 4, 4, 2],
    "Am": [-1, 0, 2, 2, 1, 0],
    "Em": [0, 2, 2, 0, 0, 0],
    "Dm": [-1, -1, 0, 2, 3, 1],
    "Bm": [-1, 2, 4, 4, 3, 2],
    "F": [1, 3, 3, 2, 1, 1],
    "Bb": [-1, 1, 3, 3, 3, 1],
    "Am7": [-1, 0, 2, 0, 1, 0],
    "Fmaj7": [-1, -1, 3, 2, 1, 0],
    "Cadd9": [-1, 3, 2, 0, 3, 0],
}

MOOD_COLORS = {
    "Happy": "#FB8500",
    "Sad": "#457B9D",
    "Chill": "#48CAE4",
    "Nostalgic": "#9C6644",
    "Hopeful": "#2D9D5F",
    "Tense": "#E63946",
    "Dreamy": "#B185DB",
    "Angry": "#D00000",
}


def draw_chord_diagram(canvas, chord_name):
    canvas.delete("all")

    left_margin = 25
    top_margin = 30
    string_spacing = 15
    fret_spacing = 22
    num_frets = 4

    shape = CHORD_SHAPES.get(chord_name)

    canvas.create_text(
        70,
        12,
        text=chord_name,
        font=("Arial", 13, "bold"),
        fill="black"
    )

    if shape is None:
        canvas.create_text(
            70,
            70,
            text="No shape",
            font=("Arial", 9),
            fill="gray"
        )
        return

    for i in range(6):
        x = left_margin + i * string_spacing
        canvas.create_line(
            x,
            top_margin,
            x,
            top_margin + num_frets * fret_spacing
        )

    for fret in range(num_frets + 1):
        y = top_margin + fret * fret_spacing
        canvas.create_line(
            left_margin,
            y,
            left_margin + 5 * string_spacing,
            y
        )

    for i, fret in enumerate(shape):
        x = left_margin + i * string_spacing

        if fret == -1:
            canvas.create_text(
                x,
                top_margin - 10,
                text="x",
                font=("Arial", 11),
                fill="red"
            )

        elif fret == 0:
            canvas.create_oval(
                x - 5,
                top_margin - 16,
                x + 5,
                top_margin - 6,
                outline="black"
            )

        else:
            y = top_margin + (fret - 1) * fret_spacing + fret_spacing // 2

            canvas.create_oval(
                x - 6,
                y - 6,
                x + 6,
                y + 6,
                fill="black"
            )


def show_progression(mood):
    data = PROGRESSIONS[mood]
    chords = data["progression"]

    result_label.config(
        text=mood + "  •  " + data["key"] + "\n" + "  -  ".join(chords)
    )

    songs_label.config(
        text="Inspired by:  " + "   |   ".join(data["songs"])
    )

    for widget in image_frame.winfo_children():
        widget.destroy()

    for i, chord in enumerate(chords):
        canvas = tk.Canvas(
            image_frame,
            width=140,
            height=140,
            bg="white",
            highlightthickness=0
        )

        canvas.grid(
            row=i // 2,
            column=i % 2,
            padx=5,
            pady=5
        )

        draw_chord_diagram(canvas, chord)


root = tk.Tk()

root.title("VibeTap")
root.geometry("430x800")
root.minsize(350, 650)
root.configure(bg="white")

menu_bar = tk.Frame(
    root,
    bg="#FFD60A",
    pady=20
)

menu_bar.pack(
    fill="x"
)

tk.Label(
    menu_bar,
    text="Pick a mood",
    font=("Arial", 22, "bold"),
    bg="#FFD60A",
    fg="black"
).pack(
    pady=(0, 15)
)

button_row = tk.Frame(
    menu_bar,
    bg="#FFD60A"
)

button_row.pack()

for i, mood in enumerate(PROGRESSIONS.keys()):
    color = MOOD_COLORS.get(mood, "#333333")

    button = tk.Button(
        button_row,
        text=mood,
        font=("Arial", 11, "bold"),
        width=13,
        height=2,
        bg=color,
        fg="white",
        relief="flat",
        bd=0,
        activebackground=color,
        command=lambda m=mood: show_progression(m)
    )

    button.grid(
        row=i // 2,
        column=i % 2,
        padx=6,
        pady=5
    )

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 17, "bold"),
    bg="white",
    fg="black",
    justify="center"
)

result_label.pack(
    pady=(25, 5)
)

songs_label = tk.Label(
    root,
    text="",
    font=("Arial", 10, "italic"),
    bg="white",
    fg="#555555",
    wraplength=370,
    justify="center"
)

songs_label.pack(
    pady=(0, 10)
)

image_frame = tk.Frame(
    root,
    bg="white"
)

image_frame.pack(
    pady=5
)

root.mainloop()
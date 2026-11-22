#**Vibetap**

Vibetap is essentially a desktop tool for budding guitarists, its purpose being to help them make music in whatever genre or mood they wish. One simply has to select a mood from the menu of options and chord progressions of known songs in that mood would appear, helping the user to compose a song in their selected mood.

<img width="898" height="496" alt="Screenshot 2026-11-22 at 10 06 32 PM" src="https://github.com/user-attachments/assets/ed6f5dab-ab02-41f6-8017-371db9ca440c" />

<img width="901" height="569" alt="Screenshot 2026-11-22 at 10 07 03 PM" src="https://github.com/user-attachments/assets/3901c119-c7ef-4896-ba26-89a7324e55b1" />

##** Features**

- 5 mood buttons which are Happy, Sad, Chill, Romantic, Energetic.
- Each mood shows its chord progressions as chord diagram images.
- Example songs are listed under each progression.

##** Why I built it**

When wanting to create my own song on the guitar, I wondered which chords to use if I wanted a happy, sad or energetic song, for example. I made this tool to solve this confusion- to create one minimalistic platform which tells what chords to play for what mood.

##**How it works**

- A dictionary maps each mood to a list of progressions. Each progression is a list of chords plus a list of songs.
- A second dictionary maps each chord name to its image file in a folder.
- Clicking a mood button clears the screen, then loops through that mood's progressions and shows each chord image and song.
- The window and buttons are built with Tkinter, and Pillow loads and resizes the chord images.

##**How to Run it**

1. Install Python 3 and Pillow:
     pip install pillow
3. Keep 'mood_chords.py' and the 'chords' folder in the same directory.
4. Run:
    python mood_chords.py


##**Possible improvements**

- Upon clicking a mood, one can also listen to the sound of a chord.
- More moods and progressions can be added.
- One can search a song's name to find its mood and chord progression.
- A browser and mobile version which makes it more accessible.

##** Built using**

Python, Tkinter, Pillow

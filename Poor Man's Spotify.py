import tkinter as tk
import fnmatch
import os
from pygame import mixer

root=tk.Tk()
root.title("Poor Man's Spotify")
root.geometry('600x600')
root.configure(bg='black')

mixer.init()        #intializing mixer

rootpath= "C:\\Users\SIDDHU\Music"
pattern ="*.wav"

previmg=tk.PhotoImage(file="prev_img.png")
nextimg=tk.PhotoImage(file="next_img.png")
stopimg=tk.PhotoImage(file="stop_img.png")
playimg=tk.PhotoImage(file="play_img.png")
pauseimg=tk.PhotoImage(file="pause_img.png")

def select():
    label.configure(text=list_box.get("anchor"))
    mixer.music.load(rootpath+"\\"+list_box.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    list_box.select_clear('active')           #to remove selection from the list_box

def play_next():
    next_song= list_box.curselection()
    next_song=next_song[0]+1
    next_song_name=list_box.get(next_song)
    label.config(text= next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    list_box.select_clear('active')     #to clear the mouse hovering effect on the song name
    list_box.activate(next_song)        #to create a mouse hovering effect on the song name
    list_box.select_set(next_song)

def play_prev():
    prev_song= list_box.curselection()
    prev_song=prev_song[0]-1
    prev_song_name=list_box.get(prev_song)
    label.config(text= prev_song_name)
    mixer.music.load(rootpath+'\\'+ prev_song_name)
    mixer.music.play()
    list_box.select_clear('active')
    list_box.activate(prev_song)
    list_box.select_set(prev_song)

def pause_song():
    if pause["text"]=="pause":
        mixer.music.pause()
        pause["text"]="play"
    else:
        mixer.music.unpause()
        pause["text"] = "pause"

list_box=tk.Listbox(root, fg="cyan",bg="black", width= 100, font=('ds-digital', 14))
list_box.pack(padx=15,pady=50)
for name,sub,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        list_box.insert('end', filename)

label=tk.Label(root,text='', bg='black', fg='yellow', font=('ds-digital', 14))
label.pack(pady=15, padx=15)

top=tk.Frame(root,bg='black')                #frame to hold the control buttons
top.pack()

prev=tk.Button(root,text="prev", image=previmg,bg='black',borderwidth=0, command=play_prev)
prev.pack(pady=10, in_=top, side='left')
stop=tk.Button(root,text="stop",image=stopimg,bg='black', borderwidth=0,command=stop)
stop.pack(pady=10, in_=top, side='left')
play=tk.Button(root,text="play", image=playimg,bg='black', borderwidth=0, command=select)
play.pack(pady=10, in_=top, side='left')
pause=tk.Button(root,text="pause", image=pauseimg,bg='black', borderwidth=0, command=pause_song)
pause.pack(pady=10, in_=top, side='left')
next=tk.Button(root,text="next", image=nextimg,bg='black', borderwidth=0, command=play_next)
next.pack(pady=10, in_=top, side='left')


root.mainloop()














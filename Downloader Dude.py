from tkinter import *
from pytube import YouTube
import tkinter.messagebox as thh
from tkinter import ttk
import webbrowser

root = Tk()
root.geometry('655x584')
root.minsize(655,584)
root.maxsize(655,584)
root.title("Downloader Dude--By Aryan")
root.config(bg="purple")
root.iconbitmap("resource/dude.ico")

def download():
    try:
        progress['value'] = 20
        YouTube(entry.get()).streams.first().download('E:/downloader dude')
        progress['value'] = 100
        p =thh.showinfo('Downloaded', 'Your File Is Downloaded')
        if p == 'ok':
            webbrowser.open("E:/downloader dude")
    except Exception as e:
        thh.showerror("Failed", "Downloading failed")
        progress['value'] = 0

def internet():
    import socket
    IPaddress=socket. gethostbyname(socket. gethostname())
    if IPaddress=="127.0.0.1":
        thh.showerror("Failed", "Check Internet Connection")
    else:
        progress['value'] = 10
        download()


entry = StringVar()

title = Label(root, text="Download--Dude", font="lucida 30 bold", bg="purple", fg="yellow")
title.pack(pady=15)

url = Label(root,text="Url in This Box" ,fg="orange", bg="purple", font="helvetica 25 bold")
url.pack(pady=10)

entry = Entry(root, font="helvetica 20 italic", width=35)
entry.pack(pady=5)

button = Button(root, text="download Now", font='lucida 18 bold', bg='yellow', fg='blue', command=internet)
button.pack(pady=20)

progres = Label(root, text="Progress here", font='lucida 18 bold', bg='purple', fg='orange')
progres.pack(pady=5)

progress = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
progress.pack(pady=40)

root.mainloop()
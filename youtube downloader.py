import tkinter as tk
from tkinter import *
#from PIL import Image
from tkinter import messagebox
import pytube
import time
root = Tk()
def download():
    link = text.get("1.0","end-1c")

    if link == '':
            messagebox.showerror(
                "YouTube Downloader",
                "Please paste a link here")
    else:
            yt = pytube.YouTube(link)
            stream = yt.streams.first()
            time.sleep(2)
            text.delete(1.0,'end') 
            text.insert('end','wait Downloading......') 
            time.sleep(5)
            stream.download()
            messagebox.showinfo(
                "Youtube Downloader",
                'Video has been downloaded sucessfully')
header = Label(root,bg="black",width="300",height="2")
header.place(x=0,y=0)
yt_logo = PhotoImage(file='youtube.png')
logo = Label(root, image = yt_logo,borderwidth=0)

caption = Label(root,text="YouTube Downloader",font=('verenda',10,'bold'))
caption.place(x=50,y=10)
yt1_logo = PhotoImage(file='vishal.png')
logo1 = Label(root, image = yt1_logo,borderwidth=0)
logo1.place(x=100,y=50)


text = Text(root,width=60,height=2,font=('verenda',10,'bold'))
text.place(x=10,y=300)
text.insert('end','Paste your link here')

button = Button(root,text = "Download",relief =RIDGE,font=('verenda',10,'bold'),bg="red",fg="white",command=download)
button.place(x=70,y=370)
root.mainloop()
from tkinter import *
from tkinter import ttk
from yt_dlp import YoutubeDL
root = Tk()
def highest():
    try:
        url=e1.get()
        
        ydl_opts ={
            
            'format' :'best',
            'outtmpl':'download%(titles)s.%(ext)s'
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("The video has been downloaded ")
    except Exception as e:
        print("error ")
def lowest():
    try:
        url=e1.get()
        
        ydl_opts ={
            
            'format' :'worst',
            'outtmpl':'download%(titles)s.%(ext)s'
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("The video has been downloaded ")
    except Exception as e:
        print("error ")
        
def audio():
    try:
        url=e1.get()
        
        ydl_opts ={
            
            'format' :'bestaudio',
            'outtmpl':'download%(titles)s.%(ext)s'
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("The video has been downloaded ")
    except Exception as e:
        print("error ")        
root.title("  YouTube  Installer  ")
root.geometry("300x250")
style=ttk.Style()
style.configure("TButton",foreground="#00a55e",font="Tahoma 8 bold",width=18,)
l1=ttk.Label(root,text="  Video  Installer  ",font="Tahoma 20 bold",foreground="#e42d04")
l1.pack(pady=5,padx=5)
l2=ttk.Label(root,text="  Enter your video URL  ",font="Tahoma 9 bold",foreground="#00a55e")
l2.pack(pady=5,padx=5)
e1=ttk.Entry(root,foreground="#e42d04",width=34)
e1.pack(pady=5,padx=5)
b1=ttk.Button(root,text="Highest",command=highest)
b1.pack(pady=5,padx=5)
b2=ttk.Button(root,text="Lowest",command=lowest)
b2.pack(pady=5,padx=5)
b3=ttk.Button(root,text="Audio",command=audio)
b3.pack(pady=5,padx=5)
l3=ttk.Label(root,text="---< made by asem shalaby >---",foreground="#e42d04",font="Tahoma 7 bold")
l3.pack(pady=5)
root.mainloop()
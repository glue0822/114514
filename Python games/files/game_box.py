from tkinter import *
import subprocess
window=Tk()
window.attributes('-topmost',1)
window.title('Choose one game to play')
window.geometry('500x220')
#留白
front_message=Canvas(window,height=20,width=400)
front_message.pack()
def open_game1():
    window.destroy()
    subprocess.call(['pythonw.exe','game1.py'])
button_command=Button(window,text='Bubble Blaster',command=open_game1,width=25)
button_command.pack()
button_command.place(x=50,y=20)
#Bubble Blaster游戏
def close_window():
    window.destroy()
    subprocess.call(['pythonw.exe', 'hall.py'])
window.protocol('WM_DELETE_WINDOW',close_window)
#在关闭时，自动返回大厅
window.mainloop()

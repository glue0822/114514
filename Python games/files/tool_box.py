from tkinter import *
import subprocess
import os
window=Tk()
window.attributes('-topmost',1)
window.title('Choose one tool to use')
window.geometry("500x220")
#留白
front_message=Canvas(window,height=20,width=400)
front_message.pack()
def open_cmd():
    window.destroy()
    os.startfile('cmd.exe')
button_command=Button(window,text='open cmd',command=open_cmd,width=25)
button_command.pack()
button_command.place(x=50,y=20)
#CMD功能
def close_window():
    window.destroy()
    subprocess.call(['pythonw.exe', 'hall.py'])
window.protocol('WM_DELETE_WINDOW',close_window)
#在关闭时，自动返回大厅
window.mainloop()

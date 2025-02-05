from tkinter import *
import subprocess
window=Tk()
window.attributes('-topmost',1)
window.title('Version details')
canvas=Canvas(window,height=300,width=300)
canvas.pack()
#配置窗口
canvas.create_text(150,150,text='''----------
Python games
Version 1.0.5 for Windows
----------
Games list:
1.Bubble blaster
----------
Tools list:
1.open cmd
----------
Logs:
1.Speed system in ‘Bubble blaster’
is better than 1.0.4
----------
Special thanks:
1.nothing
----------
Release date:2024.12.22
----------''')
def close_window():
    window.destroy()
    subprocess.call(['pythonw.exe', 'hall.py'])
window.protocol('WM_DELETE_WINDOW',close_window)
quit_button=Button(window,text='Back',command=close_window,width=40)
quit_button.pack()
#返回
window.mainloop()

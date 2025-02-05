from tkinter import *
import subprocess
click=1
name=open('./data/pin.ini')
name.seek(0,0)
hall_ui=Tk()
hall_ui.geometry("400x140")
#创建窗口
hall_ui.title('Python games')
hall_ui.attributes('-topmost',1)
#将窗口置于顶层
front_message=Canvas(hall_ui,height=20,width=400)
front_message.pack()
#留白
text_canvas=Canvas(hall_ui,height=20,width=350,bg='red')
text_canvas.pack()
text_canvas.create_text(175,10,text='Welcome,'+str(name.read()),fill='white')
name.close()
hall_ui.update()
def open_games():
    hall_ui.destroy()
    subprocess.call(['pythonw.exe','game_box.py'])
#打开游戏
button_games=Button(hall_ui,text='Play games',width=45,command=open_games)
button_games.pack()
def open_tools():
    hall_ui.destroy()
    subprocess.call(['pythonw.exe', 'tool_box.py'])
#打开工具
def open_ver():
    global click
    if not click < 5:
        hall_ui.destroy()
        subprocess.call(['pythonw.exe', 'version.py'])
        click=1
    else:
        click+=1
#打开版本号详情
button_tools=Button(hall_ui,text='Use tools',justify='center',width=45,command=open_tools)
button_tools.pack()
under_message=Button(hall_ui,text='Version 1.0.5',bd=0,command=open_ver)
under_message.pack()
under_message.place(x=300,y=110)
#留白
hall_ui.mainloop()

from tkinter import *
import subprocess
window=Tk()
#创建窗口
window.attributes('-topmost',1)
#将窗口置于顶层
canvas=Canvas(window,width=300,height=20)
canvas.pack()
pin_file=open(r'.\data\pin.ini','r+')
#打开密码文件
pin_file.seek(0,0)
len_pin_num=str(len(pin_file.read()))
#读出密码有多长，以便接下来做判断
pin_file.seek(0,0)
if len_pin_num == '0':
    window.title('New PIN')
    canvas.create_text(150,10,text='Please enter you PIN:')
    input_field=Entry(window,width=40,exportselection=False)
    input_field.pack()
    def write_pin():
        pin=input_field.get()
        pin_file.write(str(pin))
        pin_file.seek(0,0)
        #“seek(0,0)”很多，不然会因为光标在末尾读不出来密码
        window.destroy()
        pin_file.close()
    button=Button(window,text='OK',command=write_pin,width=10)
    button.pack()
    window.mainloop()
    #结束更改，等待密码输入完成
else:
    window.title('Please log in')
    canvas.create_text(150,10,text='Enter you PIN:')
    input_field=Entry(window,width=40,exportselection=False,show='*')
    input_field.pack()
    def confirm():
        pin_file.seek(0,0)
        if str(pin_file.read()) == str(input_field.get()):
            pin_file.close()
            window.destroy()
            subprocess.call(['pythonw.exe', 'hall.py'])
            #打开接下来的进程
        else:
            input_field.delete(0,END)
            #清空输入框，以便再次尝试
            pin_file.seek(0,0)
    button=Button(window,text='log in',command=confirm,width=10)
    button.pack()
    window.mainloop()

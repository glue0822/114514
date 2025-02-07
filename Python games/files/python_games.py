import subprocess
sign=open(r'data/sign.ini')
sign.seek(0,0)
if sign.read() == 'False':
    subprocess.call(['pythonw.exe', 'log_in.py'])
if sign.read() == 'True':
    subprocess.call(['pythonw.exe', 'hall.py'])
#只是个引导，我怕用python.exe解释的控制台碍事

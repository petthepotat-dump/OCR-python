import subprocess
import os

# install facialexpression
# if mac
if os.name == 'posix':
    subprocess.call(['curl', 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml', '>', 'assets/facialcascade_default.xml'])
else:
    # if windows
    subprocess.call(['powershell', 'Invoke-WebRequest', 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml', '-OutFile', 'assets/facialcascade_default.xml'])




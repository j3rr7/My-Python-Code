# using convert through Python
 
import subprocess
import os
 
i = "*.png"
o = "output.gif"
subprocess.call("convert -delay 100 -loop 5 " + i + " " + o, shell=True)
os.system("start output.gif")
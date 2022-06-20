##import os
##import subprocess
##cmd = "date"
##
####returned_value = os.system(cmd)
####print('returned value:', returned_value)
##
####returned_output = subprocess.check_output(cmd)
####print('Current date is:', returned_output.decode("utf-8"))

from tkinter import Tk
import time



M=["c","b","a"]

r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append("i")

r.update()
time.sleep(.2)
r.update()

r.destroy()




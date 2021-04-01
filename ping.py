# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:38:43 2021

@author: kaisar mirza
"""
#importing OS module    
import os
from tkinter import Label, Tk
    
window = Tk()
window.title('Ping,Pong')
window.geometry('600x400')
    
lbl = Label(window, font =("Arial", 15))
lbl.grid(column=0,row=0)
    
# Open ip_list.txt file 
with open("C:\\Users\kaisa\Desktop\ip_list.txt") as file:
    dump = file.read()
    dump = dump.splitlines()    
    print(dump)
    
        
# Ping for each ip address and write to output.txt
for ip in dump:
    res = os.popen(f"ping {ip}").read()
    if "host" in res:
        print(res)
        f = open("C:\\Users\kaisa\Desktop\output.txt", "a")
        f.write(str(ip) + ' is down ' + '\n')
        f.close()
    else:
        print(res)
        f = open("C:\\Users\kaisa\Desktop\output.txt", "a")
        f.write(str(ip) + ' is up ' + '\n') 
        f.close()

#Open output.txt file
with open("C:\\Users\kaisa\Desktop\output.txt") as file:
        output = file.read()
        print(output)
#Display the results on the GUI    
lbl.configure(text=output)    
# Delete content of output.txt file
with open ("C:\\Users\kaisa\Desktop\output.txt", "w") as file:
   pass

window.mainloop()
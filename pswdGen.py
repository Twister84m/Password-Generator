#init GUI (buttons, radio buttons etc.)
#take user input
#generate password
#display back to user on GUI
#option to save password and copy
#ask for name to save under
#take input and store locally
#close program

#Encryt passwords stored and submitted
#event lister for pressing enter button etc??

import tkinter as tk
from tkinter.constants import ACTIVE, HORIZONTAL
from typing_extensions import IntVar
window = tk.Tk()
window.title("Password Generator")
window.geometry("320x500")

def genPswd():
    return ("fefef")

specialChar = IntVar()

def sliderVal(val):
    print(IntVar)


# def newPass():
#     return("gfb")
newPass = "GEv@Ccu4G£vQ"

label = tk.Label(window, bg="white", padx=15, pady=10, text=f"{newPass}")
label.pack()
slider = tk.Scale(window, from_=5, to=25, orient=HORIZONTAL, command=sliderVal)
slider.pack()
chkBtn4 = tk.Checkbutton(window, text="@!£&#...", variable=specialChar)
chkBtn4.pack()
genBtn = tk.Button(window, text="Generate", padx=30, pady=10, command=genPswd)
genBtn.pack()
copyBtn = tk.Button(window, text="Copy to Clipboard", padx=30, pady=10, command=genPswd)
copyBtn.pack()
saveBtn = tk.Button(window, text="Save", padx=30, pady=10, command=genPswd)
saveBtn.pack()
savedBtn = tk.Button(window, text="Saved", padx=30, pady=10, command=genPswd)
savedBtn.pack()


# show window
window.mainloop()






# CANVAS CANVAS CANVAS CANVAS CANVAS CANVAS CANVAS 
# canvas = tk.Canvas(window, width=280, height=400)
# canvas.pack()
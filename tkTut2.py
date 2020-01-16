from tkinter import *

root = Tk() # creates blank window
topFrame = Frame(root) #makes an invisible container in main root
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


button1 = Button(topFrame, text ="PRESS ME NIGGA", fg="red") # installs a button
button2 = Button(topFrame, text ="PRESS ME BITCH", fg="blue") # installs a button
button3 = Button(topFrame, text ="PRESS ME HOE", fg="green") # installs a button
button4 = Button(bottomFrame, text ="PRESS ME SKANK", fg="purple") # installs a button
# Button(frame, text=(text, fg=(color))

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


root.mainloop() # keeps window open until closed via breaking a loop



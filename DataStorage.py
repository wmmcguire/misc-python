from tkinter import *
import tkinter.filedialog
import sqlite3




class dbEdit:

    

    def open_file(self, event=None):

        db_load = tkinter.filedialog.askopenfilename(parent=window,
                                                      initialdir="C:/Users/")

        if db_load:

            name.set('')
            address.set('')
            phone.set('')
            email.set('')
            doctor.set('')
        

            # Open database
            with open(db_load) as _file:
                conn = sqlite3.connect(_file)
                c = conn.cursor()

                

    def makedb(self, event=None):
        dbn = dbName.get()
        conn = sqlite3.connect(dbn)
        c = conn.cursor



    # # Opens the save as dialog box
    # file = tkinter.filedialog.asksaveasfile(mode='w')
    # if file != None:
    #     # Get text in the text widget and delete the last newline
    #     conn = sqlite3.connect(dbName)
    #     conn.commit()

    #     # Write the text and close
    #     file.write(data)
    #     file.close()

    def clear(self, event=None): #button
        name.set('')
        address.set('')
        phone.set('')
        email.set('')
        doctor.set('')
        

    def submit(self, event=None):
        c.execute("INSERT INTO "+tbName.get()+"VALUES (?, ?, ?, ?, ?)", (name.get(), address.get(), phone.get(), email.get(), doctor.get() ) )
        name.set('')
        address.set('')
        phone.set('')
        email.set('')
        doctor.set('')
        



    def make_table(self, event=None): #button
        c.execute("CREATE TABLE " +tbName.get()+ " (Name VARCHAR, Addr VARCHAR, Phone VARCHAR, Email VARCHAR, Doctor VARCHAR)")






    def __init__(self, window):
        window = Tk()
        window.title("Database Editor")
        window.configure(background="green")
        window.geometry("550x500") # initialize window



        #make a listbox inside a frame
        frame = Frame(window, width=200, height=250)
        frame.pack(side="left", fill="both")



        
        #openShort = window.bind('<Control-i>', open_file())

        name = StringVar(window)
        address = StringVar(window)
        phone = StringVar(window)
        email = StringVar(window)
        doctor = StringVar(window)



        dbName = StringVar(window)
        dbE = Entry(window, textvariable=dbName) #set the name of our new database

        tbName = StringVar(window)
        tbE =Entry(window, textvariable=tbName)



        nameLab = Label(window, text = "Name", font=("arial", 12)).place(x=0,y=300)
        addlab = Label(window, text = "Address", font=("arial", 12)).place(x=100,y=300)
        numlab = Label(window, text = "Phone #", font=("arial", 12)).place(x=200,y=300)
        emailab = Label(window, text = "email", font=("arial", 12)).place(x=300,y=300)
        drlab = Label(window, text = "Doctor", font=("arial", 12)).place(x=400,y=300)
        # entries and labels will be placed on the bottom

        nameE = Entry(window, textvariable=name)
        nameE.place(x=0,y=350)

        addressE = Entry(window, textvariable=address)
        addressE.place(x=100,y=350)

        telNumE = Entry(window, textvariable=phone)
        telNumE.place(x=200,y=350)

        emailE = Entry(window, textvariable=email)
        emailE.place(x=300,y=350)

        drE = Entry(window, textvariable=doctor)
        drE.place(x=400,y=350)

        lsBox = Listbox(frame, width=200, height=250)
        lsBox.pack(side="left", fill="both")

        lsBox.insert(0, 'Name       |       Address         |       Phone#      |         e-mail        |       Doctor')



   
window = Tk()
dtstorage = dbEdit(window)
window.mainloop()    	
	






from tkinter import Tk, Text, Menu, filedialog # importing modules needed for Window, Entry, Menubar and saving the files
import about_us # this is the module that creates a window when you click about/about us
import connection # importing the module behind the anti-piracy

vistas = Tk() # creating a windows, shortcut from Visible Task, although programmers mainly use root or tk = Tk()
vistas.geometry("1400x780") # setting the size of the window when you open the app

entry = Text(vistas, height=1000, width=1000) # Setting up the entry where user can write the file
entry.pack() # If you have no idea what this is, youre not alone

chosen = None # This is making the chosen variable available for all functions, needed to: If you opened a file using openusersfile(), you can save the file
              # clicking only once the save in menubar, without specifying the directory

def openusersfile():
    global chosen # This is making so you can use the chosen variable in this function
    chosen = filedialog.askopenfilename(title="Select a file") # When user clicks the Open in the Menubar/file/open, it asks the user for the dir of the file
    if chosen: # Preventing crash if user doesnt specify the dir
        entry.delete("1.0", "end") # Cleaning out the users table, so then we can insert the file's content without having the last file's content on
        with open(chosen, "r") as file: # Opening the dir file
            entry.insert("1.0", file.read()) # Inserting the file's content into the users box

def saveusersfile():
    global chosen # This is making so you can use the chosen variable in this function
    if chosen: # Preventing crash if user doesnt specify the dir
        with open(chosen, "w", encoding="utf-8") as file: # Opening the dir file
            file.write(entry.get("1.0", "end-1c")) # writing to the user-specified file
    else: # If user doesnt specify the file
        file_dir = filedialog.asksaveasfilename(filetypes=[('All', '*')], defaultextension=".txt") # Asking the user where and how to create a file
        if file_dir: # Preventing crash if user doesnt specify the file
            chosen = file_dir # synchronizing chosen with the file dir
            chosen += '.txt' # making it txt file
            with open(chosen, "w", encoding="utf-8") as file: # opening the file
                file.write(entry.get("1.0","end-1c")) # writing to the file

def abouwind():
    about_us.main(vistas) # The about us window opening function

menubar = connection.verification.ver(vistas) # Here is the anti-piracy embedded script, if the license is wrong the app will crash
filesect = Menu(menubar, tearoff=0) # Adding the file section into the menubar
filesect.add_command(label="Open", command=openusersfile)
filesect.add_command(label="Save", command=saveusersfile)
menubar.add_cascade(label="File", menu=filesect)
abousect = Menu(menubar, tearoff=0) # Adding the about section in the menubar
abousect.add_command(label="About us", command=abouwind)
menubar.add_cascade(label="About", menu=abousect)



vistas.config(menu=menubar)
vistas.mainloop()
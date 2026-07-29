from tkinter import Tk, Text, Menu, filedialog
import about_us
import connection

vistas = Tk()
vistas.geometry("1400x780")

entry = Text(vistas, height=1000, width=1000)
entry.pack()

chosen = None

def openusersfile():
    global chosen
    chosen = filedialog.askopenfilename(title="Select a file")
    if chosen:
        entry.delete("1.0", "end")
        with open(chosen, "r") as file:
            entry.insert("1.0", file.read())

def saveusersfile():
    global chosen
    if chosen:
        with open(chosen, "w", encoding="utf-8") as file:
            file.write(entry.get("1.0", "end-1c"))
    else:
        file_dir = filedialog.asksaveasfilename(filetypes=[('All', '*')], defaultextension=".txt")
        if file_dir:
            chosen = file_dir
            chosen += '.txt'
            with open(chosen, "w", encoding="utf-8") as file:
                file.write(entry.get("1.0","end-1c"))

def abouwind():
    about_us.main(vistas)

menubar = connection.verification.ver(vistas)
filesect = Menu(menubar, tearoff=0)
filesect.add_command(label="Open", command=openusersfile)
filesect.add_command(label="Save", command=saveusersfile)
menubar.add_cascade(label="File", menu=filesect)
abousect = Menu(menubar, tearoff=0)
abousect.add_command(label="About us", command=abouwind)
menubar.add_cascade(label="About", menu=abousect)



vistas.config(menu=menubar)
vistas.mainloop()
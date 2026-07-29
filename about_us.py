import tkinter as tk

def main(root):
    vistas = tk.Toplevel(root)
    vistas.geometry("500x500")

    abtcr_label = tk.Label(vistas, text="Hey there, nothing here! Why do you care about my god damn life?")
    abtcr_label.pack(padx=10,pady=10)
    vistas.lift()
    vistas.focus_set()

    vistas.mainloop()
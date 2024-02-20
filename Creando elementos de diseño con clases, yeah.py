from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import ttk

root = Tk()
root.geometry("900x600")
root.title("Creando elementos de diseño con clases")

gui_elements = ["Botón","Etiqueta","Menú desplegable"]
dropdown = ttk.Combobox(root,state="readonly",values = gui_elements)
dropdown.pack()

class create_elements():
    def __init__(self):
        print("Esta es la clase create_elements")
        
    def create_label(self):
        label = Label(root,text="Se a creado una nueva etiqueta usando clases",fg="red")
        label.pack()
        
    def create_button(self):
        btn = Button(root,text="Botón",command=self.message)
        btn.pack(padx=20,pady=10)
        
    def create_dropdown(self):
        value = ["Creaste","un","menú","desplegable","usando","las","clases",":)"]
        class_dropdown = ttk.Combobox(root,state="readonly",values=value)
        class_dropdown.pack()
        
    def choose(self):
        global dropdown
        element = dropdown.get()
        if(element == "Etiqueta"):
            self.create_label()
        elif(element == "Botón"):
            self.create_button()
        elif(element == "Menú desplegable"):
            self.create_dropdown()
            
    def message(self):
        messagebox.showinfo("Mostrar información","Haz presionado el botón creado por la clase")
        
obj_of_create_elements = create_elements()
btn2 = Button(root,text="Crear Elemento",command=obj_of_create_elements.choose)
btn2.pack(padx=20,pady=10)

root.mainloop()
from tkinter import *
from tkinter import messagebox
from difusao_pura_solve import Calculator

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("Difusão Pura - Método Explícito")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        fields = 'Partições de Tempo', 'C', 'dx', 'dt'
        ents = self.__make_form__(self.master, fields)
        # creating a button instance
        Button(self, text="Sobre", command=self.__about__).pack(side=RIGHT)
        Button(self, text="Executar", \
        command=(lambda e=ents: self.__fetch__(e))).pack(side=RIGHT)
        Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
    
    def __about__(self):
        messagebox.showinfo("init_window","Grupo:\nErick Grilo, Max Fratane,\nVitor Araujo, Vítor Lourenço")
        
    def __make_form__(self, root, fields):
        entries = []
        for field in fields:
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent = Entry(row)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((field, ent))

        return entries

    def __fetch__(self, ents):
        #qdt_time, c, dx, dt
        
        Calculator.careless_whispers(int(ents[0][1].get()), \
        float(ents[1][1].get()), float(ents[2][1].get()), float(ents[3][1].get()))

root = Tk()

#size of the window
root.geometry("370x400")
image = PhotoImage(file="img.png")
label = Label(image=image)
label.pack()
app = Window(root)
root.mainloop()

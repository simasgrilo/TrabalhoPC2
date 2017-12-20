from tkinter import *
from tkinter import messagebox
from rk import Calculator

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)

   def state(self):
      return map((lambda var: var.get()), self.vars)

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("Oscilador de Van der Pol - Runge-Kutta")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        fields = 'Ordens', 'Partições', 't0', 'tn', 'x0', 'v0', 'mu', 'Amplitute', 'Omega'
        ents, checkbar = self.__make_form__(self.master, fields)
        # creating a button instance
        Button(self, text="Sobre", command=self.__about__).pack(side=RIGHT)
        Button(self, text="Tableau", command=self.__tableau__).pack(side=RIGHT)
        Button(self, text="Executar", \
        command=(lambda e=ents: self.__fetch__(e,list(checkbar.state())))).pack(side=RIGHT)
        Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
    
    def __about__(self):
        messagebox.showinfo("Grupo","Grupo:\nErick Grilo, Max Fratane,\nVitor Araujo, Vítor Lourenço \nPeríodo: 2017.2")
        
    def __tableau__(self):
        novi = Toplevel()
        canvas = Canvas(novi, width = 600, height = 200)
        canvas.pack(expand = NO, fill = BOTH)
        gif1 = PhotoImage(file = 'tableau.png')
                                    #image not visual
        canvas.create_image(50, 10, image = gif1, anchor = NW)
        #assigned the gif1 to the canvas object
        canvas.gif1 = gif1
    
        
    def __make_form__(self, root, fields):
        entries = []
        for field in fields:
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            if(field == "Ordens"):
                ckbar = Checkbar(root, ['1', '2', '3', '4'])
                ckbar.pack(side=TOP)
            else:
                ent = Entry(row)
                ent.pack(side=RIGHT, expand=YES, fill=X)
                entries.append((field, ent))

        return entries, ckbar

    def __fetch__(self, ents, cb_states):
        orders = []
        for i in range(len(cb_states)):
            if(cb_states[i] == 1):
                orders.append(i+1)
        #orders, partition, t_variation, initial_condition, mu, amplitude, omega
        args = [orders, int(ents[0][1].get()), \
        (float(ents[1][1].get()), float(ents[2][1].get())), \
        (float(ents[3][1].get()), float(ents[4][1].get())), \
        float(ents[5][1].get()), float(ents[6][1].get()), float(ents[7][1].get())]

        Calculator.calculate(*args)

root = Tk()

#size of the window
root.geometry("370x400")
image = PhotoImage(file="img.png")
label = Label(image=image)
label.pack()
app = Window(root)
root.mainloop()

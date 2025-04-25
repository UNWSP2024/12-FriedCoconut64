import tkinter
import tkinter.messagebox

class show_cost:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("Joe's Automative Services")
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()


        self.cb1 = tkinter.Checkbutton(self.top_frame, text = 'Oil Change: $30', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text='Lube Job: $20', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text='Radiator Flush: $40', variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text='Transmission Fluid: $100', variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text='Inspection: $35', variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text='Muffler Replacement: $200', variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text='Tire Rotation: $20', variable=self.cb_var7)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate Cost', command= self.show_cost)
        self.button_quit = tkinter.Button(self.main_window, text = 'Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.button_quit.pack(side='bottom')

        self.label = tkinter.Label(self.main_window)
        self.label.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_cost(self):
        costs = {
                'Oil Change': 30,
                'Lube Job': 20,
                'Radiator Flush': 40,
                'Transmission Fluid': 100,
                'Inspection': 35,
                'Muffler Replacement': 200,
                'Tire Rotation': 20,
                }


        total_cost = 0
        if self.cb_var1.get():
            total_cost += costs['Oil Change']
        if self.cb_var2.get():
            total_cost += costs['Lube Job']
        if self.cb_var3.get():
            total_cost += costs['Radiator Flush']
        if self.cb_var4.get():
            total_cost += costs['Transmission Fluid']
        if self.cb_var5.get():
            total_cost += costs['Inspection']
        if self.cb_var6.get():
            total_cost += costs['Muffler Replacement']
        if self.cb_var7.get():
            total_cost += costs['Tire Rotation']


        tkinter.messagebox.showinfo("Total Cost", "The total cost for your selection is " + str(total_cost) + ' dollars')

if __name__ == '__main__':
    repair = show_cost()

# Program #2, Donovan Thompson 4/25/2025

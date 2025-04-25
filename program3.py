import tkinter
import tkinter.messagebox

class call_cost:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("Long-Distance Calls")
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.rb_var = tkinter.IntVar(value=1)


        self.rb1 = tkinter.Radiobutton(self.top_frame, text = 'Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02', variable=self.rb_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12', variable=self.rb_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Off-Peak (midnight through 5:59 P.M.) 	$0.05', variable=self.rb_var,value=3)

        self.label_entry = tkinter.Label(self.bottom_frame, text='Enter Phone Call Length (in minutes):')
        self.label_entry.pack()
        self.eb1 = tkinter.Entry(self.bottom_frame, width=10)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.eb1.pack()

        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate Cost', command= self.call_cost)
        self.button_quit = tkinter.Button(self.main_window, text = 'Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='bottom')
        self.button_quit.pack(side='bottom')

        self.label = tkinter.Label(self.main_window)
        self.label.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def call_cost(self):
        costs = {
                1: 0.02,
                2: 0.12,
                3: 0.05
                }
        try:
            call_length = float(self.eb1.get())
            total_cost = round(costs[self.rb_var.get()] * call_length, 2)
            tkinter.messagebox.showinfo("Total Cost", "The total cost for your selection is " + str(total_cost) + ' dollars')
        except ValueError:
            tkinter.messagebox.showerror("Input Error", "Please enter a valid number for call length.")

if __name__ == '__main__':
    repair = call_cost()

# Program #3, Donovan Thompson 4/25/2025

import tkinter
import tkinter.messagebox

class mile_per_gallon:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("MPG Converter")
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.prompt_label = tkinter.Label(self.top_frame, text = "Enter gas tank size in Gallons:")
        self.gallon_entry = tkinter.Entry(self.top_frame, width=5)

        self.prompt_label2 = tkinter.Label(self.top_frame, text = "Enter Total mileage on full tank:")
        self.mile_entry = tkinter.Entry(self.top_frame, width=7)

        self.prompt_label.pack(side='top')
        self.gallon_entry.pack(side='top')
        self.prompt_label2.pack(side='top')
        self.mile_entry.pack(side='top')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate', command= self.mile_per_gallon)
        self.button_quit = tkinter.Button(self.main_window, text = 'Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.button_quit.pack(side='bottom')

        self.label = tkinter.Label(self.main_window)
        self.label.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def mile_per_gallon(self):
        gallons = float(self.gallon_entry.get())
        miles = float(self.mile_entry.get())

        total_mpg = miles/gallons

        tkinter.messagebox.showinfo("MPG", "The MPG on this car is " + str(total_mpg))

if __name__ == '__main__':
    coverter = mile_per_gallon()

# Program #1, Donovan Thompson 4/25/2025

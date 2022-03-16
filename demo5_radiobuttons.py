import tkinter
import tkinter.messagebox

class radiobutton:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('Output as Label')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        #Have to pack everything, including the frames 
        self.top_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'top')

        #similar to making the string variable in demo 4
        self.radio_var = tkinter.IntVar()

        #create a radio button
        self.rb1 = tkinter.Radiobutton(self.top_frame, text = 'Option 1', variable= self.radio_var, value= 10)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text = 'Option 2', variable= self.radio_var, value= 20)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text = 'Option 3', variable= self.radio_var, value= 30)

        #set the default button 
        self.rb2.select()

        #pack the radiobuttons
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.ok_button = tkinter.Button(self.bottom_frame, text = 'OK', command = self.show_choice)
        self.reset_button = tkinter.Button(self.bottom_frame, text = 'Reset', command=self.rb1.select)
        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        self.ok_button.pack(side = 'left')
        self.reset_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo('Selection', 'You have selected option' + str(self.radio_var.get()))

MyGUI = radiobutton()

print('moving on.....')

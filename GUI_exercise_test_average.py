from cgitb import text
import tkinter

class TestAverageGUI:

    def __init__(self):
        
        #set up the main window
        self.main_window = tkinter.Tk()
        self.main_window.geometry('600x300')
        self.main_window.title('Test Average Generator')

        #set up the frames
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.output_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        #pack the frames
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.output_frame.pack()
        self.button_frame.pack()

        #set and pack the labels 
        self.prompt_label1 = tkinter.Label(self.test1_frame, text = 'Enter the score for test 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame, width = 10)
        self.prompt_label1.pack(side = 'left')
        self.test1_entry.pack(side = 'left')

        self.prompt_label2 = tkinter.Label(self.test2_frame, text = 'Enter the score for test 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame, width = 10)
        self.prompt_label2.pack(side = 'left')
        self.test2_entry.pack(side = 'left')

        self.prompt_label3 = tkinter.Label(self.test3_frame, text = 'Enter the score for test 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame, width = 10)
        self.prompt_label3.pack(side = 'left')
        self.test3_entry.pack(side = 'left')

        self.average_var = tkinter.StringVar()
        self.average_label = tkinter.Label(self.output_frame, text = 'Average')
        self.output_label = tkinter.Label(self.output_frame, textvariable = self.average_var)
        self.average_label.pack(side = 'left')
        self.output_label.pack(side = 'left')
        
        self.average_button = tkinter.Button(self.button_frame, text = 'Average', command = self.average)
        self.quit_button = tkinter.Button(self.button_frame, text = 'Quit', command = self.main_window.destroy)
        self.average_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        tkinter.mainloop()

    def average(self):
        
        test1 = float(self.test1_entry.get())
        test2 = float(self.test2_entry.get())
        test3 = float(self.test3_entry.get())
        avg = round((test1 + test2 + test3)/3, 2)
        self.average_var.set(avg)

my_gui = TestAverageGUI()

print('Moving on...')

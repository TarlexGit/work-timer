import tkinter as tk
from calc_and_get import get_end_time

class TimeCalculator:
    """This is the main app class
    Attributes
    ----------
    input* : Entry
        displaying and input fields
    label_* : Label
        displaying and input fields
    Methods
    -------
    builder()
        Setting and pack(unmap) widgets
    """
    def __init__(self, master) -> None:
        self.master = master
        self.label_h = tk.Label(master, text='Enter hours')
        self.input1 = tk.Entry(master, text='Hours')
        self.input2 = tk.Entry(master, text='Minutes')
        self.label_m = tk.Label(master, text='Enter minutes')

        self.request_label = tk.Label(master, text="")
        
    def builder(self):
        frame = tk.Frame(self.master, width=400, height=200)
        self.master.title('Working Time Calculator')

        self.label_h.pack()
        self.input1.pack()
        self.label_m.pack()
        self.input2.pack()
        self.request_label.pack()

        button1= tk.Button(self.master, text='Calculate', command=self.evaluate)
        button1.pack()
        frame.pack()
        frame.focus()

    def evaluate(self):
        a_str = self.input1.get()
        b_str = self.input2.get()
        try:
            a = int(a_str)
            b = int(b_str)
            self.request_label['text'] = '{}'.format(get_end_time(hours=a,minutes=b))
        except ValueError:
            self.request_label['text'] = 'Wrong value(s) hours "{}" and/or minutes"{}" \
                                          \n\nmust be in 0..23 and 0..59'.format(a_str, b_str)


if __name__ == '__main__':
    root = tk.Tk()
    Tc = TimeCalculator(root)
    Tc.builder()
    root.mainloop()
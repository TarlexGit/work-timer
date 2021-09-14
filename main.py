import tkinter as tk
from calc_and_get import get_end_time

class TimeCalculator:
    def __init__(self, master) -> None:
        frame = tk.Frame(master, width=400, height=200)
        master.title('Work time calculator')
        self.input1 = tk.Entry(master, text='Hours')
        self.input2 = tk.Entry(master, text='Minutes')
        button1= tk.Button(master, text='Sum', command=self.evaluate)

        self.label_h = tk.Label(master, text='Whrite hours')
        self.label_m = tk.Label(master, text='Whrite minutes')
        self.request_label = tk.Label(master, text="")
        
        self.label_h.pack()
        self.input1.pack()
        self.label_m.pack()
        self.input2.pack()
        self.request_label.pack()
        button1.pack()
        frame.pack()
        frame.focus()

    def evaluate(self):
        a_str = self.input1.get()
        b_str = self.input2.get()
        try:
            a = int(a_str)
            b = int(b_str)
        except ValueError:
            self.request_label['text'] = "Wrong value(s) {} and/or {}".format(a_str, b_str)
            return
        self.request_label['text'] = '{}'.format(get_end_time(hours=a,minutes=b))

if __name__ == '__main__':
    root = tk.Tk()
    TimeCalculator(root)
    root.mainloop()
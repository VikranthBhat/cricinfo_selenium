import tkinter as tk
from Cricinfo_selenium import cricinfo_selenium


def run_cricinfo(*args):
    root.update()
    file_gen=cricinfo_selenium.Cricinfo_selenium()
    print(input_url.get())
    file_gen.cricinfo_selenium(output_file.get())
    # cricinfo_selenium.cricinfo_selenium(input_url)


root = tk.Tk()
root.title("Cricinfo data")
frame = tk.Frame(root, relief='raised', bd=5, width=100)
frame.grid(column=0, row=0, sticky=("N", "E", "W", "S"))

input_url = tk.StringVar(frame)
tk.Label(frame, text="input URL", pady=10).grid(row=1, column=1, sticky="E")
output_file=tk.Entry(frame, width=80, textvariable=input_url)
output_file.grid(row= 1, column= 2, sticky='W')

tk.Button(frame, text="Run", command=run_cricinfo, state="active").grid(row=2, column=1, sticky="N")
root.bind('<Return>', run_cricinfo)
root.mainloop()

# import tkinter as tk
# win = tk.Tk()
# win.title("First program")#title of progeam
# win.geometry("300x300")

# label = tk.Label(win, text="First GUI", font= ("Serif",20))# pop at screen
# label.pack()

# text = tk.Text(win, height=1, font=("serif",15)) 
# text.pack(padx=15, pady=15)

# bt = tk.Button(win, text="CLICK HERE! ")
# bt.pack(padx=15, pady=15)

# grid_btns = tk.Frame(win)
# grid_btns.columnconfigure(0, weight=1)
# grid_btns.columnconfigure(1, weight=1)
# grid_btns.columnconfigure(2, weight=1)

# bt1 = tk.Button(grid_btns, text="1")
# bt1.grid(row=0, column=0, sticky=tk.W+tk.E)

# bt2 = tk.Button(grid_btns, text="2")
# bt2.grid(row=0, column=1 ,sticky=tk.W+tk.E)

# bt3 = tk.Button(grid_btns, text="3")
# bt3.grid(row=0, column=2 , sticky=tk.W+tk.E)

# bt4 = tk.Button(grid_btns, text="4")
# bt4.grid(row=2, column=0 , sticky=tk.W+tk.E)

# bt5 = tk.Button(grid_btns, text="5")
# bt5.grid(row=2, column=1 , sticky=tk.W+tk.E)

# bt6 = tk.Button(grid_btns, text="6")
# bt6.grid(row=2, column=2 , sticky=tk.W+tk.E)

# bt7 = tk.Button(grid_btns, text="7")
# bt7.grid(row=3, column=0 , sticky=tk.W+tk.E)

# bt8 = tk.Button(grid_btns, text="8")
# bt8.grid(row=3, column=1 , sticky=tk.W+tk.E)

# bt9 = tk.Button(grid_btns, text="9")
# bt9.grid(row=3, column=2 , sticky=tk.W+tk.E)

# bt0 = tk.Button(grid_btns, text="0")
# bt0.grid(row=4, column=1 , sticky=tk.W+tk.E)
# grid_btns.pack(fill="both")
# win.mainloop()


# #WITH CLASS:
# import tkinter as tk
# class bycls:
#     def __init__(self):
        
#      self.win=tk.Tk()

#      self.label= tk.Label(self.win, text = "Message Program", font=("Arial",10))
#      self.label.pack()
#      self.win.geometry("500x200")

#      self.textbox= tk.Text(self.win, height=3,)
#      self.textbox.pack(padx=10,pady=10)

#     #  self.chk= tk.IntVar()
#     #  self.check= tk.Checkbutton(self.win, text = "Click for Checking", variable=self.chk)
#     #  self.check.pack(padx=10,pady=10)

#      self.btn= tk.Button(self.win, text="click for poping the message", command=self.show)
#      self.btn.pack(padx=10,pady=10)

#      self.win.mainloop()
#      self.win.wm_colormapwindows("red")
    
#     def show(self):
#        print("The Message is Being printed ")

# bycls()

#CUSTOM TKINTER MODULE:
import customtkinter as ct
ct.set_appearance_mode("dark")
ct.set_default_color_theme("dark-blue")

win= ct.Ctk()
win.geometry("500x300")
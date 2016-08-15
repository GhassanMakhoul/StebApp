from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print( "hello world")
       # if tkMessageBox.askyesno("Print", "Print this report?"):
        #    report.print()

    def createWidgets(self):
        self.createMenu()
        self.QUIT = Button(self)
        self.QUIT['text'] = "QUIT"
        self.QUIT['fg'] = 'red'
        self.QUIT["command"] = self.quit
        self.QUIT.config(relief=SUNKEN)
       
        self.QUIT.pack({"side":"right"})

        self.hi_there = Button(self)
        self.hi_there['text'] = "hello"
        self.hi_there['command'] = self.say_hi
        self.hi_there.config(relief=RIDGE)
        
        self.hi_there.pack({"side":"left"})

  
     
    def createMenu(self):
  
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff =0)
        filemenu.add_command(label="Open", command=self.say_hi)
        filemenu.add_command(label="Save", command=self.say_hi)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        optionsmenu = Menu(menubar, tearoff=0)
        optionsmenu.add_command(label="Help", command=self.say_hi)
        optionsmenu.add_command(label="Preferences", command=self.say_hi)
        optionsmenu.add_separator()
        optionsmenu.add_command(label="Turn off Ghassan", command = root.quit)
        
        menubar.add_cascade(label="Options", menu=optionsmenu)
       
       


        root.config(menu=menubar)
    def createToolBar(self):
        toolbar = Frame(root)
        b = Button(toolbar, text ="new", width=6, command=self.say_hi)
        b.pack(side=LEFT, padx=2, pady=2)
        
        b = Button(toolbar, text ="Open", width =6, command=self.say_hi)
        b.pack(side=LEFT, padx=2, pady=2)
        toolbar.pack(side=TOP, fill=X)


    def callback(self, event):
        print "clicked at", event.x, event.y

    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.master.bind("<Button-1>", self.callback)
        self.pack()
        self.createMenu()
        self.createWidgets()
        self.createToolBar()


root = Tk()
root.geometry("800x400")
app = Application(master = root)
app.mainloop()
root.destroy()  
     

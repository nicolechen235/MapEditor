from Tkinter import *


class TextureList(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.data_group = [1]

        self.group_list = Listbox(self, selectmode=SINGLE)
        self.group_list.insert(END, "GROUP 0")
        self.group_list.pack()


class Application(Frame):
    def say_hi(self):
        print self.message

    def create_widgets(self):
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self,  master=None):
        Frame.__init__(self, master)

        self.texture_listbox = TextureList(self)

        self.QUIT = Button(self)
        self.hi_there = Button(self)

        self.texture_listbox.pack(side='top')
        self.pack()
        self.create_widgets();


root = Tk()
app = Application(master=root)

app.mainloop()
root.destroy()

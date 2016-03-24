from Tkinter import *


class TextureList(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.data_group = [1]

        self.group_list = Listbox(self, selectmode=SINGLE)
        self.group_list.insert(END, "GROUP 0")
        self.group_list.pack()


class Application(Frame):
    def __init__(self,  master=None):
        Frame.__init__(self, master)

        self.texture_listbox = TextureList(self)

        self.QUIT = Button(self, text='QUIT', fg='red', command=self.quit)
        self.QUIT.pack(side='bottom')

        self.texture_listbox.pack(side='left')
        self.pack()


root = Tk()
app = Application(master=root)

app.mainloop()

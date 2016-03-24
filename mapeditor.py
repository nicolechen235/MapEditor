from Tkinter import *


class TextureList(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.data_group = [1]

        self.group_listbox = Listbox(self, selectmode=SINGLE)
        self.group_listbox.insert(END, "GROUP 0")
        self.group_listbox.pack()

        self.add_texture_button = Button(self, text='Add Texture', command=self.add_texture)
        self.add_texture_button.pack(side="bottom")

        self.add_group_button = Button(self, text='Add Group', command=self.add_group)
        self.add_group_button.pack(side="left")

    def group_in_data_list(self, index, left, right):
        if right - left <= 1:
            print left, right
            return left

        pivot = (left + right) / 2
        # left difference

        print index, left, pivot, self.data_group[left:right]
        ld = index - sum(self.data_group[left:pivot])
        print index, self.data_group[left:right], ld
        if ld < 0:
            return self.group_in_data_list(index, left, pivot)
        else:
            return self.group_in_data_list(ld, pivot, right)

    def group_for_selection(self, index=0):
        return self.group_in_data_list(index, 0, len(self.data_group))

    def add_texture(self):
        cur_group = self.group_for_selection(self.group_listbox.curselection()[0])
        cg_last_index = sum(self.data_group[:cur_group+1])
        print self.data_group, "group =", cur_group, "cur_index =", cg_last_index
        self.group_listbox.insert(cg_last_index, "-texture: "+str(cur_group)+str(self.data_group[cur_group]))
        self.data_group[cur_group] += 1
        print cur_group

    def add_group(self):
        self.group_listbox.insert(END, "GROUP "+str(len(self.data_group)))
        self.data_group.append(1)



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

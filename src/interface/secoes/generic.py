import customtkinter

Frame = customtkinter.CTkFrame


class InputValueWidget(Frame):
    def __init__(self, master, text,label_width=80,entry_width=140):

    

        super().__init__(master,fg_color="transparent")
        label = customtkinter.CTkLabel(self, text=text, width=label_width)
        entry = customtkinter.CTkEntry(self, width=entry_width)

        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)


class SwitchWidget(Frame):
    def __init__(self, master, text,):
        super().__init__(master)

        label = customtkinter.CTkLabel(self, text=text,width=40)
        switch = customtkinter.CTkSwitch(self, width=40)

        label.grid(row=0, column=0)
        switch.grid(row=0, column=1,)
       

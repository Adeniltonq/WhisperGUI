import customtkinter
import tkinter as Tk

Frame = customtkinter.CTkFrame


class GloballLabel(customtkinter.CTkLabel):

    def __init__(self, master, *args, **kwargs):

        super().__init__(
            master,
            anchor="w",
            *args,
            **kwargs
        )


class InputValueWidget(Frame):
    def __init__(self, master, text,label_width=100,entry_width=140,on_top=False):

        super().__init__(master,fg_color="transparent")
        label = GloballLabel(self, text=text, width=label_width)
        entry = customtkinter.CTkEntry(self, width=entry_width)


        if on_top:
            label.grid(row=0, column=0,sticky="w")
            entry.grid(row=1, column=0,)
        else:
            label.grid(row=0, column=0)
            entry.grid(row=0, column=1)
       


class SwitchWidget(Frame):
    def __init__(self, master, text):
        super().__init__(master,fg_color="transparent")

        label = GloballLabel(self, text=text)
        label.grid(row=0, column=0)

        switch = customtkinter.CTkSwitch(self,text='',width=0,)
        switch.grid(row=0, column=1,padx=(5,0))
       


class SliderWidget(Frame):
    def __init__(self,master,text,label_width=120,slider_width=40,from_=0,to=1):
        super().__init__(master,fg_color="transparent")

        value_slider = Tk.DoubleVar()


        def atualizar(valor):
            value_slider.set(round(float(valor),3))


        label = GloballLabel(self, width=label_width,text=text)
        label.grid(row=0,column=0)

        slider = customtkinter.CTkSlider(
            self,
            width=slider_width,
            from_=from_,
            to=to,
            variable=value_slider,
            number_of_steps=100,
            command=atualizar)
            
        slider.grid(row=0,column=1,)

        entry = customtkinter.CTkEntry(self,width=40,textvariable=value_slider)
        entry.grid(row=0,column=2)




    







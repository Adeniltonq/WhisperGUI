import customtkinter
import tkinter as Tk
from tkinter import filedialog
from tkinter import StringVar
import time

Frame = customtkinter.CTkFrame
Toplevel = customtkinter.CTkToplevel



class GloballLabel(customtkinter.CTkLabel):

    def __init__(self, master, *args, **kwargs):

        super().__init__(
            master,
            anchor="w",
            *args,
            **kwargs
        )


class InputValueWidget(Frame):
    def __init__(self, master, text='',label_width=100,entry_width=140,on_top=False,textvariable = None ):

        super().__init__(master,fg_color="transparent")

        def is_float(value: str) -> bool:
            return  value == '' or all(c.isnumeric() or c in "." for c in value)
            
        def set_number_int(event,textvariable ,ErrorMessage=''):
            text = event.widget.get()

            if  not text.isdigit():
                print(ErrorMessage)
                event.widget.delete(0,'end')
                event.widget.insert(0,'')

            else: 
                textvariable.set(int(text))

        def set_number_float(event, textvariable,ErrorMessage='TTTT'):
            text = event.widget.get()
            

            if not is_float(text):
                print(ErrorMessage)
                event.widget.delete(0,'end')
                event.widget.insert(0,'0')

            else:
                if float(text) > 1:
                    textvariable.set(0) 
                else:  
                    textvariable.set(float(text))
                

        
        label = GloballLabel(self, text=text, width=label_width)


        if isinstance(textvariable,Tk.StringVar) or textvariable == None :
            self.entry = customtkinter.CTkEntry(self, width=entry_width,textvariable = textvariable)
            
        elif isinstance(textvariable,Tk.IntVar):
            self.entry = customtkinter.CTkEntry(self, width=entry_width)

            self.entry.bind('<KeyRelease>',lambda event: set_number_int(event=event,textvariable=textvariable))

        elif isinstance(textvariable,Tk.DoubleVar):
            self.entry = customtkinter.CTkEntry(self, width=entry_width,textvariable=textvariable)
            self.entry.bind('<FocusOut>',lambda event: set_number_float(event=event,textvariable=textvariable))

        if text == '':
            self.entry.grid(row=0, column=0)
        else:
            if on_top:
                label.grid(row=0, column=0,sticky="w")
                self.entry.grid(row=1, column=0,)
            else:
                label.grid(row=0, column=0)
                self.entry.grid(row=0, column=1)

class TextAreaWidget(Frame):
    def __init__(self, master,text,width=300,height=390,on_top=False):

        super().__init__(master,fg_color="transparent")

        prompt_title = customtkinter.CTkLabel(self,text=text)
        prompt_title.grid(row=0)
        textbox_widget = customtkinter.CTkTextbox(self,fg_color='gray20',width=width,height=height)
        textbox_widget.grid(row=1,rowspan=10,padx=10)



class SwitchWidget(Frame):
    def __init__(self, master, text,command):
        super().__init__(master,fg_color="transparent")

        label = GloballLabel(self, text=text)
        label.grid(row=0, column=0)

        self.switch = customtkinter.CTkSwitch(self,text='',width=0,command=command)
        self.switch.grid(row=0, column=1,padx=(5,0))
       


class SliderWidget(Frame):
    def __init__(self,master,text,label_width=120,slider_width=180,from_=0,to=1):
        super().__init__(master,fg_color="transparent")

        value_slider = Tk.DoubleVar()
        value_slider.set(0.1)


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

        entry = InputValueWidget(self,textvariable=value_slider,entry_width=40)
        entry.grid(row=0,column=2)



class FilesPathWidget(Frame):
    def __init__(self, master, text,label_width=100,entry_width=140,on_top=False,textvariable:StringVar = None):

        
        def buscar_diretorio():
          textvariable.set(filedialog.askopenfiles()) 

        super().__init__(master,fg_color="transparent")

        label = GloballLabel(self, text=text, width=label_width)
        entry = customtkinter.CTkEntry(self, width=entry_width,textvariable=textvariable)
        button = customtkinter.CTkButton(self,width=40,command=buscar_diretorio,text='/')
        

        if on_top:
            label.grid(row=0, column=0,sticky="w")
            entry.grid(row=1, column=0,)
            button.grid(row=1,column=2)
        else:
            label.grid(row=0, column=0)
            entry.grid(row=0, column=1)
            button.grid(row=0,column=3)
class FilePathWidget(Frame):
    def __init__(self, master, text:str,label_width=100,entry_width=50,on_top=False):

        str_var = Tk.StringVar()
        
        def buscar_diretorio():
          str_var.set(filedialog.askopenfile()) 

        super().__init__(master,fg_color="transparent")

        entry = customtkinter.CTkEntry(self, width=entry_width,textvariable=str_var)
        button = customtkinter.CTkButton(self,width=40,command=buscar_diretorio,text='/')
        label = GloballLabel(self, text=text, width=label_width)

        if not text.strip():
            entry.grid(row=0, column=0)
            button.grid(row=0,column=1)
        else: 
            if on_top:
                label.grid(row=0, column=0,sticky="w")
                entry.grid(row=1, column=0,)
                button.grid(row=1,column=2)
            else:
                label.grid(row=0, column=0)
                entry.grid(row=0, column=1)
                button.grid(row=0,column=3)

       
       
        

        
            
        



class DirPathWidget(Frame):
    def __init__(self, master, text,label_width=100,entry_width=140,on_top=False):

        str_var = Tk.StringVar()
        
        def buscar_diretorio():
          str_var.set(filedialog.askdirectory(initialdir="./",)) 

        super().__init__(master,fg_color="transparent")

        label = GloballLabel(self, text=text, width=label_width)
        entry = customtkinter.CTkEntry(self, width=entry_width,textvariable=str_var)
        button = customtkinter.CTkButton(self,width=40,command=buscar_diretorio,text='/')
        

        if on_top:
            label.grid(row=0, column=0,sticky="w")
            entry.grid(row=1, column=0,)
            button.grid(row=1,column=2)
        else:
            label.grid(row=0, column=0)
            entry.grid(row=0, column=1)
            button.grid(row=0,column=3)

       
       
        


    







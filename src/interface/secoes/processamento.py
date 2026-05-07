import customtkinter
from secoes.generic import InputValueWidget, SwitchWidget
Frame = customtkinter.CTkFrame





class SwitchWidgetForGpu(Frame):
    def __init__(self, master):
        super().__init__(master)
        SwitchWidget(self,'GPU',).grid(row=0,column=0)
        InputValueWidget(self,"GPU_ID",label_width=20,entry_width=30).grid(row=0,column=1)


       
        
       




class ProcesWidget(Frame):
    def __init__(self,master):
        super().__init__(master)
        
        titulo = customtkinter.CTkLabel(self,text='Processamento',height=30)
        titulo.grid(row=0,column=0,columnspan=2)


        InputValueWidget(self,'Nucleos:').grid(row=1, column=0)
        InputValueWidget(self,'Processos:').grid(row=2, column=0)
        SwitchWidgetForGpu(self).grid(row=3, column=0)
        
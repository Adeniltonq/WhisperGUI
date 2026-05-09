import customtkinter
from secoes.generic import InputValueWidget, SwitchWidget
Frame = customtkinter.CTkFrame





class SwitchWidgetForGpu(Frame):
    def __init__(self, master):
        super().__init__(master)

        gpu_switch_widget = SwitchWidget(self,'GPU',)
        gpu_switch_widget.grid(row=0,column=0,padx=(14,0))


        gpu_id_in_widget= InputValueWidget(self,"GPU_ID",label_width=20,entry_width=50)
        gpu_id_in_widget.grid(row=0,column=1,padx=(60,0))

       
        
       




class ProcesWidget(Frame):
    def __init__(self,master):
       
        super().__init__(master)

        
        
        titulo = customtkinter.CTkLabel(self,text='Processamento',height=30)
        titulo.grid(row=0,column=0,columnspan=2)


        InputValueWidget(self,'Nucleos:').grid(row=1, column=0)
        InputValueWidget(self,'Processos:').grid(row=2, column=0)
        SwitchWidgetForGpu(self).grid(row=3, column=0)
        
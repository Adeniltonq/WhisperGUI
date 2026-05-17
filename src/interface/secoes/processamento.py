import customtkinter
from secoes.generic import InputValueWidget, SwitchWidget
Frame = customtkinter.CTkFrame





class SwitchWidgetForGpu(Frame):
    def __init__(self, master,data):
        super().__init__(master)

        
        

        def set_gpu_state():
            
            if gpu_switch_widget.switch.get():
                data.disable_gpu['var'] = False
            else:
                data.disable_gpu['var'] = False
            print(gpu_switch_widget.switch.get())


        def set_number_int(event):
            text = event.widget.get()

            if  not text.isdigit() :
                print('ID de gpu invalido')
                event.widget.delete(0,'end')
                event.widget.insert(0,'')

            else: 
                data.gpu_device_id['var'].set(int(text))


            
            

        gpu_switch_widget = SwitchWidget(self,'GPU',command=set_gpu_state)
        gpu_switch_widget.grid(row=0,column=0,padx=(14,0))


        gpu_id_in_widget= InputValueWidget(self,"GPU_ID",label_width=20,entry_width=50,textvariable=data.gpu_device_id['var'])
        gpu_id_in_widget.grid(row=0,column=1,padx=(60,0))

        

        
       




class ProcesWidget(Frame):
    def __init__(self,master,data):
       
        super().__init__(master)

        threads = data.threads['var']
        processors = data.processors['var']
        
        
        
        titulo = customtkinter.CTkLabel(self,text='Processamento',height=30)
        titulo.grid(row=0,column=0,columnspan=2)


        InputValueWidget(self,'Nucleos:').grid(row=1, column=0)
        InputValueWidget(self,'Processos:').grid(row=2, column=0)
        switch_widget_for_gpu= SwitchWidgetForGpu(self,data)
        switch_widget_for_gpu.grid(row=3, column=0)

        
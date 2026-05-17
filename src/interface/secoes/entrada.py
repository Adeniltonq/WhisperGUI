import  customtkinter
from tkinter import StringVar

from secoes.generic import FilesPathWidget, InputValueWidget







class EntradaWidget(FilesPathWidget):
    def __init__(self,master,data):
        
        path_file_input= data.input_audio_file_path['var']
        lang_file_input= data.language['var']
        
        super().__init__(master,text='Caminho Midia',entry_width=700,on_top=True,textvariable=path_file_input)
    
        

        lg = InputValueWidget(self,text='Lingua Entrada',label_width=40,textvariable= lang_file_input)
        lg.grid(column=3,row=1,padx=(10))



        

       




        
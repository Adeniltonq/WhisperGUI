import customtkinter


from secoes.processamento import ProcesWidget
from secoes.time import TimeWidget
from secoes.text import TextWidget
from secoes.saida_format import SaidaFormatWidget
from secoes.generic import InputValueWidget
from secoes.model_conf import ModelConfWidget

from variaveis import PAD_WIDGETS_Y, PAD_WIDGETS_X

CTk = customtkinter.CTk


class MainWidget(CTk):

    def __init__(self):
        super().__init__()

       

        self.geometry("1200x600")
        
        InputValueWidget(self,'Caminho',on_top=True,entry_width=900).grid(row=1,column=0,columnspan=2,padx=(PAD_WIDGETS_X,0),pady=(10))


        ProcesWidget(self).grid(row=2,pady=(PAD_WIDGETS_Y),padx=(PAD_WIDGETS_X,0),sticky="nsew")
        TimeWidget(self).grid(row=3,pady=(PAD_WIDGETS_Y),padx=(PAD_WIDGETS_X,0),sticky="nsew")
        TextWidget(self).grid(row=4,pady=(PAD_WIDGETS_Y),padx=(PAD_WIDGETS_X,0),sticky="nsew")
        SaidaFormatWidget(self).grid(row=5,column=0,pady=(PAD_WIDGETS_Y),padx=(PAD_WIDGETS_X,0),sticky="nsew")

        ModelConfWidget(self).grid(column=1,row=2,padx=PAD_WIDGETS_X,columnspan=2,rowspan=4)

        

        
app = MainWidget()

app.mainloop()

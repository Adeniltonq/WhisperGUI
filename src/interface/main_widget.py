import customtkinter

from secoes.processamento import ProcesWidget
from secoes.time import TimeWidget
from secoes.text import TextWidget
from secoes.saida_format import SaidaFormatWidget

from variaveis import PAD_WIDGETS_Y

CTk = customtkinter.CTk


class MainWidget(CTk):

    def __init__(self):
        super().__init__()

       

        self.geometry("1200x500")
        
        
        ProcesWidget(self).grid(row=0,pady=(PAD_WIDGETS_Y),sticky="nsew")
        TimeWidget(self).grid(row=1,pady=(PAD_WIDGETS_Y),sticky="nsew")
        TextWidget(self).grid(row=2,pady=(PAD_WIDGETS_Y),sticky="nsew")
        SaidaFormatWidget(self).grid(row=3,column=0,pady=(PAD_WIDGETS_Y),sticky="nsew")


app = MainWidget()

app.mainloop()

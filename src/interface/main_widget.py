import customtkinter
 

from secoes.processamento import ProcesWidget
from secoes.time import TimeWidget
from secoes.text import TextWidget
from secoes.saida import SaidaFormatWidget
from secoes.model_conf import ModelConfWidget
from secoes.entrada import EntradaWidget
from secoes.vad import VadWidget
from secoes.terminal import TerminaltOutPutWidget

from Cli import CliWhisper


from variaveis import PAD_WIDGETS_Y, PAD_WIDGETS_X

CTk = customtkinter.CTk





class MainWidget(CTk):

    

    def __init__(self):
        super().__init__()

        cli = CliWhisper()

       

        self.geometry("1480x650")
        
        EntradaWidget(self,data=cli.conf_input).grid(row=1,column=0,columnspan=2,padx=(PAD_WIDGETS_X,0),pady=(10))


        ProcesWidget(self,data=cli.conf_process).grid(row=2,pady=(PAD_WIDGETS_Y),padx=(PAD_WIDGETS_X,0),sticky="nsew")
        
        TimeWidget(self).grid(row=3,pady=(PAD_WIDGETS_Y),padx=(PAD_WIDGETS_X,0),sticky="nsew")
        
        TextWidget(self).grid(row=4,pady=(PAD_WIDGETS_Y),padx=(PAD_WIDGETS_X,0),sticky="nsew")
        
        SaidaFormatWidget(self).grid(row=5,column=0,pady=(PAD_WIDGETS_Y),padx=(PAD_WIDGETS_X,0),sticky="nsew")


        ModelConfWidget(self).grid(column=1,row=2,padx=PAD_WIDGETS_X,columnspan=2,rowspan=4)

        VadWidget(self).grid(row=7,column=0,columnspan=3,padx=PAD_WIDGETS_X)

        TerminaltOutPutWidget(self).grid(row=2,column=3,padx=PAD_WIDGETS_X,rowspan=7)

        
app = MainWidget()

app.mainloop()

import customtkinter

from secoes.generic import InputValueWidget

Frame = customtkinter.CTkFrame


class TimeWidget(Frame):
    def __init__(self, master):
        super().__init__(master)

        

        titulo = customtkinter.CTkLabel(self,text='Tempo',height=30)
        titulo.grid(row=0,column=0,columnspan=2)


        inicio_widget = InputValueWidget(self,'Inicio')
        inicio_widget.grid(row=1)

        duracao_widget = InputValueWidget(self,'Duração')
        duracao_widget.grid(row=2)

        contexto_chunk_widget = InputValueWidget(self,'Contexto Chunk')
        contexto_chunk_widget.grid(row=3)
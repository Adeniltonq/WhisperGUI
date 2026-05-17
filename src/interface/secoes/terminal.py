from secoes.generic import TextAreaWidget
from customtkinter import CTkButton
import customtkinter

Frame = customtkinter.CTkFrame


class TerminaltOutPutWidget(Frame):
    def __init__(self, master):
        super().__init__(master)

        TextAreaWidget(self, text='Terminal', width=350, height=490, on_top=True).grid(row=0,column=0, columnspan=2,rowspan=6)

        iniciar_button  =  CTkButton(self,text='Iniciar')
        iniciar_button.grid(row=6,column=0,pady=(5))

        abortar_button  =  CTkButton(self,text='Abortar')
        abortar_button.grid(row=6,column=1,pady=(5))

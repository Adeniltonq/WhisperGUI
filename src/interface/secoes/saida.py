import customtkinter
import tkinter as Tk

from secoes.generic import SwitchWidget, DirPathWidget, InputValueWidget

Frame = customtkinter.CTkFrame


class SaidaFormatWidget(Frame):
    def __init__(self, master):
        super().__init__(master)

        TEXT_FORMAT = [
            ['TXT', 'VTT', 'SRT'],
            ['CSV', 'LRC', 'JSON'],
            ['JSON FULL']
            ]

        for row, lista in enumerate(TEXT_FORMAT):
            for col, texto in enumerate(lista):

                switch_widget = SwitchWidget(self, text=texto,command=None)

                switch_widget.grid(
                    row=row,
                    column=col,
                    padx=8,
                    pady=5

                )

        lg = InputValueWidget(self,text='Lingua Saida',label_width=40)
        lg.grid(column=1,row=2,columnspan=2)

        path_widget = DirPathWidget(self,text='PATH',label_width=40,entry_width=220)
        path_widget.grid(columnspan=4)


        

              


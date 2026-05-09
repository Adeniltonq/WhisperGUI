import customtkinter

from secoes.generic import SwitchWidget

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

                switch_widget = SwitchWidget(self, text=texto)

                switch_widget.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5

                )

                


import customtkinter

from secoes.processamento import ProcesWidget


CTk = customtkinter.CTk


class MainWidget(CTk):

    def __init__(self):
        super().__init__()

    

        self.geometry("1200x700")
        ProcesWidget(self).pack()


app = MainWidget()

app.mainloop()

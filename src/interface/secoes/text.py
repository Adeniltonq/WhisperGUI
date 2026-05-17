import customtkinter

from secoes.generic import InputValueWidget,SwitchWidget


Frame = customtkinter.CTkFrame


class TextWidget(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        tam_linha = InputValueWidget(self,text='Tamanho da Linha',entry_width=100,label_width=140)
        tam_linha.grid(columnspan= 3)

        switch_widget = SwitchWidget(self,text='Cortar Palavras',command= None)
        switch_widget.grid(column=0,padx=(15,40))

        num_split_words = customtkinter.CTkEntry(self,width=50)
        num_split_words.grid(row=1,column=1)



        






        

        
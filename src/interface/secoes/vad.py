import customtkinter

from secoes.generic import InputValueWidget, SliderWidget,SwitchWidget, FilePathWidget
from variaveis import PAD_WIDGETS_X, PAD_WIDGETS_Y

Frame = customtkinter.CTkFrame

styles = {
    'slider_width': 144
}

style_pad = {
    'padx':PAD_WIDGETS_X,
    'pady':PAD_WIDGETS_Y
}


class VadSelectWidget(Frame):
    def __init__(self, master):
        super().__init__(master,fg_color="transparent")

        vad_activate_widget = SwitchWidget(self,'VAD',command=None)
        vad_activate_widget.grid(row=0,padx=PAD_WIDGETS_X,pady=PAD_WIDGETS_Y)

        vad_model_path_widget = FilePathWidget(self,text='',entry_width=590)
        vad_model_path_widget.grid(row=0,column=1,padx=PAD_WIDGETS_X,pady=PAD_WIDGETS_Y)

        

    



class VadWidget(Frame):
    def __init__(self, master):
        super().__init__(master)


        
        vad_select_widget = VadSelectWidget(self)
        vad_select_widget.grid(row=0, columnspan=2,**style_pad)

        vad_threshold_widget = SliderWidget(self,text='Sensibilidade de Detecção',**styles)
        vad_threshold_widget.grid(row=0,column=2,**style_pad)

        vad_samples_overlap = SliderWidget(self,text='Sobreposição entre blocos',**styles)
        vad_samples_overlap.grid(row=1,column=0,**style_pad)
       
        vad_min_speech_duration_ms_widget = InputValueWidget(self,text='Duração Mínima da Fala')
        vad_min_speech_duration_ms_widget.grid(row=1,column=1,**style_pad)

        vad_min_silence_duration_ms= InputValueWidget(self,text='Duração mínima de silêncio')
        vad_min_silence_duration_ms.grid(row=1,column=2,**style_pad)

        vad_speech_pad_ms= InputValueWidget(self,text='Padding de Fala')
        vad_speech_pad_ms.grid(row=2,column=0,**style_pad)

        

       






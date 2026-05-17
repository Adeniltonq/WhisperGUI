import customtkinter

from secoes.generic import InputValueWidget, SwitchWidget,SliderWidget,TextAreaWidget
from variaveis import PAD_WIDGETS_X, PAD_WIDGETS_Y

Frame = customtkinter.CTkFrame

class ModelConfWidget(Frame):
    def __init__(self,master):
        super().__init__(master)

        inputs_style = {
            "entry_width":160,
            "label_width":180
        }



        input_widget_model = InputValueWidget(self,text='Modelo',entry_width=600,label_width=100)
        input_widget_model.grid(column=0,columnspan=2)


        input_widget_model = InputValueWidget(self,text='Best of',**inputs_style)
        input_widget_model.grid(column=0)

        input_widget_model_uncertainty = InputValueWidget(self,text='Incerteza do modelo',**inputs_style)
        input_widget_model_uncertainty.grid()

        input_widget_model_uncertainty = InputValueWidget(self,text='Max_context',**inputs_style)
        input_widget_model_uncertainty.grid()



        slider_widget_temp_inc = SliderWidget(self,'Temperatura\n de Incremento')
        slider_widget_temp_inc.grid(pady=(PAD_WIDGETS_Y))

        slider_widget_thresh = SliderWidget(self,'Threshold de \n confiança \n por palavra')
        slider_widget_thresh.grid(pady=(PAD_WIDGETS_Y))

        slider_widget_log_prob= SliderWidget(self,'Limite de \n log-probabilidade\n média')
        slider_widget_log_prob.grid(pady=(PAD_WIDGETS_Y))

        slider_widget_log_prob= SliderWidget(self,'Probabilidade de \n não existirfala \nem um segmento')
        slider_widget_log_prob.grid(pady=(PAD_WIDGETS_Y))


        switch_widget_diarazion = SwitchWidget(self,'Separar Falantes',command=None)
        switch_widget_diarazion.grid( sticky="w", pady=PAD_WIDGETS_Y)


        text_area_widget = TextAreaWidget(self,text='prompt')
        text_area_widget.grid(column=1,row=1,rowspan=8)
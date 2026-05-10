import customtkinter

from secoes.generic import InputValueWidget, SwitchWidget,SliderWidget
from variaveis import PAD_WIDGETS_X, PAD_WIDGETS_Y

Frame = customtkinter.CTkFrame

class ModelConfWidget(Frame):
    def __init__(self,master):
        super().__init__(master)

        inputs_style = {
            "entry_width":160,
            "label_width":180
        }



        input_widget_model = InputValueWidget(self,text='Modelo',**inputs_style)
        input_widget_model.grid(column=0)


        input_widget_model = InputValueWidget(self,text='Best of',**inputs_style)
        input_widget_model.grid(column=0)

        input_widget_model_uncertainty = InputValueWidget(self,text='Incerteza do modelo',**inputs_style)
        input_widget_model_uncertainty.grid()

        input_widget_model_uncertainty = InputValueWidget(self,text='Max_context',**inputs_style)
        input_widget_model_uncertainty.grid()


        slider_style =  {
            "slider_width":180,
            "label_width":120
            }

        slider_widget_temp_inc = SliderWidget(self,'Temperatura\n de Incremento',**slider_style)
        slider_widget_temp_inc.grid(pady=(PAD_WIDGETS_Y))

        slider_widget_thresh = SliderWidget(self,'Threshold de \n confiança \n por palavra',**slider_style)
        slider_widget_thresh.grid(pady=(PAD_WIDGETS_Y))

        slider_widget_log_prob= SliderWidget(self,'Limite de \n log-probabilidade\n média',**slider_style)
        slider_widget_log_prob.grid(pady=(PAD_WIDGETS_Y))

        slider_widget_log_prob= SliderWidget(self,'Probabilidade de \n não existirfala \nem um segmento',**slider_style)
        slider_widget_log_prob.grid(pady=(PAD_WIDGETS_Y))


        switch_widget_diarazion = SwitchWidget(self,'Separar Falantes')
        switch_widget_diarazion.grid(row=10, sticky="w", pady=PAD_WIDGETS_Y)


        prompt_title = customtkinter.CTkLabel(self,text="Prompt").grid(column=1,row=0)
        textbox_widget = customtkinter.CTkTextbox(self,width=300,height=390,fg_color='gray20')
        textbox_widget.grid(column=1,row=1,rowspan=10,padx=10)
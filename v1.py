###---------------------------------------- Assistente Virtual-----------------------------------
## Autor: Jhennifer Matias
## Data 17/01/2020
## Funcionalidades: funciona apenas para perguntas simples e claras

# ------------------------------------------------------- Code ------------------------------------------------------------------
import wolframalpha
import wikipedia
import PySimpleGUI as sg

layout = [  [sg.Txt('' * 10, background_color="#F0D9B5")],
            [sg.Text('Olá, eu sou a Cláudia como posso ajuda-la?',text_color= "black",font=('Helvetica', 15), background_color="#F0D9B5")],
            [sg.Input(size=(45,3)), sg.Button("Enviar", size= (10, 1),button_color=('black', 'orange'))],
            [sg.Text('', size=(40, 20), font=('Helvetica', 12), text_color= "black", key='input', background_color="#F0D9B5")],
            [sg.Txt('' * 10, background_color="#F0D9B5")],
          ]

# Set PySimpleGUI
form = sg.FlexForm('Claúdia assistente virtual', default_button_element_size=(5, 2),   size = (450, 600), background_color="#F0D9B5")
form.Layout(layout)

# Set Process
while True:
    button, value = form.Read()  # call GUI

    # Press Button
    if button is 'Enviar':
        if value[0] == 'Qual o seu nome?' or value[0] == 'qual o seu nome?' or value[0] == 'qual é o seu nome?' or value[0] == 'qual o seu nome?'or value[0] == 'Qual é o seu nome?':
            form.FindElement('input').Update("Claudia, fui criada por Jhennifer Matias")
      
        else:
            try:
                client = wolframalpha.Client("W4UHPT-6H53Q57EP5")
                res = client.query(value[0])
                pergunta = value[0]
                form.FindElement('input').Update(next(res.results).text)
            except:
                wikipedia.set_lang("pt")
                form.FindElement('input').Update(wikipedia.summary(value[0]))

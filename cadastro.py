import PySimpleGUI as sg

sg.theme('Reddit')

layout = [  [sg.Text('ensira o seu nome: '), sg.InputText(key='nome_do_usuario')],
            [sg.Text('ensira a sua idade: '), sg.InputText(key='idade_do_usuario')],
            [sg.Checkbox('salvar login?')],
            [sg.Button('entrar'), sg.Button('Cancelar')] ,
            [sg.Text('', key='resultado_da_formatação')]]


window = sg.Window('login', layout)

while True:
    evento, valores = window.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar': 
            break

    if evento == 'entrar':
        nome = valores['nome_do_usuario']
        idade = valores['idade_do_usuario']



        window['resultado_da_formatação'].update(f'seja bem-vindo {nome}, ao nosso site')

window.close()

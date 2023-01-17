import PySimpleGUI as sg

#create Layout
def create_task_manager():
    sg.theme('Reddit')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('task', layout=linha, key='contener')],
        [sg.Button('new task'), sg.Button('reset')]
    ]
    return sg.Window('task menager', layout=layout,finalize=True)
#create window
window = create_task_manager()
#window rules
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'new task':
        window.extend_layout(window['contener'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'reset':
        window.close()
        window = create_task_manager()

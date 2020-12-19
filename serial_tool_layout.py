import PySimpleGUI as sg


# Demo of how columns work
# window has on row 1 a vertical slider followed by a COLUMN with 7 rows
# Prior to the Column element, this layout was not possible
# Columns layouts look identical to window layouts, they are a list of lists of elements.

#window = sg.Window('Columns')                                   # blank window


#layout = [[sg.Slider(range=(1,100), default_value=10, orientation='h', size=(20,10)), sg.Column(col)],
#          [sg.In('Last input')],
#          [sg.OK()]]
r1 = [sg.Output(size=(100, 25), key = "display", background_color= "black", text_color= "green", font=('宋体',15))]
r2 = [sg.Checkbox("TS", tooltip = "if display the timestamp", key="ts", enable_events=True),
     sg.B("Clear")]
r3 = [sg.Button("Open", key = 'onoff'), sg.Combo([], size = (10, 5), key = "ports"), 
     sg.Text("Baud"), sg.Input(), sg.B("Set Filter"), sg.Input(key = "filter")]


layout = [r1, r2, r3] 



# Display the window and get values



if __name__ == '__main__':
    window = sg.Window('Test Layout', layout)
    event, values = window.read()
    while True: 
        event, values = window.read(timeout = 100) 
        if event == sg.WINDOW_CLOSED: 
          
            break
        elif event == sg.TIMEOUT_KEY:
            continue
        
        print(event, values)
    window.close()





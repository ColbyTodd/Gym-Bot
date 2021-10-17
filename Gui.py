#Colby Todd

import PySimpleGUI as sg

def gui():
    """
    () -> none

    Opens the user interface
    """
    layout = [[sg.Text("Choose an option")], [sg.Button("Login")],
              [sg.Button("Book a time")], [sg.Button("close")]]

    window = sg.Window("Gym Booker", layout)


    event, values = window.read()

    if event == "close":
       window.close()
        
    elif event == "Login":
        window.close()
        login_information()

    elif event == "Book a time":
        window.close()
        time()

def login_information():
    """
    () -> none

    checks if login information already exists and if user wants to change it
    """
    file = open("info.txt", "r")
    temp = file.read()
    file.close()

    layout = [[sg.T("Would you like to change your Username and Password?")],
                       [sg.B("Yes"), sg.B("No")]]
    
    

    if  "uname" and "pword" in temp:
        window = sg.Window("Login", layout)
        event, values = window.read()
        
        if event == "Yes":
            window.close()
            login()

        elif event == "No":
            window.close()
            gui()

def login():
    """
    () -> none

    Gets username and password from user and stores it into a file
    """
    layout = [[sg.T('Enter your Username'), sg.In(key='-ID-')],
                  [sg.T("Enter your Password "), sg.In(key='-Password-')],
                  [sg.B('OK'), sg.B('Cancel') ]]

    window = sg.Window("Login", layout)
    event, values = window.read()

    uname = values["-ID-"].strip()
    pword = values["-Password-"].strip()

    window.close()
    gui()
        
    file = open("info.txt", "w")
    
    temp = repr(uname)
    file.write("uname = " + temp + "\n")

    temp = repr(pword)
    file.write("pword = " + temp + "\n")

    file.close()

def time():
    """
    () -> none

    allows the user to choose what time they would like and stores it in a file
    """
    layout_day = [[sg.T("Choose a day")],
                          [sg.B("Monday"), sg.B("Tuesday"), sg.B("Wednesday"), sg.B("Thursday"), sg.B("Friday"),
                           sg.B("Saturday"), sg.B("Sunday")],
                          [sg.B("Close")]]

    window = sg.Window("Day", layout_day)
    event, value = window.read()

    if event == "Close":
        window.close()
        gui()

    elif event:
        file = open("schedule.txt", "w")
        temp = repr(event)
        file.write("Day = " + temp + "\n")

        window.close()

    
    
gui()








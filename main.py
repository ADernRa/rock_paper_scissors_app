from tkinter import *

main_win = Tk() 

def CreateWin(main_win):
    main_win.geometry("720x360")
    main_win.resizable(False, False)
    main_win.title("Game RPS")
    icon = PhotoImage(file = "icon.png")
    main_win.iconphoto(False, icon)
    main_win.config(bg="black")

CreateWin(main_win)

main_win.mainloop()
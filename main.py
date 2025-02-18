from tkinter import *

main_win = Tk() 

def ClearWin():
    for widget in main_win.winfo_children():
        widget.destroy()

def CreateWin():
    main_win.geometry("720x360")
    main_win.resizable(False, False)
    main_win.title("Game RPS")
    icon = PhotoImage(file = "icon.png")
    main_win.iconphoto(False, icon)
    main_win.config(bg="black")

def GamePlay():
    ClearWin()

def Info():
    ClearWin()

def Leave():
    ClearWin()
    
    def click_yes():
        main_win.destroy()

    def click_no():
        MainMenu()

    lbl_leave = Label(text="Вы уверены что хотите выйти", bg="black", fg = "lime", font=("Arial", 16))
    lbl_leave.place(anchor="c", y=120, x = 360)

    btn_yes = Button(text="Да", width=10, height=2, command=click_yes)
    btn_yes.place(anchor="c",y=160,x=300)
    
    btn_no = Button(text="Нет", width=10, height=2, command=click_no)
    btn_no.place(anchor="c",y=160,x=420)

def MainMenu():
    ClearWin()

    btn_start = Button(text="Начать", width=10, height=2, command=GamePlay)
    btn_start.place(anchor="c",y=120,x=360)

    btn_info = Button(text="Информация", width=10, height=2, command=Info)
    btn_info.place(anchor="c",y=180,x=360)

    btn_leave= Button(text="Выход", width=10, height=2, command=Leave)
    btn_leave.place(anchor="c",y=240,x=360)
    
CreateWin()
MainMenu()

main_win.mainloop()
from tkinter import *
import time
import random

main_win = Tk() 
score = 0
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

    def Win():
        ClearWin()
        lbl_win = Label(text="Вы победили\n+1", bg="black", fg = "lime", font=("Arial", 16))
        lbl_win.place(anchor="c", x=360, y = 130)

        btn_back = Button(text="Продолжить", width=10, height=2, command=GamePlay)
        btn_back.place(anchor="c", y=180, x = 360)

        global score
        score = int(score) + 1
    
    def Lose():
        ClearWin()
        global score

        btn_back = Button(text="Продолжить", width=10, height=2, command=GamePlay)
        btn_back.place(anchor="c", y=180, x = 360)
        
        lbl_win = Label(text=f"Вы проиграли\n-{score}", bg="black", fg = "lime", font=("Arial", 16))
        lbl_win.place(anchor="c", x=360, y = 130)
        score = 0

    def Draw():
        ClearWin()
        btn_back = Button(text="Продолжить", width=10, height=2, command=GamePlay)
        btn_back.place(anchor="c", y=180, x = 360)
        
        lbl_win = Label(text=f"Ничья", bg="black", fg = "lime", font=("Arial", 16))
        lbl_win.place(anchor="c", x=360, y = 130)

    def click_brick():
        bot_var = random.randint(0,2)
        if bot_var == 0:
            Draw()
        elif bot_var == 1:
            Win()
        elif bot_var == 2:
            Lose()
    
    def click_scissors():
        bot_var = random.randint(0,2)
        if bot_var == 0:
            Lose()
        elif bot_var == 1:
            Draw()
        elif bot_var == 2:
            Win()
    
    def click_paper():
        bot_var = random.randint(0,2)
        if bot_var == 0:
            Win()
        elif bot_var == 1:
            Lose()
        elif bot_var == 2:
            Draw()

    lbl_varian = Label(text="Выберите вариант", bg="black", fg = "lime", font=("Arial", 16))
    lbl_varian.place(anchor="c", y=40, x = 360)

    lbl_score = Label(text=f"Счет {score}", bg="black", fg = "lime", font=("Arial", 16))
    lbl_score.place(anchor="c", x=40, y = 20)

    btn_brick= Button(text="Камень", width=10, height=2, command=click_brick)
    btn_brick.place(anchor="c", y=180, x = 360)
    
    btn_scissors = Button(text="Ножницы", width=10, height=2, command=click_scissors)
    btn_scissors.place(anchor="c", y=180, x = 260)

    btn_paper= Button(text="Бумага", width=10, height=2, command=click_paper)
    btn_paper.place(anchor="c", y=180, x = 460)

    btn_ex= Button(text="✗", width=3, height=2, command= MainMenu)
    btn_ex.place(anchor="c", y=20, x = 700)

def Info():
    ClearWin()

    lbl_leave = Label(text="Правила игры\nКамень 🔪 Ножницы\nНожницы 🔪 Бумагу\nБумага 🔪 Камень\nПри поражении счет обнуляется", bg="black", fg = "lime", font=("Arial", 16))
    lbl_leave.place(anchor="c", y=90, x = 360)

    btn_menu = Button(text="В меню", width=10, height=2, command=MainMenu)
    btn_menu.place(anchor="c", y=200, x = 360)

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
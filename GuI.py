from tkinter import *

w = Tk() #윈도우창 객체 생성
w.title("Pythone Tkinter")      	    #윈도우 타이틀("제목")
w.geometry("200x200+500+300")     #윈도우 크기 및 기준점("너비x높이+x좌표+y좌표")
w.resizable(False, False)      	    #창 크기 조절 가능 여부(상하, 좌우)
def btn_call():
    instr=en.get()
    lb.config(text=instr,bg="green",fg="red")
    print(instr)

lb = Label(w, text="Welcome!",width=10,height=10,bg="blue")
lb.pack()
en = Entry()
en.pack()
bt = Button(w, text="확인")
bt.pack()
bt.config(command=btn_call)
lb.config(fg="red")

w.mainloop() #계속 돌면서 이벤트를 받고 있음





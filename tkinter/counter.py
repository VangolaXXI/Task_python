from tkinter import *

root = Tk()
root.title('Сумма чисел между')
root.geometry("500x200")
root.resizable(False, False)


def counter(action):
    global a
    a += action
    lab["text"] = str(a)
    if a > 0:
        lab.config(fg='dark Green')
    elif a < 0:
        lab.config(fg='#EF0801')
    else:
        lab.config(fg='black')
a = 0
Label(root, width=10, font='Roboto 16',text="Счетчик V 2.0",padx=20).place(relx=0.5, rely=0.2, anchor="center")

lab = Label(root, width=4, font='Roboto 16',text=str(a),padx=20)
lab.place(relx=0.5, rely=0.5, anchor="center")

but = Button(root, text='+',font='Roboto 16 bold', command=lambda:counter(1),bg='Green',padx=20)
but.place(relx=0.65, rely=0.5, anchor="center")

but1 = Button(root, text='-', font='Roboto 16  bold', command=lambda: counter(-1),bg='#EF0801',padx=20)
but1.place(relx=0.35, rely=0.5, anchor="center")

root.mainloop()

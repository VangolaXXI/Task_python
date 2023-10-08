from tkinter import *

root = Tk()
root.title('Сумма чисел между')
root.geometry("500x200")

def summa():
    a = EntryA.get()
    a = int(a)
    b = EntryB.get()
    b = int(b)
    sum_numbers = 0
    for i in range(a, b + 1):
        sum_numbers += i    
    lab['text'] = f'Сумма чисел от {a} до {b} равна {sum_numbers}'

Label(root, text='Первое число').grid(row=0, sticky=W)
Label(root, text='Второе число').grid(row=1, sticky=W)

EntryA = Entry(root, width=10, font='Arial 16')
EntryA.grid(row=0, column=1, sticky=E)


EntryB = Entry(root, width=10, font='Arial 16')
EntryB.grid(row=1, column=1, sticky=E)


lab = Label(root, width=30, font='Arial 16')
lab.grid(row=2, columnspan=2)

but = Button(root, text='Вычислить сумму', command=summa)
but.grid(row=3, column=0, columnspan=2)

root.mainloop()
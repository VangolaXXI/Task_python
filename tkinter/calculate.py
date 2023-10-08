from tkinter import *
root = Tk()
root.title('Произведение двух чисел')
def proizv(): # произведения
    a = EntryA.get() # берем текст из первого поля
    a = int(a) # преобразуем в число целого типа
    b = EntryB.get()
    b = int(b)
    result = str(a * b) # результат переведем в строку для дальнейшего вывода
    EntryC.delete(0, END) # очищаем текстовое поле полностью
    EntryC.insert(0, result) # вставляем результат в начало

def summa(): #Сумма
    a = EntryA.get() 
    a = int(a) 
    b = EntryB.get()
    b = int(b)
    result = str(a + b) 
    EntryC.delete(0, END) 
    EntryC.insert(0, result) 
def raz(): #разность
    a = EntryA.get() 
    a = int(a)
    b = EntryB.get()
    b = int(b)
    result = str(a - b) 
    EntryC.delete(0, END) 
    EntryC.insert(0, result)
def chas():#частность
    a = EntryA.get() 
    a = int(a) 
    b = EntryB.get()
    b = int(b)
    result = str(a / b) 
    EntryC.delete(0, END) 
    EntryC.insert(0, result) 
# первая метка в строке 0, столбце 0 (0 по умолчанию)
# парамет sticky  означает выравнивание. W, E,N,S — запад, восток, север, юг
Label(root, text='Первое число').grid(row=0, sticky=W)
# вторая метка в строке 1
Label(root, text='Второе число').grid(row=1, sticky=W)
# создаем виджеты текстовых полей
EntryA = Entry(root, width=10, font='Arial 16')
EntryB = Entry(root, width=10, font='Arial 16')
EntryC = Entry(root, width=20, font='Arial 16')
# размещаем первые два поля справа от меток, второй столбец (отсчет от нуля)
EntryA.grid(row=0, column=1, sticky=E)
EntryB.grid(row=1, column=1, sticky=E)
# третье текстовое поле ввода занимает всю ширину строки 2
# columnspan — объединение ячеек по столбцам; rowspan — по строкам
EntryC.grid(row=2, columnspan=2)
# размещаем кнопку в строке 3 во втором столбце
but = Button(root, text='*', command=proizv)
but.grid(row=3, column=1, sticky=E)

but = Button(root, text='+', command=summa)
but.grid(row=3, column=2, sticky=E)

but = Button(root, text='-', command=raz)
but.grid(row=3, column=3, sticky=E)

but = Button(root, text='/', command=chas)
but.grid(row=3, column=4, sticky=E)
root.mainloop()


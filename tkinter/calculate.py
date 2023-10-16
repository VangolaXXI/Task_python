from tkinter import *

root = Tk()
root.title('Произведение, сумма, разность и частное двух чисел')

def calculate(operation):
    try:
        a = float(EntryA.get())
        b = float(EntryB.get())
        if operation == '*':
            result = a * b
        elif operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '/':
            if b != 0:  # Проверка деления на ноль
                result = a / b
            else:
                result = "Деление на ноль невозможно"
        else:
            result = "Недопустимая операция"
        EntryC.delete(0, END)
        EntryC.insert(0, result)
    except ValueError:
        EntryC.delete(0, END)
        EntryC.insert(0, "Ошибка ввода")

Label(root, text='Первое число').grid(row=0, sticky=W)
Label(root, text='Второе число').grid(row=1, sticky=W)

EntryA = Entry(root, width=10, font='Arial 16')
EntryB = Entry(root, width=10, font='Arial 16')
EntryC = Entry(root, width=20, font='Arial 16')

EntryA.grid(row=0, column=1, sticky=E)
EntryB.grid(row=1, column=1, sticky=E)
EntryC.grid(row=2, columnspan=2)

operations = ['*', '+', '-', '/']
col = 1
for operation in operations:
    but = Button(root, text=operation, command=lambda op=operation: calculate(op))
    but.grid(row=3, column=col, sticky=E)
    col += 1

root.mainloop()


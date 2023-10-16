import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import StringVar
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Викторина по видеоиграм")
        self.score = 0
        self.point = 0
        self.current_question = 0
        
        root.geometry("400x450")# Размер окна 
        
         # Загрузка вопросов из файла
        self.questions = self.load_questions()
        self.question_label = tk.Label(root, text="", font=("Roboto", 15,"bold"),bg="#FDEB41")
        self.question_label.pack(pady=20)
        random.shuffle(self.questions)  # Перемешиваем вопросы

        self.option_radios = []
        self.selected_option = StringVar()
        self.selected_option.trace_add('write', self.on_option_selected)
        
         # Кнопка "Ответить"
        self.answer_button = ttk.Button(root, text="Ответить", command=self.check_answer, state="disabled",style="TButton",)
        self.answer_button.place(x=125, y=350)

        self.show_question()

    
    #Проверка на выбран ли какой вариант
    def on_option_selected(self, *args):
        if self.selected_option.get():
            self.answer_button["state"] = "active"
        else:
            self.answer_button["state"] = "disabled"


    #Загрузка вопросов и ответов из questions.txt 
    def load_questions(self, encoding='utf-8'):
        questions = []
        try:
            with open('questions.txt', 'r', encoding=encoding) as file:
                for line in file:
                    parts = line.strip().split('@')
                    if len(parts) == 6:
                        question_text, option1, option2, option3, option4, correct_answer = parts
                        question_text = question_text.replace("\\n", "\n")
                        questions.append({
                            'question': question_text,
                            'options': [option1, option2, option3, option4],
                            'correct_answer': int(correct_answer)
                        })
        except Exception as e:
            print("Ошибка при загрузке вопросов:", e)
        return questions

# Отображеня вопросов и вариантов ответов 
    def show_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data['question'])

            for i in range(4):
                if i < len(question_data['options']):
                    if i < len(self.option_radios):
                        self.option_radios[i].config(
                            text=question_data['options'][i],
                            value=i,
                            variable=self.selected_option,
                            state="normal"
                        )
                    else:
                        radio = ttk.Radiobutton(
                            self.root,
                            text=question_data['options'][i],
                            value=i,
                            variable=self.selected_option,
                            style="TRadiobutton",
                            padding=(10, 5),
                            width=15
                           
                        )
                        radio.place(x=90, y=150 + i * 50)  
                        self.option_radios.append(radio)
                else:
                    if i < len(self.option_radios):
                        self.option_radios[i].pack_forget()
        else:
            self.show_result()

    #Проверка правильность ответов 
    def check_answer(self):
        selected_option = self.selected_option.get()
        if int(selected_option) == self.questions[self.current_question]['correct_answer']:#Преоброзвание selected option в целое  число перед сравнением 
            self.score += 1
            self.point += 5
        self.current_question += 1
        self.selected_option.set("")  # Сброс выбранный ответ
        self.show_question()

    #Вывод ответов
    def show_result(self):
        if self.root:
            messagebox.showinfo(
                "Результат",
                f"Вы ответили правильно на {self.score} из {len(self.questions)} вопросов и получили {self.point} баллов"
            )
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    root.configure(bg="#FDEB41")
    style.configure("TRadiobutton", font=("Roboto", 14), background="#143642",foreground="#FDEB41",borderwidth=2, relief="solid")
    style.configure("TButton", font=("Roboto", 14,"bold"),background="#143642", padding=(10, 5), borderwidth=2, relief="solid")
    style.map("TRadiobutton", background=[("active", "white")],foreground=[("active", "#143642")])
    app = QuizApp(root)
    root.mainloop()

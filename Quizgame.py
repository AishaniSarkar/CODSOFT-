import tkinter as tk
from tkinter import messagebox
import random

quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Rome", "Berlin"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Earth", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.current_question_index = 0
        self.questions = random.sample(quiz_data, len(quiz_data))  

        self.create_widgets()

    def create_widgets(self):
        self.welcome_label = tk.Label(self.root, text="Welcome to the Quiz Game!\nAnswer the following questions:", font=("Helvetica", 16))
        self.welcome_label.pack(pady=20)

        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=10)

        self.var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.var, value="", font=("Helvetica", 12))
            rb.pack(anchor='w')
            self.option_buttons.append(rb)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, state=tk.DISABLED)
        self.submit_button.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack(pady=20)

    def start_quiz(self):
        self.score = 0
        self.current_question_index = 0
        self.start_button.pack_forget()
        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.questions):
            q = self.questions[self.current_question_index]
            self.question_label.config(text=q["question"])

            self.var.set(None)
            for i, option in enumerate(q["options"]):
                self.option_buttons[i].config(text=option, value=option)

            self.submit_button.config(state=tk.NORMAL)
        else:
            self.end_quiz()

    def check_answer(self):
        selected_option = self.var.get()
        correct_answer = self.questions[self.current_question_index]["answer"]

        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Incorrect! The correct answer was: {correct_answer}")

        self.current_question_index += 1
        self.load_question()

    def end_quiz(self):
        self.question_label.config(text=f"Quiz Over! Your score: {self.score}/{len(self.questions)}")
        self.submit_button.pack_forget()
        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again)
        self.play_again_button.pack(pady=20)

    def play_again(self):
        self.play_again_button.pack_forget()
        self.start_button.pack(pady=20)

root = tk.Tk()
root.geometry("500x500")
quiz_game = QuizGame(root)
root.mainloop()

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout, \
    QPushButton, QButtonGroup
from random import shuffle


class Question:
    def __init__(self, question, correct_answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.correct_answer = correct_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3


questions = [
    Question('Сколько планет в солнечной системе?', '8', '6', '7', '9'),
    Question('Какой самый крутой напиток?', 'Coca-Cola', 'Fanta', 'Sprite', 'Coffee'),
    Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Бразильский', 'Английский')
]
correct_count = 0
all_count = 0
question_num = 0
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.setFixedSize(400, 400)

question_label = QLabel('Вопрос')
layout_main = QVBoxLayout()
layout_sub1 = QHBoxLayout()
layout_sub2 = QHBoxLayout()
layout_sub3 = QHBoxLayout()
answer_button = QPushButton('Ответить')
radio_group_box = QGroupBox('Варианты ответов')

btn_answer1 = QRadioButton('answer')
btn_answer2 = QRadioButton('answer')
btn_answer3 = QRadioButton('answer')
btn_answer4 = QRadioButton('answer')
radio_group = QButtonGroup()
radio_group.addButton(btn_answer1)
radio_group.addButton(btn_answer2)
radio_group.addButton(btn_answer3)
radio_group.addButton(btn_answer4)
layout_quest = QVBoxLayout()
layout_h1_quest = QHBoxLayout()
layout_h2_quest = QHBoxLayout()
layout_h1_quest.addWidget(btn_answer1)
layout_h1_quest.addWidget(btn_answer2)
layout_h2_quest.addWidget(btn_answer3)
layout_h2_quest.addWidget(btn_answer4)
layout_quest.addLayout(layout_h1_quest)
layout_quest.addLayout(layout_h2_quest)
radio_group_box.setLayout(layout_quest)

answer_buttons = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]

layout_sub1.addWidget(question_label, alignment=Qt.AlignmentFlag.AlignCenter)
layout_sub2.addWidget(radio_group_box)
layout_sub3.addWidget(answer_button, alignment=Qt.AlignmentFlag.AlignHCenter)
layout_main.setSpacing(30)

result_group_box = QGroupBox('Результат теста')
next_button = QPushButton('Следующий вопрос')
layout_answer = QVBoxLayout()
true_or_false = QLabel('Правильно/Неправильно')
answer_label = QLabel('Правильный ответ')
layout_answer.addWidget(true_or_false)
layout_answer.addWidget(answer_label, alignment=Qt.AlignmentFlag.AlignHCenter)
result_group_box.setLayout(layout_answer)
layout_sub2.addWidget(result_group_box, alignment=Qt.AlignmentFlag.AlignCenter)
layout_sub3.addWidget(next_button)
layout_main.addLayout(layout_sub1)
layout_main.addLayout(layout_sub2)
layout_main.addLayout(layout_sub3)


def show_question(question):
    question_label.setText(question.question)
    shuffle(answer_buttons)
    answer_buttons[0].setText(question.correct_answer)
    answer_buttons[1].setText(question.wrong_answer1)
    answer_buttons[2].setText(question.wrong_answer2)
    answer_buttons[3].setText(question.wrong_answer3)
    answer_label.setText('Правильный ответ: ' + question.correct_answer)


def next_question():
    global question_num
    result_group_box.hide()
    next_button.hide()
    radio_group.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    radio_group.setExclusive(True)
    radio_group_box.show()
    answer_button.show()
    show_question(questions[question_num])
    question_num += 1
    if question_num == len(questions):
        question_num = 0
        shuffle(questions)


def answer():
    global correct_count
    global all_count
    if answer_buttons[0].isChecked():
        true_or_false.setText('Правильно')
        correct_count += 1
    else:
        true_or_false.setText('Неправильно')
    all_count += 1
    result = correct_count / all_count * 100
    print('Статистика', '\n'
          , 'Всего вопросов:', all_count, '\n'
          , 'Правильных вопросов:', correct_count, '\n'
          , 'Рейтинг:', result)
    radio_group_box.hide()
    answer_button.hide()
    result_group_box.show()
    next_button.show()


next_question()
main_win.setLayout(layout_main)

answer_button.clicked.connect(answer)
next_button.clicked.connect(next_question)

main_win.show()
app.exec()
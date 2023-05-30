# -*- coding: utf-8 -*-
import random
import sys
from PyQt5 import QtCore, QtWidgets, QtGui

def start_function():
    label.setText('Введи длину твоего пароля (просто число!):')
    start_btn.hide()
    btn_1.show()
    pass_length.show()

def btn_1_func():
    label.setText('Использовать буквы и спец. символы?')
    pass_length.hide()
    btn_1.hide()
    btn_2.show()
    btn_3.show()

def btn_2_func():
    btn_4.show()
    btn_2.hide()
    btn_3.hide()
    for i in range(int(pass_length.text())):
        rand = str(random.choice(yes))
        window.password += rand
    label.setText('Ваш пароль сгенерирован👇')
    pass_length.show()
    pass_length.setText(str(window.password))
    window.password = ''

def btn_3_func():
    btn_4.show()
    btn_2.hide()
    btn_3.hide()
    for i in range(int(pass_length.text())):
        rand = str(random.choice(no))
        window.password += rand
    label.setText('Ваш пароль сгенерирован👇')
    pass_length.show()
    pass_length.setText(str(window.password))
    window.password = ''

def btn_4_func():
    label.setText('Привет! Это приложение Генератор паролей.\n\nСдесь ты можешь сгенерировать пароль по выбранным тобой критериям😲')
    start_btn.show()
    pass_length.setText('')
    btn_4.hide()
    pass_length.hide()

app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setWindowTitle('Генератор паролей')
window.resize(700, 300)

window.password = ''

yes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '!', ':', ';', '@', '?', '$', '%', '^', '&', '*', ')', '(', '+', '-', '_', '=', '/', '|', '[', ']']
no = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

label = QtWidgets.QLabel('Привет! Это приложение Генератор паролей.\n\nСдесь ты можешь сгенерировать пароль по выбранным тобой критериям😲')
label.setFont(QtGui.QFont('Calibri', 14))

start_btn = QtWidgets.QPushButton('Начать!🐱‍💻')
start_btn.setFont(QtGui.QFont('Calibri', 12))

btn_1 = QtWidgets.QPushButton('Следующий шаг -->')
btn_1.setFont(QtGui.QFont('Calibri', 12))

btn_2 = QtWidgets.QPushButton('Да')
btn_2.setFont(QtGui.QFont('Calibri', 12))

btn_3 = QtWidgets.QPushButton('Нет')
btn_3.setFont(QtGui.QFont('Calibri', 12))

btn_4 = QtWidgets.QPushButton('Назад в меню😃')
btn_4.setFont(QtGui.QFont('Calibri', 12))

pass_length = QtWidgets.QLineEdit()
pass_length.setFont(QtGui.QFont('Calibri', 14))

boss = QtWidgets.QVBoxLayout()

line = QtWidgets.QVBoxLayout()
line.addWidget(label, alignment= QtCore.Qt.AlignHCenter)
line.addWidget(start_btn)
line.addWidget(pass_length)
line.addWidget(btn_1)

line_1 = QtWidgets.QHBoxLayout()
line_1.addWidget(btn_2)
line_1.addWidget(btn_3)
line_1.addWidget(btn_4)

btn_1.hide()
btn_2.hide()
btn_3.hide()
btn_4.hide()
pass_length.hide()

start_btn.clicked.connect(start_function)
btn_1.clicked.connect(btn_1_func)
btn_2.clicked.connect(btn_2_func)
btn_3.clicked.connect(btn_3_func)
btn_4.clicked.connect(btn_4_func)

boss.addLayout(line)
boss.addLayout(line_1)

window.setLayout(boss)
window.show()
sys.exit(app.exec_())
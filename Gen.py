from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from random import*
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Генератор")
main_window.resize(800, 500)

instruction_label = QLabel("Натисніть щоб обрати переможця!")
random_number = QLabel("?")
generate_button = QPushButton("Згенерувати")

def generate():
    instruction_label.setText("Переможець:")
    random_number.setText(str(randint(1, 100)))

generate_button.clicked.connect(generate)

main_loyaout = QVBoxLayout()
main_loyaout.addWidget(instruction_label)
main_loyaout.addWidget(random_number)
main_loyaout.addWidget(generate_button)

main_window.setLayout(main_loyaout)
main_window.show()
app.exec()

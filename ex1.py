import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLineEdit, QPushButton


class WordFlipper(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Перекидыватель cлов')
        self.resize(400, 100)

        layout = QHBoxLayout()

        self.input1 = QLineEdit(self)
        self.input1.setPlaceholderText("Введите текст...")
        self.input2 = QLineEdit(self)
        self.input2.setPlaceholderText("Сюда прилетит...")

        self.direction_to_right = True

        self.btn = QPushButton('->', self)
        self.btn.setStyleSheet("font-size: 16px; font-weight: bold; padding: 5px;")
        self.btn.clicked.connect(self.flip_words)

        layout.addWidget(self.input1)
        layout.addWidget(self.btn)
        layout.addWidget(self.input2)

        self.setLayout(layout)

    def flip_words(self):
        txt1 = self.input1.text()
        txt2 = self.input2.text()

        self.input1.setText(txt2)
        self.input2.setText(txt1)

        if self.direction_to_right:
            self.btn.setText('<-')
            self.direction_to_right = False
        else:
            self.btn.setText('->')
            self.direction_to_right = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordFlipper()
    ex.show()
    sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt


class SequentialCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Калькулятор')
        layout = QVBoxLayout()

        self.display = QLineEdit('0', self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setStyleSheet("font-size: 20px; padding: 5px;")
        layout.addWidget(self.display)

        grid = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0)
        ]

        for text, r, c in buttons:
            btn = QPushButton(text, self)
            btn.setFixedSize(50, 50)
            btn.clicked.connect(self.on_button_click)
            grid.addWidget(btn, r, c)

        layout.addLayout(grid)
        self.setLayout(layout)

    def on_button_click(self):
        button = self.sender()
        if not button:
            return

        text = button.text()
        current_text = self.display.text()

        if text == 'C':
            self.display.setText('0')
            return

        if current_text == '0' and text not in ['+', '-', '*', '/', '.']:
            current_text = ''

        if text == '=':
            try:
                if '/0' in current_text.replace(' ', ''):
                    self.display.setText("Ошибка: Деление на 0!")
                else:
                    res = eval(current_text)
                    self.display.setText(str(res))
            except Exception:
                self.display.setText("Ошибка!")
        else:
            if text in ['+', '-', '*', '/'] and current_text[-1:] in ['+', '-', '*', '/']:
                self.display.setText(current_text[:-1] + text)
            else:
                self.display.setText(current_text + text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SequentialCalculator()
    ex.show()
    sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Вычислитель')
        layout = QVBoxLayout()

        self.expr_input = QLineEdit(self)
        self.expr_input.setPlaceholderText("Введите выражение, например: 1 + 2 * 3")

        self.result_output = QLineEdit(self)
        self.result_output.setReadOnly(True)

        self.calc_btn = QPushButton('Вычислить', self)
        self.calc_btn.clicked.connect(self.evaluate_expr)

        layout.addWidget(self.expr_input)
        layout.addWidget(self.calc_btn)
        layout.addWidget(self.result_output)

        self.setLayout(layout)

    def evaluate_expr(self):
        self.expr_input.setStyleSheet("")
        try:
            expression = self.expr_input.text()
            res = eval(expression)
            self.result_output.setText(str(res))
        except Exception:
            self.result_output.setText("Ошибка выражения!")
            self.expr_input.setStyleSheet("border: 1px solid red;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Evaluator()
    ex.show()
    sys.exit(app.exec())

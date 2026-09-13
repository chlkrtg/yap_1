import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QSpinBox, QPushButton, \
    QPlainTextEdit
from PyQt6.QtCore import Qt


class RestaurantOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = {
            "Пицца Маргарита": 450,
            "Паста Карбонара": 380,
            "Салат Цезарь": 290,
            "Кофе Капучино": 150
        }
        self.items_controls = {}
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Заказ в ресторане')
        main_layout = QVBoxLayout()

        for dish, price in self.menu.items():
            row = QHBoxLayout()

            cb = QCheckBox(f"{dish} ({price} руб.)", self)
            spin = QSpinBox(self)
            spin.setRange(0, 10)
            spin.setEnabled(False)

            cb.stateChanged.connect(lambda state, s=spin: self.toggle_spin(state, s))

            row.addWidget(cb)
            row.addWidget(spin)
            main_layout.addLayout(row)

            self.items_controls[dish] = (cb, spin)

        self.receipt = QPlainTextEdit(self)
        self.receipt.setReadOnly(True)

        btn_pay = QPushButton('Сформировать чек', self)
        btn_pay.clicked.connect(self.generate_receipt)

        main_layout.addWidget(btn_pay)
        main_layout.addWidget(self.receipt)
        self.setLayout(main_layout)

    def toggle_spin(self, state, spin):
        if state == Qt.CheckState.Checked.value or state == Qt.CheckState.Checked:
            spin.setEnabled(True)
            if spin.value() == 0:
                spin.setValue(1)
        else:
            spin.setEnabled(False)
            spin.setValue(0)

    def generate_receipt(self):
        receipt_text = "====== Ваш чек ======\n"
        total_sum = 0

        for dish, (cb, spin) in self.items_controls.items():
            if cb.isChecked():
                count = spin.value()
                price = self.menu[dish]
                cost = price * count
                total_sum += cost
                receipt_text += f"{dish} x {count} = {cost} руб.\n"

        receipt_text += "=====================\n"

        if total_sum > 1000:
            discount = total_sum * 0.1
            total_sum -= discount
            receipt_text += f"Скидка 10%: {discount:.2f} руб.\n"

        receipt_text += f"ИТОГО К ОПЛАТЕ: {total_sum:.2f} руб."
        self.receipt.setPlainText(receipt_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RestaurantOrder()
    ex.show()
    sys.exit(app.exec())

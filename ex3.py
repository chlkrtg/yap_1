import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QCheckBox, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt


class CheckBoxManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Универсальный скрыватель')
        grid = QGridLayout()

        widgets = [
            QLabel("Я текстовая метка", self),
            QPushButton("Я кнопка-призрак", self),
            QLineEdit("Я поле ввода", self)
        ]

        for i, widget in enumerate(widgets):
            cb = QCheckBox(f"Показать виджет №{i + 1}", self)
            cb.setChecked(True)

            cb.setProperty("target_widget", widget)
            cb.stateChanged.connect(self.toggle_widget)

            grid.addWidget(cb, i, 0)
            grid.addWidget(widget, i, 1)

        self.setLayout(grid)

    def toggle_widget(self, state):
        sender = self.sender()
        if sender:
            widget = sender.property("target_widget")
            if widget:
                is_visible = (state == Qt.CheckState.Checked.value or state == Qt.CheckState.Checked)
                widget.setVisible(is_visible)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckBoxManager()
    ex.show()
    sys.exit(app.exec())

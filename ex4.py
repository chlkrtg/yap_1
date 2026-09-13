import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit


class MorseKeyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..'
        }
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Азбука Морзе')
        main_layout = QVBoxLayout()

        self.output = QLineEdit(self)
        self.output.setReadOnly(True)
        main_layout.addWidget(self.output)

        grid = QGridLayout()
        letters = list(self.morse_dict.keys())

        for i, letter in enumerate(letters):
            btn = QPushButton(letter, self)
            btn.clicked.connect(self.char_clicked)
            grid.addWidget(btn, i // 6, i % 6)

        clear_btn = QPushButton('Clear', self)
        clear_btn.clicked.connect(lambda: self.output.clear())
        grid.addWidget(clear_btn, 4, 4)

        space_btn = QPushButton('Space ( / )', self)
        space_btn.clicked.connect(lambda: self.output.setText(self.output.text() + " / "))
        grid.addWidget(space_btn, 4, 5)

        main_layout.addLayout(grid)
        self.setLayout(main_layout)

    def char_clicked(self):
        button = self.sender()
        if button:
            letter = button.text()
            morse_code = self.morse_dict[letter]
            self.output.setText(self.output.text() + morse_code + " ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MorseKeyboard()
    ex.show()
    sys.exit(app.exec())

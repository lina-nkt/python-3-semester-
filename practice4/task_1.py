import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QWidget,
    QVBoxLayout
)
from functools import partial

size_window = 350
size_display = 50
size_buttons = 50
mistake = "Ошибка"


class PatternWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор")
        self.setFixedSize(size_window, size_window)
        self.generalLayout = QVBoxLayout()
        widget = QWidget(self)
        widget.setLayout(self.generalLayout)
        self.setCentralWidget(widget)
        self.display()
        self.buttons()

    def display(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(size_display)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def buttons(self):
        self.dictButtons = {}
        buttons_pattern = QGridLayout()
        key = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="]
        ]
        for row, keys in enumerate(key):
            for col, key in enumerate(keys):
                self.dictButtons[key] = QPushButton(key)
                self.dictButtons[key].setFixedSize(size_buttons, size_buttons)
                buttons_pattern.addWidget(self.dictButtons[key], row, col)

        self.generalLayout.addLayout(buttons_pattern)

    def setTextDisplay(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def text(self):
        return self.display.text()

    def clearText(self):
        self.setTextDisplay("")



def errors(data):
    try:
        result = str(eval(data, {}, {}))
    except Exception:
        result = mistake
    return result


class CalculatorFunctions:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connectButtons()

    def calculatorResult(self):
        result = self.model(data=self.view.text())
        self.view.setTextDisplay(result)

    def functions(self, sub):
        if self.view.text() == mistake:
            self.view.clearText()
        expression = self.view.text() + sub
        self.view.setTextDisplay(expression)

    def connectButtons(self):
        for keySymbol, button in self.view.dictButtons.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self.functions, keySymbol)
                )
        self.view.dictButtons["="].clicked.connect(self.calculatorResult)
        self.view.display.returnPressed.connect(self.calculatorResult)
        self.view.dictButtons["C"].clicked.connect(self.view.clearText)


def main():
    appCalcuator = QApplication([])
    appCalculatorWindow = PatternWindow()
    appCalculatorWindow.show()
    CalculatorFunctions(model=errors, view=appCalculatorWindow)
    sys.exit(appCalcuator.exec())


if __name__ == "__main__":
    main()

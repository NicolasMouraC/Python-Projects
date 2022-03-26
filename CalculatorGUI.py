import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMainWindow, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from functools import partial

ERROR_MSG = 'ERROR'
app = QApplication(sys.argv)

def evaluateExpression(expression):
    try:
        result = str((eval(expression, {}, {})))
    except Exception:
        result = ERROR_MSG
    return result

class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(235, 235)
        self.centralWidget = QWidget(self)
        self.generalLayout = QVBoxLayout()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.generalLayout)
        self.createDisplay()
        self.createButtons()
    def createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
    def createButtons(self):
        buttonsLayout = QGridLayout()
        self.buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '-': (2, 3),
                   ')': (2, 4),
                   '0': (3, 0),
                   '00': (3, 1),
                   '.': (3, 2),
                   '+': (3, 3),
                   '=': (3, 4),}
        for btn, pos in self.buttons.items():
            self.buttons[btn] = QPushButton(btn)
            self.buttons[btn].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btn], pos[0], pos[1])
        self.generalLayout.addLayout(buttonsLayout)
    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()
    def displayText(self):
        return self.display.text()
    def clearDisplay(self):
        self.setDisplayText("")

class PyCalcCtrl:
    def __init__(self,model, view):
        self._view = view
        self._evaluate = model
        self._connectSignals()    
    def _buildExpression(self, sub_exp):
        """Build expression."""
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)
    def _calculatedResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)
    def _connectSignals(self):
        """Connect signals and slots."""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
        self._view.buttons["="].clicked.connect(self._calculatedResult)
        self._view.display.returnPressed.connect(self._calculatedResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
def main():
    pyCalc = QApplication(sys.argv)
    view = Calc()
    view.show()
    model = evaluateExpression
    PyCalcCtrl(model=model, view=view)
    sys.exit(pyCalc.exec_())

if __name__ == "__main__":
    main()
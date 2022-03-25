import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMainWindow, QVBoxLayout, QLineEdit

#Qlineedit, QcomboBox/QradioButton

app = QApplication(sys.argv)

class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(235, 235)
        self.centralWidget = QWidget(self)
        self.generalLayout = QVBoxLayout()
        self.setCentralWidget(self._centralWidget)
        self.centralWidget.setLayout(self.generalLayout)
        self.createDisplay()
        self.createButtons()
    def createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

def main():
    pyCalc = QApplication(sys.argv)
    view = Calc()
    view.show()
    sys.exit(pyCalc.exec_())

if __name__ == "__main__":
    main()

'''window = QWidget()
layout = QGridLayout()
layout.addWidget(QPushButton('1'), 0, 0)
layout.addWidget(QPushButton('2'), 0, 1)
layout.addWidget(QPushButton('3'), 0, 2)
layout.addWidget(QPushButton('4'), 1, 0)
layout.addWidget(QPushButton('5'), 1, 1)
layout.addWidget(QPushButton('6'), 1, 2)
layout.addWidget(QPushButton('7'), 2, 0)
layout.addWidget(QPushButton('8'), 2, 1)
layout.addWidget(QPushButton('9'), 2, 2)
layout.addWidget(QPushButton('0'), 3, 0, 3, 2)
layout.addWidget(QPushButton('-'), 0, 3)
layout.addWidget(QPushButton('*'), 1, 3)
layout.addWidget(QPushButton('+'), 2, 3)
layout.addWidget(QPushButton('='), 3, 3)


layout.addWidget(QLabel("<h1>Hello World!"),0, 1)
layout.addWidget(QLabel("<h1>Hello...<h1>"),1, 1)
layout.addWidget(QLabel("<h1>...World<h1>"),2, 1)
layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)


window.setLayout(layout)
window.setWindowTitle("Calculator")
window.setGeometry(150, 150, 300, 100)
window.move(600, 300)

window.show()

sys.exit(app.exec_())'''
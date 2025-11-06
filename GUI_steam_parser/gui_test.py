from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel,QLineEdit,
                             QVBoxLayout, QHBoxLayout, QWidget)
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parsteam")
        self.setFixedSize(500,500)


        self.program_label = QLabel("Software by Dargram")
        self.input = QLineEdit("")
        self.input.setFixedSize(300,30)
        self.input.setPlaceholderText("Enter game name...")


        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(v_layout)
        v_layout.setAlignment(Qt.AlignmentFlag.AlignTop)


        v_layout.addWidget(self.program_label, alignment=Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(self.input, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(container)
        

app = QApplication(sys.argv)

with open("style.qss", "r") as file:
    app.setStyleSheet(file.read())

window = MainWindow()
window.show()
app.exec()
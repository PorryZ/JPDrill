from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QHBoxLayout, QComboBox, QLineEdit
)
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("日语抽背训练器")
        self.resize(600, 400)

        self.layout = QVBoxLayout(self)

        self.mode_box = QComboBox()
        self.mode_box.addItems(["平假名", "片假名", "单词", "例句"])

        self.question_label = QLabel("请选择模式")
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setStyleSheet("font-size: 36px;")

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("可输入你的答案")

        self.answer_label = QLabel("")
        self.answer_label.setAlignment(Qt.AlignCenter)
        self.answer_label.setStyleSheet("font-size: 24px; color: green;")

        btn_layout = QHBoxLayout()
        self.btn_check = QPushButton("查看答案")
        self.btn_next = QPushButton("下一个")
        btn_layout.addWidget(self.btn_check)
        btn_layout.addWidget(self.btn_next)

        self.layout.addWidget(self.mode_box)
        self.layout.addWidget(self.question_label)
        self.layout.addWidget(self.input_box)
        self.layout.addWidget(self.answer_label)
        self.layout.addLayout(btn_layout)

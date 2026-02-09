from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QHBoxLayout, QComboBox, QFrame
)
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("日语抽背训练器")
        self.resize(600, 400)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(32, 24, 32, 24)
        self.layout.setSpacing(18)

        self.mode_box = QComboBox()
        self.mode_box.addItems(["平假名", "片假名", "单词", "例句"])
        self.mode_box.setCursor(Qt.PointingHandCursor)

        self.question_label = QLabel("请选择模式")
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setObjectName("questionLabel")

        self.answer_label = QLabel("")
        self.answer_label.setAlignment(Qt.AlignCenter)
        self.answer_label.setObjectName("answerLabel")

        self.answer_card = QFrame()
        self.answer_card.setObjectName("answerCard")
        answer_layout = QVBoxLayout(self.answer_card)
        answer_layout.setContentsMargins(16, 12, 16, 12)
        answer_layout.addWidget(self.answer_label)

        btn_layout = QHBoxLayout()
        self.btn_check = QPushButton("显示答案")
        self.btn_check.setCursor(Qt.PointingHandCursor)
        self.btn_next = QPushButton("下一个")
        self.btn_next.setCursor(Qt.PointingHandCursor)
        btn_layout.addWidget(self.btn_check)
        btn_layout.addWidget(self.btn_next)

        self.author_label = QLabel("作者：PorryZ")
        self.author_label.setAlignment(Qt.AlignRight)
        self.author_label.setObjectName("authorLabel")

        self.layout.addWidget(self.mode_box)
        self.layout.addWidget(self.question_label)
        self.layout.addWidget(self.answer_card)
        self.layout.addLayout(btn_layout)
        self.layout.addStretch()
        self.layout.addWidget(self.author_label)

        self.setStyleSheet(
            """
            QWidget {
                background-color: #f6f7fb;
                color: #1f2937;
                font-family: "Microsoft YaHei", "PingFang SC", sans-serif;
            }
            QComboBox {
                padding: 8px 12px;
                border-radius: 10px;
                background: white;
                border: 1px solid #e5e7eb;
                font-size: 15px;
            }
            QComboBox::drop-down {
                border: none;
            }
            #questionLabel {
                font-size: 64px;
                font-weight: 600;
                color: #111827;
                padding: 12px 0;
            }
            #answerCard {
                background: white;
                border-radius: 16px;
                border: 1px solid #e5e7eb;
            }
            #answerLabel {
                font-size: 26px;
                color: #10b981;
            }
            QPushButton {
                padding: 10px 22px;
                border-radius: 999px;
                background: #2563eb;
                color: white;
                font-size: 16px;
                font-weight: 600;
            }
            QPushButton:hover {
                background: #1d4ed8;
            }
            QPushButton:pressed {
                background: #1e40af;
            }
            #authorLabel {
                font-size: 12px;
                color: #9ca3af;
            }
            """
        )

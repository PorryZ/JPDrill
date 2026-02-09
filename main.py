import sys
from PySide6.QtWidgets import QApplication
from data_manager import DataManager
from trainer_logic import Trainer
from ui_main import MainWindow

MODE_FILE = {
    "平假名": "hiragana.json",
    "片假名": "katakana.json",
    "单词": "words.json",
    "例句": "sentences.json"
}

app = QApplication(sys.argv)

window = MainWindow()
dm = DataManager()

trainer = None

def load_mode():
    global trainer
    mode = window.mode_box.currentText()
    data = dm.load(MODE_FILE[mode])
    if not data:
        window.question_label.setText("暂无可背诵内容")
        window.answer_label.setText("")
        window.input_box.clear()
        trainer = None
        return
    trainer = Trainer(data)
    window.answer_label.setText("")
    window.input_box.clear()
    window.question_label.setText(trainer.next())

window.mode_box.currentIndexChanged.connect(load_mode)

def show_answer():
    if trainer is None:
        window.answer_label.setText("请先选择模式")
        return
    ok, ans = trainer.check(window.input_box.text())
    if ok:
        window.answer_label.setText(f"✔ 正确：{ans}")
    else:
        window.answer_label.setText(f"✘ 正确答案：{ans}")

def next_item():
    if trainer is None:
        window.answer_label.setText("请先选择模式")
        return
    window.answer_label.setText("")
    window.input_box.clear()
    window.question_label.setText(trainer.next())

window.btn_check.clicked.connect(show_answer)
window.btn_next.clicked.connect(next_item)

load_mode()
window.show()
sys.exit(app.exec())

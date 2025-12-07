import sys
import re
from collections import Counter

from PyQt6.QtWidgets import ( QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QPlainTextEdit)

class SeoAnalyzer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SEO анализ текста")
        self.resize(800, 600)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        main_layout.addWidget(QLabel("Введите текст для анализа:"))

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Введите текст сюда...")
        main_layout.addWidget(self.text_input, stretch=2)

        btn_layout = QHBoxLayout()
        main_layout.addLayout(btn_layout)

        self.analyze_button = QPushButton("Анализ")
        self.analyze_button.clicked.connect(self.run_analysis)
        btn_layout.addStretch()
        btn_layout.addWidget(self.analyze_button)
        btn_layout.addStretch()

        main_layout.addWidget(QLabel("Результат SEO-анализа:"))

        self.result_output = QPlainTextEdit()
        self.result_output.setReadOnly(True)
        main_layout.addWidget(self.result_output, stretch=3)

    def run_analysis(self):
        text = self.text_input.toPlainText()

        if not text.strip():
            self.result_output.setPlainText("Введите текст перед анализом")
            return

        chars_with_spaces = len(text)
        chars_without_spaces = len(text.replace(" ", ""))

        words = re.findall(r"\w+", text.lower(), flags=re.UNICODE)
        words_count = len(words)


        counter = Counter(words)
        most_common = counter.most_common(10)

        # Формируем строку с результатом
        lines = []
        lines.append("Статистика текста")
        lines.append(f"Количество символов (с пробелами): {chars_with_spaces}")
        lines.append(f"Количество символов (без пробелов): {chars_without_spaces}")
        lines.append(f"Количество слов: {words_count}")
        lines.append("")

        lines.append("топ-10 слов")
        for word, i in most_common:
            lines.append(f"слово - {word}; кол-во - {i}")

        self.result_output.setPlainText("\n".join(lines))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SeoAnalyzer()
    window.show()

    sys.exit(app.exec())

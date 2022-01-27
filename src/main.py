# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from widget import Widget

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

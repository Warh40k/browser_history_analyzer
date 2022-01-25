# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileSystemModel, QTreeView
from PySide6.QtCore import QFile, QDir
from PySide6.QtUiTools import QUiLoader

from form import Ui_Widget

class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()
        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())
        treeView = QTreeView()
        treeView.setModel(model)

    # Я так понимаю для загрузки элементов из ui файла
    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

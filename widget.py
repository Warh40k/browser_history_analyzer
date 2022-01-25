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
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())
        self.ui.treeView.setModel(model)

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

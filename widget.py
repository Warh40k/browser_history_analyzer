# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileSystemModel, QFileDialog
from PySide6.QtCore import QDir
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
        self.ui.pushButton.clicked.connect(self.submit_button)

    def submit_button(self):
        file = QFileDialog.getOpenFileName()
        print(file)
        #list = self.ui.treeView.selectedIndexes()
        #for i in list:
        #    print(i.data())
        #print(self.ui.treeView.indexAbove(list[0]).data())


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

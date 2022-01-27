# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Slot

from form import Ui_Widget


class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.showDialog)
        self.ui.pushButton_3.clicked.connect(sys.exit)

    @Slot()
    def showDialog(self):
        path = QFileDialog.getOpenFileName()[0]
        self.ui.lineEdit.setText(path)

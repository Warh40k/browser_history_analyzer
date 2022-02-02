# This Python file uses the following encoding: utf-8
import sys
import sqlite3

from datetime import datetime
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Slot

from form import Ui_Widget


class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText("/usr/firefox/comp/places.sqlite_")

        self.ui.select_button.clicked.connect(self.show_dialog)
        self.ui.exit_button.clicked.connect(sys.exit)
        self.ui.confirm_button.clicked.connect(self.get_history)

    @Slot()
    def get_history(self):
        path = self.ui.lineEdit.text()
        con = sqlite3.connect(path)
        cur = con.cursor()

        cur.execute("SELECT title, last_visit_date AS date FROM moz_places")
        for title, date in cur:
            if title is not None and date is not None:
                date = datetime.fromtimestamp(round(date/1000000))
                self.ui.listWidget.addItem("{0}, {1}".format(title, date))
        con.close()

    @Slot()
    def show_dialog(self):
        path = QFileDialog.getOpenFileName()[0]
        self.ui.lineEdit.setText(path)

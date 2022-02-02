# This Python file uses the following encoding: utf-8
import sys
import sqlite3

from datetime import datetime

from PySide6.QtWidgets import QWidget, QFileDialog, QTableWidgetItem, QHeaderView
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
        table_content = cur.fetchall()
        cur.close()
        data_length = len(table_content)
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(data_length)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Name", "Date"])
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        row_number = 0
        for title, raw_date in table_content:
            if title is not None and raw_date is not None:
                date = datetime.fromtimestamp(round(raw_date/1000000))
                title_item = QTableWidgetItem(title)
                date_item = QTableWidgetItem(str(date))
                self.ui.tableWidget.setItem(row_number, 0, title_item)
                self.ui.tableWidget.setItem(row_number, 1, date_item)
                row_number += 1


    @Slot()
    def show_dialog(self):
        path = QFileDialog.getOpenFileName()[0]
        self.ui.lineEdit.setText(path)

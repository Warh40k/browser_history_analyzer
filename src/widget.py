# This Python file uses the following encoding: utf-8
import sys
import sqlite3

from override_form import overrideTableWidget
from datetime import datetime

from PySide6.QtWidgets import QWidget, QFileDialog, QTableWidgetItem
from PySide6.QtCore import Slot, Qt

from form import Ui_Widget


class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        overrideTableWidget(self.ui)

        self.ui.select_button.clicked.connect(self.show_dialog)
        self.ui.exit_button.clicked.connect(sys.exit)
        self.ui.confirm_button.clicked.connect(self.get_history)
        self.ui.tableWidget.itemDoubleClicked.connect(self.open_url)

# Taking history from db and output to table widget
    @Slot()
    def get_history(self):
        path = self.ui.lineEdit.text()
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT title, last_visit_date, url AS date FROM moz_places "
                    "WHERE title IS NOT Null AND last_visit_date IS NOT NULL")
        table_content = cur.fetchall()
        cur.close()
        row_count = len(table_content)
        column_count = len(table_content[0])
        self.ui.tableWidget.setRowCount(row_count)
        self.ui.tableWidget.setColumnCount(column_count)
        self.ui.tableWidget.setColumnHidden(2, True)

        for row_number, (title, raw_date, site_url) in enumerate(table_content):
            date = datetime.fromtimestamp(round(raw_date/1000000))
            title_item = QTableWidgetItem(title)
            date_item = QTableWidgetItem(str(date))
            url_item = QTableWidgetItem(site_url)
            self.ui.tableWidget.setItem(row_number, 0, title_item)
            self.ui.tableWidget.setItem(row_number, 1, date_item)
            self.ui.tableWidget.setItem(row_number, 2, url_item)

        self.ui.tableWidget.sortItems(1, Qt.AscendingOrder)

    @Slot()
    def show_dialog(self):
        path = QFileDialog.getOpenFileName()[0]
        self.ui.lineEdit.setText(path)

    @Slot()
    def open_url(self):
        self.ui.tableWidget.currentItem()

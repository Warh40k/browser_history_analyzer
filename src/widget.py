# This Python file uses the following encoding: utf-8
import sys
import sqlite3
import matplotlib

matplotlib.use('Qt5Agg')

from override_form import overrideTableWidget
from datetime import datetime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from PySide6.QtWidgets import QWidget, QFileDialog, QTableWidgetItem, QMainWindow
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QDesktopServices

from form import Ui_Widget

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Widget(QWidget):

    def __init__(self):
        super(Widget, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        overrideTableWidget(self.ui)
        self.table_content = []
        self.dates_hour = []
        self.ui.select_button.clicked.connect(self.show_dialog)
        self.ui.exit_button.clicked.connect(sys.exit)
        self.ui.confirm_button.clicked.connect(self.get_history)
        self.ui.confirm_button.clicked.connect(self.report_history)
        self.ui.confirm_button.clicked.connect(self.most_visits_time)
        self.ui.tableWidget.itemDoubleClicked.connect(self.open_url)

# Taking history from db and output to table widget
    @Slot()
    def get_history(self):
        path = self.ui.lineEdit.text()
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute("SELECT p.title, p.last_visit_date, p.url, o.host FROM moz_places AS p "
                    "LEFT JOIN moz_origins AS o ON p.origin_id = o.id "
                    "WHERE p.title IS NOT NULL AND p.last_visit_date IS NOT NULL")

        self.table_content = cur.fetchall()
        cur.close()
        row_count = len(self.table_content)
        self.ui.tableWidget.setRowCount(row_count)
        self.ui.tableWidget.setColumnHidden(3, True)

        for row_number, (title, raw_date, site_url, site_host) in enumerate(self.table_content):
            # Convert date and save for next statistics
            date = datetime.fromtimestamp(round(raw_date/1000000))
            self.dates_hour.append(date.hour)

            # Insert data in QTable
            title_item = QTableWidgetItem(title)
            date_item = QTableWidgetItem(str(date))
            url_item = QTableWidgetItem(site_url)
            host_item = QTableWidgetItem(site_host)
            self.ui.tableWidget.setItem(row_number, 0, title_item)
            self.ui.tableWidget.setItem(row_number, 1, date_item)
            self.ui.tableWidget.setItem(row_number, 2, host_item)
            self.ui.tableWidget.setItem(row_number, 3, url_item)

        self.ui.tableWidget.sortItems(1, Qt.AscendingOrder)

    @Slot()
    def show_dialog(self):
        path = QFileDialog.getOpenFileName()[0]
        self.ui.lineEdit.setText(path)

    @Slot()
    def open_url(self):
        selected_row = self.ui.tableWidget.currentRow()
        selected_url = self.ui.tableWidget.item(selected_row, 3).text()
        QDesktopServices.openUrl(selected_url)

    def report_history(self):
        list_origins = []
        for i in self.table_content:
            list_origins.append(i[3])
        set_origins = set(list_origins)
        count_dict = {}
        for i in set_origins:
            count_dict[i] = list_origins.count(i)

        sorted_tuple = sorted(count_dict.items(), key=lambda x: x[1])
        sorted_tuple.reverse()
        for i in range(15):
            name_item = QTableWidgetItem(sorted_tuple[i][0])
            count_item = QTableWidgetItem(str(sorted_tuple[i][1]))
            self.ui.topsiteTable.setItem(i, 0, name_item)
            self.ui.topsiteTable.setItem(i, 1, count_item)

    def most_visits_time(self):
        for i in range(24):
            count = self.dates_hour.count(i)
            hour_item = QTableWidgetItem(str(i)+":00")
            count_item = QTableWidgetItem(str(count))
            self.ui.activityTable.setItem(i, 0, hour_item)
            self.ui.activityTable.setItem(i, 1, count_item)

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        self.ui.formLayout_2.addWidget(sc)

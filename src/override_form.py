from PySide6.QtWidgets import QAbstractItemView, QHeaderView


def overrideTableWidget(ui):
    ui.lineEdit.setText("/usr/firefox/comp/places.sqlite_")
    ui.tableWidget.setColumnCount(2)
    ui.tableWidget.setHorizontalHeaderLabels(["Name", "Date"])
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
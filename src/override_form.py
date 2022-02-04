from PySide6.QtWidgets import QAbstractItemView, QHeaderView


def overrideTableWidget(ui):
    ui.tableWidget.setColumnCount(4)
    ui.lineEdit.setText("/usr/firefox/comp/places.sqlite_")
    ui.tableWidget.setHorizontalHeaderLabels(["Name", "Visit_date", "Host", "URI"])
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

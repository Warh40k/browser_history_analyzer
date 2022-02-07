from PySide6.QtWidgets import QAbstractItemView, QHeaderView


def overrideTableWidget(ui):
    ui.tableWidget.setColumnCount(4)
    ui.lineEdit.setText("/usr/firefox/comp/places.sqlite_")
    ui.tableWidget.setHorizontalHeaderLabels(["Name", "Visit_date", "Host", "URI"])
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    ui.topsiteTable.setColumnCount(2)
    ui.topsiteTable.setRowCount(15)
    ui.topsiteTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.topsiteTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.topsiteTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    ui.topsiteTable.setHorizontalHeaderLabels(["Name", "Visits count"])

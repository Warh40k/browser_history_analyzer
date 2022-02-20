from PySide6.QtWidgets import QAbstractItemView, QHeaderView


def overrideTableWidget(ui):
    ui.tableWidget.setColumnCount(4)
    ui.lineEdit.setText("/home/nikita/docs/stuff/firefox_backup/places.sqlite")
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

    ui.activityTable.setColumnCount(2)
    ui.activityTable.setRowCount(24)
    ui.activityTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.activityTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    ui.activityTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
    ui.activityTable.setHorizontalHeaderLabels(["Hour", "Visits count"])
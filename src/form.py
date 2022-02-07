# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(871, 669)
        Widget.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(853, 112))
        font1 = QFont()
        font1.setPointSize(12)
        self.groupBox.setFont(font1)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, 5, -1)
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(200, 27))
        self.lineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.select_button = QPushButton(self.groupBox)
        self.select_button.setObjectName(u"select_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.select_button.sizePolicy().hasHeightForWidth())
        self.select_button.setSizePolicy(sizePolicy2)
        self.select_button.setMinimumSize(QSize(0, 27))
        self.select_button.setMaximumSize(QSize(100, 16777215))
        self.select_button.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout.addWidget(self.select_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.confirm_button = QPushButton(self.groupBox)
        self.confirm_button.setObjectName(u"confirm_button")
        sizePolicy.setHeightForWidth(self.confirm_button.sizePolicy().hasHeightForWidth())
        self.confirm_button.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.confirm_button, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(853, 450))
        self.tabWidget.setBaseSize(QSize(0, 0))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.topsiteTable = QTableWidget(self.tab_2)
        self.topsiteTable.setObjectName(u"topsiteTable")

        self.gridLayout.addWidget(self.topsiteTable, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.exit_button = QPushButton(Widget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMaximumSize(QSize(80, 27))
        self.exit_button.setFont(font1)

        self.verticalLayout.addWidget(self.exit_button, 0, Qt.AlignHCenter)

        QWidget.setTabOrder(self.lineEdit, self.select_button)
        QWidget.setTabOrder(self.select_button, self.confirm_button)
        QWidget.setTabOrder(self.confirm_button, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.exit_button)

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0438\u0441\u0442\u043e\u0440\u0438\u0438 firefox", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u043e\u0440 \u043f\u0440\u043e\u0444\u0438\u043b\u044f \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0430", None))
        self.select_button.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.confirm_button.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u043e\u0441\u0435\u0449\u0435\u043d\u0438\u0439", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u0422\u043e\u043f-10 \u043f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u044b\u0445 \u0441\u0430\u0439\u0442\u043e\u0432:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.exit_button.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi


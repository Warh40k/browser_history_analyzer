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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(871, 669)
        Widget.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
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

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 60))
        font1 = QFont()
        font1.setPointSize(12)
        self.groupBox.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, 5, -1)
        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(200, 27))
        self.lineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(0, 27))
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.groupBox)

        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(350, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.listView = QListView(Widget)
        self.listView.setObjectName(u"listView")
        self.listView.setMinimumSize(QSize(0, 400))

        self.verticalLayout.addWidget(self.listView)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(100, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.rowLayout = QFormLayout()
        self.rowLayout.setObjectName(u"rowLayout")
        self.rowLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.rowLayout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)
        self.rowLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.rowLayout.setLabelAlignment(Qt.AlignCenter)
        self.rowLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.rowLayout.setHorizontalSpacing(6)
        self.rowLayout.setContentsMargins(0, -1, -1, -1)
        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(150, 16777215))

        self.rowLayout.setWidget(0, QFormLayout.FieldRole, self.pushButton_3)


        self.verticalLayout_2.addLayout(self.rowLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0443\u0442\u044c \u043a \u0432\u0430\u0448\u0435\u043c\u0443 \u043f\u0440\u043e\u0444\u0438\u043b\u044e firefox", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u043e\u0440 \u043f\u0440\u043e\u0444\u0438\u043b\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi


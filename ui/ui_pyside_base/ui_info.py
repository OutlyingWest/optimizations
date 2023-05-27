# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_info.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_InfoWidget(object):
    def setupUi(self, InfoWidget):
        if not InfoWidget.objectName():
            InfoWidget.setObjectName(u"InfoWidget")
        InfoWidget.resize(408, 418)
        InfoWidget.setMinimumSize(QSize(300, 200))
        InfoWidget.setBaseSize(QSize(400, 400))
        self.verticalLayoutWidget = QWidget(InfoWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 19, 381, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)


        self.retranslateUi(InfoWidget)

        QMetaObject.connectSlotsByName(InfoWidget)
    # setupUi

    def retranslateUi(self, InfoWidget):
        InfoWidget.setWindowTitle(QCoreApplication.translate("InfoWidget", u"Info", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HoraireInputsTAIkf.ui'
##
## Created by: Qt User Interface Compiler version 6.10.3
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QSpinBox, QWidget)

class Ui_Horaire(object):
    def setupUi(self, Horaire):
        if not Horaire.objectName():
            Horaire.setObjectName(u"Horaire")
        Horaire.resize(512, 256)
        Horaire.setBaseSize(QSize(100, 100))
        Horaire.setSizeGripEnabled(False)
        self.buttonBox = QDialogButtonBox(Horaire)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 210, 461, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(Horaire)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 29, 110, 16))
        self.label_2 = QLabel(Horaire)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 55, 140, 16))
        self.label_3 = QLabel(Horaire)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 81, 285, 16))
        self.label_4 = QLabel(Horaire)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 107, 161, 16))
        self.label_5 = QLabel(Horaire)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 134, 131, 16))
        self.label_6 = QLabel(Horaire)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 160, 265, 16))
        self.spinBox_6 = QSpinBox(Horaire)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setGeometry(QRect(380, 159, 70, 19))
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setValue(2)
        self.spinBox = QSpinBox(Horaire)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(380, 27, 70, 19))
        self.spinBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.spinBox.setMinimum(1)
        self.spinBox.setValue(8)
        self.spinBox.setDisplayIntegerBase(10)
        self.spinBox_5 = QSpinBox(Horaire)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setGeometry(QRect(380, 132, 70, 20))
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setValue(2)
        self.spinBox_4 = QSpinBox(Horaire)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(380, 106, 70, 19))
        self.spinBox_4.setValue(2)
        self.spinBox_3 = QSpinBox(Horaire)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(380, 80, 70, 19))
        self.spinBox_3.setValue(4)
        self.spinBox_2 = QSpinBox(Horaire)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(380, 53, 70, 20))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setValue(11)

        self.retranslateUi(Horaire)
        self.buttonBox.accepted.connect(Horaire.accept)
        self.buttonBox.rejected.connect(Horaire.reject)

        QMetaObject.connectSlotsByName(Horaire)
    # setupUi

    def retranslateUi(self, Horaire):
        Horaire.setWindowTitle(QCoreApplication.translate("Horaire", u"Horaire", None))
        self.label.setText(QCoreApplication.translate("Horaire", u"Nombre de nuits : ", None))
        self.label_2.setText(QCoreApplication.translate("Horaire", u"Nombre d'animateurs : ", None))
        self.label_3.setText(QCoreApplication.translate("Horaire", u"Nombre d'animateurs qui ne font pas les nuits : ", None))
        self.label_4.setText(QCoreApplication.translate("Horaire", u"Nombre d'aides de camp : ", None))
        self.label_5.setText(QCoreApplication.translate("Horaire", u"Nombre de dortoirs  : ", None))
        self.label_6.setText(QCoreApplication.translate("Horaire", u"Nombre de dodos avant la premi\u00e8re nuit :   : ", None))
    # retranslateUi


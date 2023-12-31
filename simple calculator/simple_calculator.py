# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\toupa\Desktop\Projects\Python\Designer uis\simple calculator\simple calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcd_high_num = QtWidgets.QLCDNumber(Dialog)
        self.lcd_high_num.setSmallDecimalPoint(False)
        self.lcd_high_num.setDigitCount(20)
        self.lcd_high_num.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_high_num.setProperty("value", 0.0)
        self.lcd_high_num.setObjectName("lcd_high_num")
        self.verticalLayout.addWidget(self.lcd_high_num)
        self.label_sign = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sign.sizePolicy().hasHeightForWidth())
        self.label_sign.setSizePolicy(sizePolicy)
        self.label_sign.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_sign.setIndent(-5)
        self.label_sign.setObjectName("label_sign")
        self.verticalLayout.addWidget(self.label_sign)
        self.lcd_low_num = QtWidgets.QLCDNumber(Dialog)
        self.lcd_low_num.setDigitCount(20)
        self.lcd_low_num.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_low_num.setObjectName("lcd_low_num")
        self.verticalLayout.addWidget(self.lcd_low_num)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lcd_result = QtWidgets.QLCDNumber(Dialog)
        self.lcd_result.setDigitCount(20)
        self.lcd_result.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_result.setObjectName("lcd_result")
        self.horizontalLayout.addWidget(self.lcd_result)
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.butt_4 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_4.sizePolicy().hasHeightForWidth())
        self.butt_4.setSizePolicy(sizePolicy)
        self.butt_4.setObjectName("butt_4")
        self.gridLayout_3.addWidget(self.butt_4, 1, 0, 1, 1)
        self.butt_9 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_9.sizePolicy().hasHeightForWidth())
        self.butt_9.setSizePolicy(sizePolicy)
        self.butt_9.setObjectName("butt_9")
        self.gridLayout_3.addWidget(self.butt_9, 0, 2, 1, 1)
        self.butt_point = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_point.sizePolicy().hasHeightForWidth())
        self.butt_point.setSizePolicy(sizePolicy)
        self.butt_point.setObjectName("butt_point")
        self.gridLayout_3.addWidget(self.butt_point, 3, 2, 1, 1)
        self.butt_7 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_7.sizePolicy().hasHeightForWidth())
        self.butt_7.setSizePolicy(sizePolicy)
        self.butt_7.setObjectName("butt_7")
        self.gridLayout_3.addWidget(self.butt_7, 0, 0, 1, 1)
        self.butt_division = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_division.sizePolicy().hasHeightForWidth())
        self.butt_division.setSizePolicy(sizePolicy)
        self.butt_division.setObjectName("butt_division")
        self.gridLayout_3.addWidget(self.butt_division, 3, 0, 1, 1)
        self.butt_5 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_5.sizePolicy().hasHeightForWidth())
        self.butt_5.setSizePolicy(sizePolicy)
        self.butt_5.setObjectName("butt_5")
        self.gridLayout_3.addWidget(self.butt_5, 1, 1, 1, 1)
        self.butt_2 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_2.sizePolicy().hasHeightForWidth())
        self.butt_2.setSizePolicy(sizePolicy)
        self.butt_2.setObjectName("butt_2")
        self.gridLayout_3.addWidget(self.butt_2, 2, 1, 1, 1)
        self.butt_0 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_0.sizePolicy().hasHeightForWidth())
        self.butt_0.setSizePolicy(sizePolicy)
        self.butt_0.setObjectName("butt_0")
        self.gridLayout_3.addWidget(self.butt_0, 3, 1, 1, 1)
        self.butt_3 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_3.sizePolicy().hasHeightForWidth())
        self.butt_3.setSizePolicy(sizePolicy)
        self.butt_3.setObjectName("butt_3")
        self.gridLayout_3.addWidget(self.butt_3, 2, 2, 1, 1)
        self.butt_1 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_1.sizePolicy().hasHeightForWidth())
        self.butt_1.setSizePolicy(sizePolicy)
        self.butt_1.setObjectName("butt_1")
        self.gridLayout_3.addWidget(self.butt_1, 2, 0, 1, 1)
        self.butt_8 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_8.sizePolicy().hasHeightForWidth())
        self.butt_8.setSizePolicy(sizePolicy)
        self.butt_8.setObjectName("butt_8")
        self.gridLayout_3.addWidget(self.butt_8, 0, 1, 1, 1)
        self.butt_6 = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_6.sizePolicy().hasHeightForWidth())
        self.butt_6.setSizePolicy(sizePolicy)
        self.butt_6.setObjectName("butt_6")
        self.gridLayout_3.addWidget(self.butt_6, 1, 2, 1, 1)
        self.butt_plus = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_plus.sizePolicy().hasHeightForWidth())
        self.butt_plus.setSizePolicy(sizePolicy)
        self.butt_plus.setObjectName("butt_plus")
        self.gridLayout_3.addWidget(self.butt_plus, 3, 3, 1, 1)
        self.butt_minus = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_minus.sizePolicy().hasHeightForWidth())
        self.butt_minus.setSizePolicy(sizePolicy)
        self.butt_minus.setObjectName("butt_minus")
        self.gridLayout_3.addWidget(self.butt_minus, 2, 3, 1, 1)
        self.butt_multiple = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_multiple.sizePolicy().hasHeightForWidth())
        self.butt_multiple.setSizePolicy(sizePolicy)
        self.butt_multiple.setObjectName("butt_multiple")
        self.gridLayout_3.addWidget(self.butt_multiple, 1, 3, 1, 1)
        self.butt_equal = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_equal.sizePolicy().hasHeightForWidth())
        self.butt_equal.setSizePolicy(sizePolicy)
        self.butt_equal.setObjectName("butt_equal")
        self.gridLayout_3.addWidget(self.butt_equal, 0, 3, 1, 1)
        self.gridLayout_3.setRowMinimumHeight(0, 25)
        self.gridLayout_3.setRowMinimumHeight(1, 25)
        self.gridLayout_3.setRowMinimumHeight(2, 25)
        self.gridLayout_3.setRowMinimumHeight(3, 25)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_sign.setText(_translate("Dialog", "*"))
        self.label_2.setText(_translate("Dialog", "="))
        self.butt_4.setText(_translate("Dialog", "4"))
        self.butt_4.setShortcut(_translate("Dialog", "4"))
        self.butt_9.setText(_translate("Dialog", "9"))
        self.butt_9.setShortcut(_translate("Dialog", "9"))
        self.butt_point.setText(_translate("Dialog", "."))
        self.butt_point.setShortcut(_translate("Dialog", "."))
        self.butt_7.setText(_translate("Dialog", "7"))
        self.butt_7.setShortcut(_translate("Dialog", "7"))
        self.butt_division.setText(_translate("Dialog", "/"))
        self.butt_division.setShortcut(_translate("Dialog", "/"))
        self.butt_5.setText(_translate("Dialog", "5"))
        self.butt_5.setShortcut(_translate("Dialog", "5"))
        self.butt_2.setText(_translate("Dialog", "2"))
        self.butt_2.setShortcut(_translate("Dialog", "2"))
        self.butt_0.setText(_translate("Dialog", "0"))
        self.butt_0.setShortcut(_translate("Dialog", "0"))
        self.butt_3.setText(_translate("Dialog", "3"))
        self.butt_3.setShortcut(_translate("Dialog", "3"))
        self.butt_1.setText(_translate("Dialog", "1"))
        self.butt_1.setShortcut(_translate("Dialog", "1"))
        self.butt_8.setText(_translate("Dialog", "8"))
        self.butt_8.setShortcut(_translate("Dialog", "8"))
        self.butt_6.setText(_translate("Dialog", "6"))
        self.butt_6.setShortcut(_translate("Dialog", "6"))
        self.butt_plus.setText(_translate("Dialog", "+"))
        self.butt_plus.setShortcut(_translate("Dialog", "+"))
        self.butt_minus.setText(_translate("Dialog", "-"))
        self.butt_minus.setShortcut(_translate("Dialog", "-"))
        self.butt_multiple.setText(_translate("Dialog", "*"))
        self.butt_multiple.setShortcut(_translate("Dialog", "*"))
        self.butt_equal.setText(_translate("Dialog", "="))
        self.butt_equal.setShortcut(_translate("Dialog", "Return, ="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

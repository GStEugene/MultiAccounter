# Form implementation generated from reading ui file 'DialogChangeGame.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 188)
        self.exe_dir_line = QtWidgets.QLineEdit(Dialog)
        self.exe_dir_line.setGeometry(QtCore.QRect(30, 30, 341, 20))
        self.exe_dir_line.setObjectName("exe_dir_line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 10, 101, 16))
        self.label.setObjectName("label")
        self.set_exe_btn = QtWidgets.QPushButton(Dialog)
        self.set_exe_btn.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.set_exe_btn.setObjectName("set_exe_btn")
        self.set_dir_of_saves_btn = QtWidgets.QPushButton(Dialog)
        self.set_dir_of_saves_btn.setGeometry(QtCore.QRect(30, 140, 75, 23))
        self.set_dir_of_saves_btn.setObjectName("set_dir_of_saves_btn")
        self.dir_of_saves_line = QtWidgets.QLineEdit(Dialog)
        self.dir_of_saves_line.setGeometry(QtCore.QRect(30, 110, 341, 20))
        self.dir_of_saves_line.setObjectName("dir_of_saves_line")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 111, 16))
        self.label_2.setObjectName("label_2")
        self.DoneBtn = QtWidgets.QPushButton(Dialog)
        self.DoneBtn.setGeometry(QtCore.QRect(300, 140, 75, 23))
        self.DoneBtn.setObjectName("DoneBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Set game exe file:"))
        self.set_exe_btn.setText(_translate("Dialog", "Browse"))
        self.set_dir_of_saves_btn.setText(_translate("Dialog", "Browse"))
        self.label_2.setText(_translate("Dialog", "Set directory of saves:"))
        self.DoneBtn.setText(_translate("Dialog", "Done"))

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(334, 422)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setGeometry(QtCore.QRect(20, 310, 291, 41))
        self.play_btn.setObjectName("play_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.label.setObjectName("label")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(280, 70, 31, 31))
        self.add_btn.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.ActionsContextMenu)
        self.add_btn.setObjectName("add_btn")
        self.remove_btn = QtWidgets.QPushButton(self.centralwidget)
        self.remove_btn.setGeometry(QtCore.QRect(280, 100, 31, 31))
        self.remove_btn.setObjectName("remove_btn")
        self.lnk_btn = QtWidgets.QPushButton(self.centralwidget)
        self.lnk_btn.setGeometry(QtCore.QRect(20, 360, 291, 41))
        self.lnk_btn.setObjectName("lnk_btn")
        self.name_of_game = QtWidgets.QLabel(self.centralwidget)
        self.name_of_game.setGeometry(QtCore.QRect(20, 10, 121, 31))
        self.name_of_game.setObjectName("name_of_game")
        self.choose_of_game = QtWidgets.QPushButton(self.centralwidget)
        self.choose_of_game.setGeometry(QtCore.QRect(170, 10, 111, 31))
        self.choose_of_game.setObjectName("choose_of_game")
        self.list_of_players = QtWidgets.QListWidget(self.centralwidget)
        self.list_of_players.setGeometry(QtCore.QRect(20, 70, 256, 231))
        self.list_of_players.setProperty("isWrapping", False)
        self.list_of_players.setObjectName("list_of_players")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionadd_game = QtGui.QAction(MainWindow)
        self.actionadd_game.setObjectName("actionadd_game")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MultiAccounter"))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.label.setText(_translate("MainWindow", "Choose player:"))
        self.add_btn.setText(_translate("MainWindow", "+"))
        self.remove_btn.setText(_translate("MainWindow", "-"))
        self.lnk_btn.setText(_translate("MainWindow", "Create Links"))
        self.name_of_game.setText(_translate("MainWindow", "Curent game:\n"
"UnSet"))
        self.choose_of_game.setText(_translate("MainWindow", "Change the game"))
        self.actionadd_game.setText(_translate("MainWindow", "add game"))

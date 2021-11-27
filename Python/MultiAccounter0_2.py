import shutil, os, sys, time
from PyQt6 import QtWidgets, QtCore, QtGui
from tkinter import Tk
from tkinter.filedialog import askdirectory, askopenfilename
import main_window, dialog_add_player, dialog_change_game
try:
    import config
except:
    config_ = open('config.py', 'w+')
    import config

sys.argv += ['--noconsile']

def RefreshMainWindowValues(self):
    #self = getattr(self, '')
    try:
        self.dir_of_saves = config.directory_of_saves
        self.exe_dir = config.exe_dir
        self.accounts_directory = '/'.join(self.dir_of_saves.split('/')[:-1]) + '/MultiAccounter'
        self.name_of_game.setText('Curent game:\n' + self.exe_dir.split('/')[-1].split('.')[0])
        print(self.accounts_directory)
    except:
        self.dir_of_saves = ''
        self.exe_dir = ''
        self.accounts_directory = ''
        self.last_account = ''
    try:
        self.list_of_players_ = os.listdir(self.accounts_directory)
        self.list_of_players.clear()
        self.list_of_players.addItems(self.list_of_players_)
    except:
        ''''''
    try:
        self.last_account = config.last_account
        if self.last_account not in self.list_of_players_ and len(self.last_account) > 0:
            self.last_account = ''
    except:
        self.last_account = ''
    self.saves_last_account_dir = self.accounts_directory + '/' + self.last_account + '/' + \
                                  self.dir_of_saves.split('/')[-1]

class DialogChangeGame(QtWidgets.QDialog, dialog_change_game.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.exe_dir_line.setText(window.exe_dir)
        self.dir_of_saves_line.setText(window.dir_of_saves)
        self.set_exe_btn.pressed.connect(self.SetExeButon)
        self.set_dir_of_saves_btn.pressed.connect(self.SetSavesDirectory)
        self.DoneBtn.pressed.connect(self.Done)

    def SetExeButon(self):
        Tk().withdraw()
        self.exe_dir_line.setText(askopenfilename())

    def SetSavesDirectory(self):
        Tk().withdraw()
        self.dir_of_saves_line.setText(askdirectory())

    def Done(self):
        if os.path.exists(window.saves_last_account_dir) == False and len(window.last_account) > 0:
            shutil.copytree(window.dir_of_saves, window.saves_last_account_dir)
        with open('config.py', 'w') as ouf:
            ouf.write('directory_of_saves = "' + self.dir_of_saves_line.text() + '"\nexe_dir = "' + self.exe_dir_line.text() + '"\nlast_account = ""')
        config.last_account = ''
        config.exe_dir = self.exe_dir_line.text()
        config.directory_of_saves = self.dir_of_saves_line.text()
        RefreshMainWindowValues(window)
        if os.path.exists(window.accounts_directory) == False:
            os.mkdir(window.accounts_directory)
        QtWidgets.QDialog.close(self)

class DialogAddPlayer(QtWidgets.QDialog, dialog_add_player.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_player_name_btn.pressed.connect(self.DoneBtn)

    def DoneBtn(self):#Дон Батон (っ´Ι`)っ
        try:
            os.mkdir(window.accounts_directory + '/' + self.set_player_name_line.text())
            shutil.copytree(window.dir_of_saves, window.accounts_directory + '/' + self.set_player_name_line.text() + '/' + window.dir_of_saves.split('/')[-1])
            RefreshMainWindowValues(window)
            QtWidgets.QDialog.close(self)
        except:
            error = QtWidgets.QErrorMessage()
            error.showMessage("Username too short\n    or that username already used")
            error.setModal(True)
            error.exec()

class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.choose_of_game.pressed.connect(self.ChooseOfGame)
        self.add_btn.pressed.connect(self.AddPlayer)
        self.remove_btn.pressed.connect(self.RemovePlayer)
        self.play_btn.pressed.connect(self.Play)
        try:
            self.dir_of_saves = config.directory_of_saves
            self.exe_dir = config.exe_dir
            self.accounts_directory = '/'.join(self.dir_of_saves.split('/')[:-1]) + '/MultiAccounter'
            self.name_of_game.setText('Curent game:\n' + self.exe_dir.split('/')[-1].split('.')[0])
            print(self.accounts_directory)
        except:
            self.dir_of_saves = ''
            self.exe_dir = ''
            self.accounts_directory = ''
            self.last_account = ''
        try:
            self.list_of_players_ = os.listdir(self.accounts_directory)
            self.list_of_players.addItems(self.list_of_players_)
        except:
            ''''''
        try:
            self.last_account = config.last_account
            if self.last_account not in self.list_of_players_ and len(self.last_account) > 0:
                self.last_account = ''
        except:
            self.last_account = ''
        self.saves_last_account_dir = self.accounts_directory + '/' + self.last_account + '/' + self.dir_of_saves.split('/')[-1]


    def ChooseOfGame(self):
        self.dialog_change_game = DialogChangeGame()
        self.dialog_change_game.setModal(True)
        self.dialog_change_game.show()
        self.dialog_change_game.exec()

    def AddPlayer(self):
        self.dialog_add_player = DialogAddPlayer()
        #self.dialog_add_player.setModal(True)
        self.dialog_add_player.show()
        self.dialog_add_player.exec()

    def RemovePlayer(self):
        try:
            curent_item = self.list_of_players.item(self.list_of_players.currentRow()).text()
            item_to_remove = self.accounts_directory + '\\' + curent_item
            shutil.rmtree(item_to_remove)
            self.list_of_players.takeItem(self.list_of_players.currentRow())
            RefreshMainWindowValues(self)
        except:
            error = QtWidgets.QErrorMessage()
            error.showMessage('Not chosen account to remove')
            error.exec()

    def Play(self):
        try:
            curent_item = self.list_of_players.item(self.list_of_players.currentRow()).text()
            saves_curent_item_dir = self.accounts_directory + '/' + curent_item + '/' + self.dir_of_saves.split('/')[-1]
            print(curent_item)
            print(self.last_account)
            if self.last_account == curent_item and len(self.last_account) > 0:
                os.startfile(self.exe_dir)
            elif len(self.last_account) > 0:
                if os.path.exists(self.saves_last_account_dir) == False:
                    shutil.move(self.dir_of_saves, self.saves_last_account_dir)
                else:
                    shutil.rmtree(self.saves_last_account_dir)
                    shutil.move(self.dir_of_saves, self.saves_last_account_dir)
                shutil.move(saves_curent_item_dir, '/'.join(self.dir_of_saves.split('/')[:-1]))
                lines = ''
                with open('config.py') as inf:
                    for line in list(inf)[:-1]:
                        lines += line
                with open('config.py', 'w') as ouf:
                    ouf.write(lines + 'last_account = ' + '"' + curent_item + '"')
                os.startfile(self.exe_dir)
            else:
                shutil.rmtree(self.dir_of_saves)
                time.sleep(0.5)
                shutil.move(saves_curent_item_dir, '/'.join(self.dir_of_saves.split('/')[:-1]))
                lines = ''
                with open('config.py') as inf:
                    for line in list(inf)[:-1]:
                        lines += line
                with open('config.py', 'w') as ouf:
                    ouf.write(lines + 'last_account = ' + '"' + curent_item + '"')
                os.startfile(self.exe_dir)
            QtWidgets.QMainWindow.close(self)
        except:
            error = QtWidgets.QErrorMessage()
            error.showMessage('Not chosen account to play')
            error.exec()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
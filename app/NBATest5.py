# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NBATest.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os
import pickle
import pandas as pd
import sys
import cmd
import functions.predictWinPercentage as predictWinPercentage #import function
import functions.playerSwap as playerSwap

path = os.getcwd() #get working directory
player_data = pd.read_csv(path + '/data/player_data.csv') #get data
player_data_sr= pd.read_csv(path + '/data/player_data_single_record.csv')
season_average_data = pd.read_csv(path + '/data/season_average_data.csv', index_col=0)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_NBA(object):
    def setupUi(self, NBA):
        NBA.setObjectName("NBA")
        NBA.resize(962, 730)
        self.centralwidget = QtWidgets.QWidget(NBA)
        self.centralwidget.setObjectName("centralwidget")
        # Labels of 5 Players
        self.Name1 = QtWidgets.QLabel(self.centralwidget)
        self.Name1.setGeometry(QtCore.QRect(60, 90, 87, 16))
        self.Name1.setObjectName("Name1")
        self.Name2 = QtWidgets.QLabel(self.centralwidget)
        self.Name2.setGeometry(QtCore.QRect(60, 140, 87, 16))
        self.Name2.setObjectName("Name2")
        self.Name3 = QtWidgets.QLabel(self.centralwidget)
        self.Name3.setGeometry(QtCore.QRect(60, 190, 101, 16))
        self.Name3.setObjectName("Name3")
        self.Name4 = QtWidgets.QLabel(self.centralwidget)
        self.Name4.setGeometry(QtCore.QRect(60, 240, 87, 16))
        self.Name4.setObjectName("Name4")
        self.Name5 = QtWidgets.QLabel(self.centralwidget)
        self.Name5.setGeometry(QtCore.QRect(60, 290, 87, 16))
        self.Name5.setObjectName("Name5")
        self.Play = QtWidgets.QPushButton(self.centralwidget)
        self.Play.setGeometry(QtCore.QRect(590, 330, 111, 41))
        self.Play.setObjectName("Play")
        # Push button click event
        self.Play.clicked.connect(self.playbutton)
        #self.Play.clicked.connect(self.slidingbar)
        # Font Setting
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.Play.setFont(font)
        self.Play.setObjectName("Play")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(60, 400, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.text_win = QtWidgets.QTextEdit(self.centralwidget)
        self.text_win.setGeometry(QtCore.QRect(270, 450, 111, 31))
        self.text_win.setObjectName("text_win")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(290, 20, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        # Text input boxes of 5 players
        self.Enter1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Enter1.setGeometry(QtCore.QRect(180, 90, 201, 21))
        self.Enter1.setObjectName("Enter1")
        self.Enter2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Enter2.setGeometry(QtCore.QRect(180, 140, 201, 21))
        self.Enter2.setObjectName("Enter2")
        self.Enter3 = QtWidgets.QLineEdit(self.centralwidget)
        self.Enter3.setGeometry(QtCore.QRect(180, 190, 201, 21))
        self.Enter3.setObjectName("Enter3")
        self.Enter4 = QtWidgets.QLineEdit(self.centralwidget)
        self.Enter4.setGeometry(QtCore.QRect(180, 240, 201, 21))
        self.Enter4.setObjectName("Enter4")
        self.Enter5 = QtWidgets.QLineEdit(self.centralwidget)
        self.Enter5.setGeometry(QtCore.QRect(180, 290, 201, 21))
        self.Enter5.setObjectName("Enter5")
        self.label_win = QtWidgets.QLabel(self.centralwidget)
        self.label_win.setGeometry(QtCore.QRect(60, 450, 151, 20))
        # Font Setting
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_win.setFont(font)
        self.label_win.setObjectName("label_win")
        self.label_swap = QtWidgets.QLabel(self.centralwidget)
        self.label_swap.setGeometry(QtCore.QRect(60, 550, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_swap.setFont(font)
        self.label_swap.setObjectName("label_swap")
        self.text_swap = QtWidgets.QTextEdit(self.centralwidget)
        self.text_swap.setGeometry(QtCore.QRect(270, 550, 201, 31))
        self.text_swap.setObjectName("text_swap")
        self.error_message = QtWidgets.QLabel(self.centralwidget)
        self.error_message.setGeometry(QtCore.QRect(500, 450, 400, 150))
        self.error_message.setObjectName("error_message")
        self.label_salary = QtWidgets.QLabel(self.centralwidget)
        self.label_salary.setGeometry(QtCore.QRect(480, 140, 141, 20))
        self.label_salary.setObjectName("label_salary")
        self.Enter_season = QtWidgets.QLineEdit(self.centralwidget)
        self.Enter_season.setGeometry(QtCore.QRect(180, 340, 201, 21))
        self.Enter_season.setText("")
        self.Enter_season.setObjectName("Enter_season")
        self.Season = QtWidgets.QLabel(self.centralwidget)
        self.Season.setGeometry(QtCore.QRect(60, 340, 87, 16))
        self.Season.setObjectName("Season")
        self.checkBox_salary = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_salary.setGeometry(QtCore.QRect(740, 140, 87, 20))
        self.checkBox_salary.setObjectName("checkBox_salary")
        self.checkBox_strwk = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_strwk.setGeometry(QtCore.QRect(740, 190, 87, 20))
        self.checkBox_strwk.setObjectName("checkBox_strwk")
        self.label_strwk = QtWidgets.QLabel(self.centralwidget)
        self.label_strwk.setGeometry(QtCore.QRect(480, 190, 261, 20))
        self.label_strwk.setObjectName("label_strwk")
        self.label_plaerswap = QtWidgets.QLabel(self.centralwidget)
        self.label_plaerswap.setGeometry(QtCore.QRect(480, 240, 261, 20))
        self.label_plaerswap.setObjectName("label_plaerswap")
        self.checkBox_playerswap = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_playerswap.setGeometry(QtCore.QRect(740, 240, 87, 20))
        self.checkBox_playerswap.setObjectName("checkBox_playerswap")
        self.label_analysis = QtWidgets.QLabel(self.centralwidget)
        self.label_analysis.setGeometry(QtCore.QRect(60, 500, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_analysis.setFont(font)
        self.label_analysis.setObjectName("label_analysis")
        self.text_swap_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.text_swap_2.setGeometry(QtCore.QRect(270, 500, 201, 31))
        self.text_swap_2.setObjectName("text_swap_2")
        self.label_option = QtWidgets.QLabel(self.centralwidget)
        self.label_option.setGeometry(QtCore.QRect(480, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_option.setFont(font)
        self.label_option.setObjectName("label_option")
        NBA.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NBA)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 22))
        self.menubar.setObjectName("menubar")
        NBA.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NBA)
        self.statusbar.setObjectName("statusbar")
        NBA.setStatusBar(self.statusbar)

        self.retranslateUi(NBA)
        QtCore.QMetaObject.connectSlotsByName(NBA)

    def retranslateUi(self, NBA):
        _translate = QtCore.QCoreApplication.translate
        NBA.setWindowTitle(_translate("NBA", "MainWindow"))
        self.Name1.setText(_translate("NBA", "Player\'s Name"))
        self.Name2.setText(_translate("NBA", "Player\'s Name"))
        self.Name3.setText(_translate("NBA", "Player\'s Name"))
        self.Name4.setText(_translate("NBA", "Player\'s Name"))
        self.Name5.setText(_translate("NBA", "Player\'s Name"))
        self.Play.setText(_translate("NBA", "Play!"))
        self.label_result.setText(_translate("NBA", "Result:"))
        self.Title.setText(_translate("NBA", "NBA Make-A-Team"))
        self.label_win.setText(_translate("NBA", "Predicted Winning Percentage:"))
        self.label_swap.setText(_translate("NBA", "Recommended Player Swap:"))
        self.label_salary.setText(_translate("NBA", "Salary Cap On?"))
        self.Season.setText(_translate("NBA", "Season"))
        self.checkBox_salary.setText(_translate("NBA", "Yes"))
        self.checkBox_strwk.setText(_translate("NBA", "Yes"))
        self.label_strwk.setText(_translate("NBA", "Know team\'s strengths and weaknesses?"))
        self.label_plaerswap.setText(_translate("NBA", "Recommendation to swap player?"))
        self.checkBox_playerswap.setText(_translate("NBA", "Yes"))
        self.label_analysis.setText(_translate("NBA", "Team Performance Analysis:"))
        self.label_option.setText(_translate("NBA", "Options:"))
        self.error_message.setText(_translate("NBA", ""))

    # def errorMessage(self,NBA):
    #     QMessageBox.about(self, "Cannot open file",
    #                         "The selected file could not be opened.")
        # QMessageBox.warning(self, 'Error Message', 'You need 5 players to build a team!',QMessageBox.Cancel)
        # pass

    def playbutton(self, NBA):
            _translate = QtCore.QCoreApplication.translate
            textPlayer1 = self.Enter1.text()
            textPlayer2 = self.Enter2.text()
            textPlayer3 = self.Enter3.text()
            textPlayer4 = self.Enter4.text()
            textPlayer5 = self.Enter5.text()
            #Initiate text message
            self.error_message.setText(_translate("NBA", ""))
            self.text_win.setText(_translate("NBA", ""))
            self.text_swap_2.setText(_translate("NBA", ""))
            self.text_swap.setText(_translate("NBA", ""))
            #Variables and error
            season = int(self.Enter_season.text())
            player_list = (textPlayer1,textPlayer2,textPlayer3,textPlayer4,textPlayer5)
            season_data = player_data[player_data['season'] == season]
            pd_sr = player_data_sr[player_data_sr['season'] == season]
            sa_data = season_average_data[season_average_data['season'] == season]
            error = 0
            message = ("Error!\n")

            # Check for validity of season year
            if season <2000 or season >2017:
                self.error_message.setText(_translate("NBA", message + "Data of " + str(season) + " season is not available."))
                return None

            # Check for validity of player names
            for player in player_list:
                if season_data['player'].str.match(player, case=False).any():
                    message = message
                elif (not player) or (player.isspace() == True):
                    error = 1
                    break
                else:
                    message = (message + " " + player)
                    error = 2
            if error == 1:
                self.error_message.setText(_translate("NBA","Error!\n You need 5 players to build a team!"))
                return None
            elif error == 2:
                self.error_message.setText(_translate("NBA", message + "\n cannot be found in the dataset of the year."))
                return None

            # Get prediction
            else:
                prediction = predictWinPercentage.predictWinPercentage(player_data_sr, season_average_data, player_list,season)
                print(prediction)
                self.text_win.setText(_translate("NBA",prediction))

            if self.checkBox_salary.isChecked():
                salary_data = pd.read_csv(path + '/data/salaries_2017.csv')
                if season == 2017:
                    salary_result = playerSwap.salaryCap(player_list, salary_data, .8)
                    if salary_result['over_cap'] == True:
                        self.error_message.setText(_translate("NBA","The total salary of your team is " + str(salary_result['total_salary']) + "\nM. That is higher than 80 percent of the salary cap" + \
		                                                        "\nSo this team might be unrealistic... but this is just for fun!"))
                        self.text_win.setText(_translate("NBA", prediction))
                    else:
                        self.text_win.setText(_translate("NBA", prediction))
                        print(prediction)
                else:
                    self.error_message.setText(_translate("NBA","Sorry!\nWe have not set up the salary cap for this year yet."))
                    self.text_win.setText(_translate("NBA", prediction))

            if self.checkBox_strwk.isChecked():
                z_score = playerSwap.getZScores(player_list, pd_sr, sa_data)
                result = playerSwap.teamAssessment(z_score)
                print(result['weaknesses'])
                print(result['strengths'])
                self.text_swap_2.setText(_translate("NBA", result['weaknesses']+" and "+result['strengths']))

            if self.checkBox_playerswap.isChecked():
                potential_swaps = playerSwap.assessPlayerSwaps(player_list, pd_sr, sa_data)
                result = playerSwap.recommendPlayer(player_list, potential_swaps)
                print(result)
                self.text_swap.setText(_translate("NBA", result))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NBA = QtWidgets.QMainWindow()
    ui = Ui_NBA()
    ui.setupUi(NBA)
    NBA.show()
    sys.exit(app.exec_())


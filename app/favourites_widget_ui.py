# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'favourite-ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Favourites(object):
    def setupUi(self, Favourites):
        Favourites.setObjectName("Favourites")
        Favourites.resize(754, 553)
        Favourites.setStyleSheet("background-color: #e9e4d7")
        self.gridLayout = QtWidgets.QGridLayout(Favourites)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Favourites)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setStyleSheet("background-color: #ebaaa3;\n"
"border-radius: 5px;\n"
"padding-left: 10px;\n"
"padding-top: 10px;")
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Favourites)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.favourite_lyrics_combo_box = QtWidgets.QComboBox(Favourites)
        self.favourite_lyrics_combo_box.setStyleSheet("QComboBox {\n"
"    border: 2px solid #e6887c;\n"
"    border-radius: 3px;\n"
"    padding: 0px 5px 0px 5px;\n"
"    background-color: #d6ccb4;\n"
"    selection-color: #51a296;\n"
"}\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: 0px;\n"
"}")
        self.favourite_lyrics_combo_box.setObjectName("favourite_lyrics_combo_box")
        self.verticalLayout.addWidget(self.favourite_lyrics_combo_box)
        self.remove_button = QtWidgets.QPushButton(Favourites)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_button.sizePolicy().hasHeightForWidth())
        self.remove_button.setSizePolicy(sizePolicy)
        self.remove_button.setMinimumSize(QtCore.QSize(0, 20))
        self.remove_button.setMaximumSize(QtCore.QSize(16777215, 20))
        self.remove_button.setStyleSheet("QPushButton {\n"
"    background-color: #ba413f;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: #943432;\n"
"}    \n"
"")
        self.remove_button.setObjectName("remove_button")
        self.verticalLayout.addWidget(self.remove_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Favourites)
        QtCore.QMetaObject.connectSlotsByName(Favourites)

    def retranslateUi(self, Favourites):
        _translate = QtCore.QCoreApplication.translate
        Favourites.setWindowTitle(_translate("Favourites", "Form"))
        self.label.setText(_translate("Favourites", "Favourite lyrics"))
        self.remove_button.setText(_translate("Favourites", "Remove"))
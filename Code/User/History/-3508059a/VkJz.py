# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CSP.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


#START MY IMPORT
import Leonardo
import CSP_batch
import numpy
import os

Leonardo.check_license2.check()

#END MY IMPORT

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 842)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableUSER = QtWidgets.QTableWidget(self.tab)
        self.tableUSER.setMaximumSize(QtCore.QSize(605, 16777215))
        self.tableUSER.setObjectName("tableUSER")
        self.tableUSER.setColumnCount(6)
        self.tableUSER.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableUSER.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUSER.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUSER.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUSER.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUSER.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableUSER.setHorizontalHeaderItem(5, item)
        self.gridLayout_3.addWidget(self.tableUSER, 1, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineSegment = QtWidgets.QLineEdit(self.tab)
        self.lineSegment.setObjectName("lineSegment")
        self.horizontalLayout.addWidget(self.lineSegment)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.labelU = QtWidgets.QLabel(self.tab)
        self.labelU.setText("")
        self.labelU.setPixmap(QtGui.QPixmap("Images/UD.bmp"))
        self.labelU.setScaledContents(True)
        self.labelU.setObjectName("labelU")
        self.gridLayout_3.addWidget(self.labelU, 1, 3, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableT = QtWidgets.QTableWidget(self.tab_2)
        self.tableT.setMaximumSize(QtCore.QSize(605, 16777215))
        self.tableT.setObjectName("tableT")
        self.tableT.setColumnCount(2)
        self.tableT.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableT.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableT.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableT.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableT.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableT.setHorizontalHeaderItem(1, item)
        self.gridLayout_4.addWidget(self.tableT, 0, 0, 1, 1)
        self.labelT = QtWidgets.QLabel(self.tab_2)
        self.labelT.setText("")
        self.labelT.setPixmap(QtGui.QPixmap("Images/T_YES.bmp"))
        self.labelT.setScaledContents(True)
        self.labelT.setObjectName("labelT")
        self.gridLayout_4.addWidget(self.labelT, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableI = QtWidgets.QTableWidget(self.tab_3)
        self.tableI.setMaximumSize(QtCore.QSize(605, 16777215))
        self.tableI.setObjectName("tableI")
        self.tableI.setColumnCount(2)
        self.tableI.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableI.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableI.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableI.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableI.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableI.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableI.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableI.setHorizontalHeaderItem(1, item)
        self.gridLayout_5.addWidget(self.tableI, 0, 0, 1, 1)
        self.labelI = QtWidgets.QLabel(self.tab_3)
        self.labelI.setText("")
        self.labelI.setPixmap(QtGui.QPixmap("Images/I_YES.bmp"))
        self.labelI.setScaledContents(True)
        self.labelI.setObjectName("labelI")
        self.gridLayout_5.addWidget(self.labelI, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableC = QtWidgets.QTableWidget(self.tab_4)
        self.tableC.setMaximumSize(QtCore.QSize(605, 16777215))
        self.tableC.setObjectName("tableC")
        self.tableC.setColumnCount(2)
        self.tableC.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableC.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableC.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableC.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableC.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableC.setHorizontalHeaderItem(1, item)
        self.gridLayout_6.addWidget(self.tableC, 0, 0, 1, 1)
        self.labelC = QtWidgets.QLabel(self.tab_4)
        self.labelC.setText("")
        self.labelC.setPixmap(QtGui.QPixmap("Images/C_YES.bmp"))
        self.labelC.setScaledContents(True)
        self.labelC.setObjectName("labelC")
        self.gridLayout_6.addWidget(self.labelC, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tableL = QtWidgets.QTableWidget(self.tab_5)
        self.tableL.setMaximumSize(QtCore.QSize(605, 16777215))
        self.tableL.setObjectName("tableL")
        self.tableL.setColumnCount(2)
        self.tableL.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableL.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableL.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableL.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableL.setHorizontalHeaderItem(1, item)
        self.gridLayout_7.addWidget(self.tableL, 0, 0, 1, 1)
        self.labelL = QtWidgets.QLabel(self.tab_5)
        self.labelL.setText("")
        self.labelL.setPixmap(QtGui.QPixmap("Images/L_YES.bmp"))
        self.labelL.setScaledContents(True)
        self.labelL.setObjectName("labelL")
        self.gridLayout_7.addWidget(self.labelL, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.tab_6)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_h_string = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_h_string.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_h_string.setObjectName("lineEdit_h_string")
        self.horizontalLayout_5.addWidget(self.lineEdit_h_string)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)
        self.labelH = QtWidgets.QLabel(self.tab_6)
        self.labelH.setText("")
        self.labelH.setPixmap(QtGui.QPixmap("Images/H_YES.bmp"))
        self.labelH.setScaledContents(True)
        self.labelH.setObjectName("labelH")
        self.gridLayout_8.addWidget(self.labelH, 0, 2, 2, 1)
        self.tableH = QtWidgets.QTableWidget(self.tab_6)
        self.tableH.setMaximumSize(QtCore.QSize(605, 16777215))
        self.tableH.setObjectName("tableH")
        self.tableH.setColumnCount(2)
        self.tableH.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableH.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableH.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableH.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableH.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableH.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableH.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableH.setHorizontalHeaderItem(1, item)
        self.gridLayout_8.addWidget(self.tableH, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_7)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_7, "")
        self.gridLayout_2.addWidget(self.tabWidget, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(100, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboUnit = QtWidgets.QComboBox(self.centralwidget)
        self.comboUnit.setMinimumSize(QtCore.QSize(100, 0))
        self.comboUnit.setObjectName("comboUnit")
        self.comboUnit.addItem("")
        self.comboUnit.addItem("")
        self.horizontalLayout_3.addWidget(self.comboUnit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setMinimumSize(QtCore.QSize(100, 0))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.comboAnalysis = QtWidgets.QComboBox(self.centralwidget)
        self.comboAnalysis.setMinimumSize(QtCore.QSize(100, 0))
        self.comboAnalysis.setObjectName("comboAnalysis")
        self.comboAnalysis.addItem("")
        self.comboAnalysis.addItem("")
        self.horizontalLayout_2.addWidget(self.comboAnalysis)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMinimumSize(QtCore.QSize(100, 0))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_4.addWidget(self.label_11)
        self.comboEnv = QtWidgets.QComboBox(self.centralwidget)
        self.comboEnv.setMinimumSize(QtCore.QSize(100, 0))
        self.comboEnv.setObjectName("comboEnv")
        self.comboEnv.addItem("")
        self.comboEnv.addItem("")
        self.comboEnv.addItem("")
        self.horizontalLayout_4.addWidget(self.comboEnv)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 5, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuHelp = QtWidgets.QMenu(self.menu)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpenINI = QtWidgets.QAction(MainWindow)
        self.actionOpenINI.setObjectName("actionOpenINI")
        self.actionSaveINI = QtWidgets.QAction(MainWindow)
        self.actionSaveINI.setObjectName("actionSaveINI")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionF = QtWidgets.QAction(MainWindow)
        self.actionF.setObjectName("actionF")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpenINI)
        self.menuFile.addAction(self.actionSaveINI)
        self.menuFile.addAction(self.actionExit)
        self.menu.addAction(self.menuHelp.menuAction())
        self.menu.addAction(self.actionInfo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboEnv.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.MY_run) # type: ignore
        self.lineSegment.textChanged['QString'].connect(self.MY_Create_row) # type: ignore
        self.tableUSER.clicked['QModelIndex'].connect(self.MY_select_materisls) # type: ignore
        self.checkBox.released.connect(self.MYskin) # type: ignore
        self.tableC.pressed['QModelIndex'].connect(self.MY_select_materisls) # type: ignore
        self.tableUSER.pressed['QModelIndex'].connect(self.MY_select_materisls) # type: ignore
        self.tableT.pressed['QModelIndex'].connect(self.MY_select_materisls) # type: ignore
        self.tableI.clicked['QModelIndex'].connect(self.MY_select_materisls) # type: ignore
        self.tableL.pressed['QModelIndex'].connect(self.MY_select_materisls) # type: ignore
        self.tableH.pressed['QModelIndex'].connect(self.MY_select_materisls) # type: ignore
        self.actionExit.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
        # START MY INIT

        if 'app' in globals(): Leonardo.LeonardoStyle.dark(app)
        self.GUIDIR = Leonardo.LeonardoGUI.Standard(self, os.path.abspath (__file__) , MainWindow )

        #self.actionNew.triggered.connect( self.MY_New)
        self.actionOpenINI.triggered.connect( self.MY_OpenINI2)
        self.actionSaveINI.triggered.connect( self.MY_SaveINI)
        self.actionInfo.triggered.connect( self.MY_info)
        
            
        
        # END MY INIT    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "C.S.P. - Composite Section Properties"))
        item = self.tableUSER.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Length L"))
        item = self.tableUSER.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "X Coord"))
        item = self.tableUSER.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Y Coord"))
        item = self.tableUSER.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "laminate"))
        item = self.tableUSER.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "OEF/NEF"))
        item = self.tableUSER.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Angle"))
        self.label.setText(_translate("MainWindow", "n of Segments"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "USER DEFINED"))
        item = self.tableT.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Length L"))
        item = self.tableT.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "laminate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "T"))
        item = self.tableI.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Length L"))
        item = self.tableI.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "laminate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "I"))
        item = self.tableC.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Length L"))
        item = self.tableC.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "laminate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "C"))
        item = self.tableL.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Length L"))
        item = self.tableL.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "laminate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "L"))
        self.label_3.setText(_translate("MainWindow", "h_stringer"))
        item = self.tableH.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Length L"))
        item = self.tableH.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "laminate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "HAT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Results"))
        self.label_4.setText(_translate("MainWindow", "Unit system"))
        self.comboUnit.setItemText(0, _translate("MainWindow", "lb - in"))
        self.comboUnit.setItemText(1, _translate("MainWindow", "N - mm"))
        self.label_10.setText(_translate("MainWindow", "Type Analysis"))
        self.comboAnalysis.setItemText(0, _translate("MainWindow", "TEST"))
        self.comboAnalysis.setItemText(1, _translate("MainWindow", "Design"))
        self.label_11.setText(_translate("MainWindow", "Enviroment"))
        self.comboEnv.setItemText(0, _translate("MainWindow", "RT"))
        self.comboEnv.setItemText(1, _translate("MainWindow", "COLD"))
        self.comboEnv.setItemText(2, _translate("MainWindow", "HOT/WET"))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.checkBox.setText(_translate("MainWindow", "SKIN"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu.setTitle(_translate("MainWindow", "?"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpenINI.setText(_translate("MainWindow", "OpenINI"))
        self.actionSaveINI.setText(_translate("MainWindow", "SaveINI"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionF.setText(_translate("MainWindow", "f"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


    
    # START MY CODE    
    from Leonardo.LeonardoGUI import MY_New,MY_OpenINI,MY_SaveINI,MY_info
    
    def check_gui(self):

        if self.checkBox.isChecked():
            #print(1)
            self.labelT.setPixmap(QtGui.QPixmap(str('images\\T_YES.bmp')))
            self.labelI.setPixmap(QtGui.QPixmap(str('images\\I_YES.bmp')))
            self.labelC.setPixmap(QtGui.QPixmap(str('images\\C_YES.bmp')))
            self.labelL.setPixmap(QtGui.QPixmap(str('images\\L_YES.bmp')))
            self.labelH.setPixmap(QtGui.QPixmap(str('images\\H_YES.bmp')))
            
        else:
            #print(2)
            self.labelT.setPixmap(QtGui.QPixmap(str('images\\T_NO.bmp')))
            self.labelI.setPixmap(QtGui.QPixmap(str('images\\I_NO.bmp')))
            self.labelC.setPixmap(QtGui.QPixmap(str('images\\C_NO.bmp')))
            self.labelL.setPixmap(QtGui.QPixmap(str('images\\L_NO.bmp')))
            self.labelH.setPixmap(QtGui.QPixmap(str('images\\H_NO.bmp')))
            
        
            
    def MY_OpenINI2(self): 
        # noinspection PyArgumentList
        self.MY_OpenINI()
        self.check_gui()       
            
    def MY_Create_row(self):

        numberRow=int(self.lineSegment.text())

        self.tableUSER.setRowCount(numberRow)
        for i in range(numberRow):
            item = QtWidgets.QTableWidgetItem()
            self.tableUSER.setVerticalHeaderItem(i,item)



    def MYskin(self):
        self.check_gui()
        if self.checkBox.isChecked():
            item = QtWidgets.QTableWidgetItem()
            

            R=self.tableUSER.rowCount()
            self.tableUSER.setRowCount(R+1)
            self.tableUSER.setVerticalHeaderItem(R,item)
            
            R=self.tableT.rowCount()
            self.tableT.setRowCount(R+1)
            self.tableT.setVerticalHeaderItem(R,item)
            
            R=self.tableI.rowCount()
            self.tableI.setRowCount(R+1)
            self.tableI.setVerticalHeaderItem(R,item)
            
            R=self.tableC.rowCount()
            self.tableC.setRowCount(R+1)
            self.tableC.setVerticalHeaderItem(R,item)
            
            R=self.tableL.rowCount()
            self.tableL.setRowCount(R+1)
            self.tableL.setVerticalHeaderItem(R,item)

            R=self.tableH.rowCount()
            self.tableH.setRowCount(R+1)
            self.tableH.setVerticalHeaderItem(R,item)
        else:
            R=self.tableUSER.rowCount()
            self.tableUSER.removeRow(R-1)

            R=self.tableT.rowCount()
            if R>3:
                self.tableT.removeRow(R-1)

            R=self.tableI.rowCount()
            if R>5:
                self.tableI.removeRow(R-1)
                
            R=self.tableC.rowCount()
            if R>3:
                self.tableC.removeRow(R-1)
                
            R=self.tableL.rowCount()
            if R>2:
                self.tableL.removeRow(R-1)
                
            R=self.tableH.rowCount()
            if R>5:
                self.tableH.removeRow(R-1)
######################################################################################

    def MY_select_materisls(self):
        tab=self.tabWidget.currentIndex()
        if tab==0:
            table=self.tableUSER
        elif tab==1:
            table=self.tableT
        elif tab==2:
            table=self.tableI
        elif tab==3:
            table=self.tableC
        elif tab==4:
            table=self.tableL
        elif tab==5:
            table=self.tableH

        # noinspection PyUnboundLocalVariable
        ic =table.currentColumn()
        ir =table.currentRow()
        if ic == 1 and tab!=0:
            filename,_ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open ".laminate" File', '','*.laminate')
            
            if not filename:                
                return
            item=QtWidgets.QTableWidgetItem(Leonardo.LeonardoStyle.scrivi_path(filename))
            table.setItem(ir,ic,item)
        if ic == 3 and tab==0:
            filename,_ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open ".laminate" File', '','*.laminate')
            
            if not filename:                
                return
            item=QtWidgets.QTableWidgetItem(Leonardo.LeonardoStyle.scrivi_path(filename))
            table.setItem(ir,ic,item)


    def MY_run(self):
        

        temp1="test.tmp"
        Leonardo.LeonardoStyle.SALVA(self, QtCore.QSettings(temp1,QtCore.QSettings.IniFormat))
        
        tx,x_C,y_CG,EI_x_CG,EI_y_CG,EI_xy_CG,EA,EI1,EI2,angolo,GJ,minFcc,waveFcc,UM_=CSP_batch.esegui_in_batch(temp1)#@Unusedvariable
        
        #   UNITA' DI MISURA
        #   TEST O DIMENSIONAMENTO
        #   SE TEST, IN QUALI CONDIZIONI

        self.plainTextEdit.setFont(QtGui.QFont('David', 12))
        self.plainTextEdit.appendPlainText(tx)
        
     

    # END MY CODE    
    
if __name__ == "__main__":
    import sys  # @Reimport
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

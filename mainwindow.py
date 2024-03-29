from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1309, 891)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(470, 10, 20, 841))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(900, 10, 20, 841))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.selectccdropdownmenu = QtWidgets.QComboBox(self.centralwidget)
        self.selectccdropdownmenu.setGeometry(QtCore.QRect(530, 170, 241, 41))
        self.selectccdropdownmenu.setObjectName("selectccdropdownmenu")
        self.selectccdropdownmenu.addItem("")
        self.selectccdropdownmenu.addItem("")
        self.selectccdropdownmenu.addItem("")
        self.selectccdropdownmenu.addItem("")
        self.selectccdropdownmenu.addItem("")
        self.selectccdropdownmenu.addItem("")
        self.selectccdropdownmenu.addItem("")
        self.selectevstatedropdownmenu = QtWidgets.QComboBox(self.centralwidget)
        self.selectevstatedropdownmenu.setGeometry(QtCore.QRect(530, 460, 241, 41))
        self.selectevstatedropdownmenu.setObjectName("selectevstatedropdownmenu")
        self.selectevstatedropdownmenu.addItem("")
        self.selectevstatedropdownmenu.addItem("")
        self.selectevstatedropdownmenu.addItem("")
        self.selectevstatedropdownmenu.addItem("")
        self.selectevstatedropdownmenu.addItem("")
        self.selectevstatedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu = QtWidgets.QComboBox(self.centralwidget)
        self.selectthemessagedropdownmenu.setGeometry(QtCore.QRect(960, 170, 211, 41))
        self.selectthemessagedropdownmenu.setObjectName("selectthemessagedropdownmenu")
        self.selectthemessagedropdownmenu.addItem("abcd")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.selectthemessagedropdownmenu.addItem("")
        self.sendbutton = QtWidgets.QPushButton(self.centralwidget)
        self.sendbutton.setGeometry(QtCore.QRect(1080, 510, 89, 25))
        self.sendbutton.setObjectName("sendbutton")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(910, 550, 421, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.tracestextmenu = QtWidgets.QTextEdit(self.centralwidget)
        self.tracestextmenu.setGeometry(QtCore.QRect(970, 630, 311, 201))
        self.tracestextmenu.setObjectName("tracestextmenu")
        self.traceslabel = QtWidgets.QLabel(self.centralwidget)
        self.traceslabel.setGeometry(QtCore.QRect(1030, 590, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.traceslabel.setFont(font)
        self.traceslabel.setObjectName("traceslabel")
        self.selectthemessageandclickonoklabel = QtWidgets.QLabel(self.centralwidget)
        self.selectthemessageandclickonoklabel.setGeometry(QtCore.QRect(950, 120, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selectthemessageandclickonoklabel.setFont(font)
        self.selectthemessageandclickonoklabel.setObjectName("selectthemessageandclickonoklabel")
        self.okbutton = QtWidgets.QPushButton(self.centralwidget)
        self.okbutton.setGeometry(QtCore.QRect(1190, 180, 89, 25))
        self.okbutton.setObjectName("okbutton")
        self.controllerlivedatatextedit = QtWidgets.QTextEdit(self.centralwidget)
        self.controllerlivedatatextedit.setGeometry(QtCore.QRect(30, 130, 411, 701))
        self.controllerlivedatatextedit.setObjectName("controllerlivedatatextedit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(970, 240, 292, 244))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 3, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 2, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 0, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 5, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 1, 1, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout.addWidget(self.lineEdit_17, 6, 1, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout.addWidget(self.lineEdit_15, 4, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 0, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout.addWidget(self.lineEdit_18, 7, 1, 1, 1)
        self.selectthechargingcontrollerlabel = QtWidgets.QLabel(self.centralwidget)
        self.selectthechargingcontrollerlabel.setGeometry(QtCore.QRect(490, 120, 411, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selectthechargingcontrollerlabel.setFont(font)
        self.selectthechargingcontrollerlabel.setObjectName("selectthechargingcontrollerlabel")
        self.okbutton_selectchargingcontroller = QtWidgets.QPushButton(self.centralwidget)
        self.okbutton_selectchargingcontroller.setGeometry(QtCore.QRect(790, 180, 89, 25))
        self.okbutton_selectchargingcontroller.setObjectName("okbutton_selectchargingcontroller")
        self.selecttheevstatelabel = QtWidgets.QLabel(self.centralwidget)
        self.selecttheevstatelabel.setGeometry(QtCore.QRect(540, 410, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selecttheevstatelabel.setFont(font)
        self.selecttheevstatelabel.setObjectName("selecttheevstatelabel")
        self.okbutton_selectevstate = QtWidgets.QPushButton(self.centralwidget)
        self.okbutton_selectevstate.setGeometry(QtCore.QRect(790, 470, 89, 25))
        self.okbutton_selectevstate.setObjectName("okbutton_selectevstate")
        self.tracestextmenu_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.tracestextmenu_2.setGeometry(QtCore.QRect(540, 630, 311, 201))
        self.tracestextmenu_2.setObjectName("tracestextmenu_2")
        self.currentstatusofevsimulationprocesslabel = QtWidgets.QLabel(self.centralwidget)
        self.currentstatusofevsimulationprocesslabel.setGeometry(QtCore.QRect(540, 590, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.currentstatusofevsimulationprocesslabel.setFont(font)
        self.currentstatusofevsimulationprocesslabel.setObjectName("currentstatusofevsimulationprocesslabel")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 50, 1291, 26))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.controllerlivedatalabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.controllerlivedatalabel.setFont(font)
        self.controllerlivedatalabel.setObjectName("controllerlivedatalabel")
        self.gridLayout_2.addWidget(self.controllerlivedatalabel, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 3, 1, 1)
        self.evsimulationlabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.evsimulationlabel.setFont(font)
        self.evsimulationlabel.setObjectName("evsimulationlabel")
        self.gridLayout_2.addWidget(self.evsimulationlabel, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 6, 1, 1)
        self.ocppbackendlabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ocppbackendlabel.setFont(font)
        self.ocppbackendlabel.setObjectName("ocppbackendlabel")
        self.gridLayout_2.addWidget(self.ocppbackendlabel, 0, 7, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 8, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1309, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuForm = QtWidgets.QMenu(self.menubar)
        self.menuForm.setObjectName("menuForm")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuForm.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "               GUI FOR TESTING"))
        self.selectccdropdownmenu.setItemText(0, _translate("MainWindow", "Select the Charging Controller"))
        self.selectccdropdownmenu.setItemText(1, _translate("MainWindow", "CC 1"))
        self.selectccdropdownmenu.setItemText(2, _translate("MainWindow", "CC 2"))
        self.selectccdropdownmenu.setItemText(3, _translate("MainWindow", "CC 3"))
        self.selectccdropdownmenu.setItemText(4, _translate("MainWindow", "CC 4"))
        self.selectccdropdownmenu.setItemText(5, _translate("MainWindow", "CC 5"))
        self.selectccdropdownmenu.setItemText(6, _translate("MainWindow", "CC 6"))
        self.selectevstatedropdownmenu.setItemText(0, _translate("MainWindow", "Select EV-State"))
        self.selectevstatedropdownmenu.setItemText(1, _translate("MainWindow", "State \"A\""))
        self.selectevstatedropdownmenu.setItemText(2, _translate("MainWindow", "State \"B\""))
        self.selectevstatedropdownmenu.setItemText(3, _translate("MainWindow", "State \"C\""))
        self.selectevstatedropdownmenu.setItemText(4, _translate("MainWindow", "State \"D\""))
        self.selectevstatedropdownmenu.setItemText(5, _translate("MainWindow", "State \"F\""))
        self.selectthemessagedropdownmenu.setItemText(0, _translate("MainWindow", "Select the Message"))
        self.selectthemessagedropdownmenu.setItemText(1, _translate("MainWindow", "Remote Start Transaction"))
        self.selectthemessagedropdownmenu.setItemText(2, _translate("MainWindow", "Remote Stop Transaction"))
        self.selectthemessagedropdownmenu.setItemText(3, _translate("MainWindow", "Backend Availability"))
        self.selectthemessagedropdownmenu.setItemText(4, _translate("MainWindow", "Change Availability"))
        self.selectthemessagedropdownmenu.setItemText(5, _translate("MainWindow", "Clear Cache"))
        self.selectthemessagedropdownmenu.setItemText(6, _translate("MainWindow", "Extend Trigger Message"))
        self.selectthemessagedropdownmenu.setItemText(7, _translate("MainWindow", "Get Diagnostics"))
        self.selectthemessagedropdownmenu.setItemText(8, _translate("MainWindow", "Trigger Message"))
        self.selectthemessagedropdownmenu.setItemText(9, _translate("MainWindow", "Unlock Connector"))
        self.selectthemessagedropdownmenu.setItemText(10, _translate("MainWindow", "Get Configuration"))
        self.selectthemessagedropdownmenu.setItemText(11, _translate("MainWindow", "Change Configuration"))
        self.selectthemessagedropdownmenu.setItemText(12, _translate("MainWindow", "Control: FTP Server"))
        self.selectthemessagedropdownmenu.setItemText(13, _translate("MainWindow", "Update Firmware"))
        self.selectthemessagedropdownmenu.setItemText(14, _translate("MainWindow", "Set Charging Profile"))
        self.selectthemessagedropdownmenu.setItemText(15, _translate("MainWindow", "Get Composite Schedule"))
        self.selectthemessagedropdownmenu.setItemText(16, _translate("MainWindow", "Clear Charging Profile"))
        self.selectthemessagedropdownmenu.setItemText(17, _translate("MainWindow", "Reset"))
        self.selectthemessagedropdownmenu.setItemText(18, _translate("MainWindow", "Control: Get id tags"))
        self.selectthemessagedropdownmenu.setItemText(19, _translate("MainWindow", "Control: Add id tag"))
        self.sendbutton.setText(_translate("MainWindow", "Send"))
        self.traceslabel.setText(_translate("MainWindow", "Traces of the process"))
        self.selectthemessageandclickonoklabel.setText(_translate("MainWindow", "Please Select the Message and click Ok"))
        self.okbutton.setText(_translate("MainWindow", "Ok"))
        self.selectthechargingcontrollerlabel.setText(_translate("MainWindow", "Please Select the Charging Controller and click OK"))
        self.okbutton_selectchargingcontroller.setText(_translate("MainWindow", "Ok"))
        self.selecttheevstatelabel.setText(_translate("MainWindow", "Please Select the EV-State and click OK"))
        self.okbutton_selectevstate.setText(_translate("MainWindow", "Ok"))
        self.currentstatusofevsimulationprocesslabel.setText(_translate("MainWindow", "Current Status of EV-Simulation Process"))
        self.controllerlivedatalabel.setText(_translate("MainWindow", "Controller Live Data"))
        self.evsimulationlabel.setText(_translate("MainWindow", "EV-Simulation"))
        self.ocppbackendlabel.setText(_translate("MainWindow", "OCPP-Backend"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuForm.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.okbutton.clicked.connect(self.okButtonClicked)
        self.ui.sendbutton.clicked.connect(self.sendbutton_func_of_OCPP_Messages)

        #index = self.selectthemessagedropdownmenu.findText("Select the Message", QtCore.Qt.MatchFixedString)
        #self.selectthemessagedropdownmenu.setCurrentIndex(index)

    def okButtonClicked(self, Ui_MainWindow):

        print("Remote Start Transaction is selected")

        message = self.ui.selectthemessagedropdownmenu.currentText()

        if message == "Remote Start Transaction":

            send_json_data = {"msg_type": "ocpp" , "msg_id": "remote_start_transaction", "payload": {"connector_id": 1,"id_tag": 3564543423}}

            print(send_json_data)

            l1 = self.ui.lineEdit_1.setText("Message Type")
            l11 = self.ui.lineEdit_11.setText("OCPP")
            l2 = self.ui.lineEdit_2.setText("Message ID")
            l22 = self.ui.lineEdit_12.setText("Remote Start Transaction")
            l3 = self.ui.lineEdit_3.setText("Payload")
            l4 = self.ui.lineEdit_4.setText("Connector ID")
            l5 = self.ui.lineEdit_5.setText("ID Tag")

        elif message == "Remote Stop Transaction":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "remote_stop_transaction",
                "payload": {
                    "transaction_id": 77
                }
            }

        elif message == "Backend Availability":

            send_json_data = {
                "msg_type": "control",
                "msg_id": "change_backend_availability",
                "payload": {
                    "online": true
                }
            }

        elif message == "Change Availability":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "change_availability",
                "payload": {
                    "connector_id": 1,
                    "type": "Inoperative"
                }
            }

        elif message == "Clear Cache":
            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "clear_cache",
                "payload": {}
            }

        elif smessage == "Extended Trigger Message":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "extended_trigger_message",
                "payload": {
                    "connector_id": 1,
                    "requested_message": "StatusNotification"
                }
            }

        elif message == "Get Diagnostics":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "get_diagnostics",
                "payload": {
                    "location": "ftp://FT:laboratory@192.168.178.70:4563/data/ftp_server/FT/",
                    "retries": 3
                }
            }

        elif message == "Trigger Message":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "trigger_message",
                "payload": {
                    "connector_id": 0,
                    "requested_message": "StatusNotification"
                }
            }

        elif message == "Unlock Connector":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "unlock_connector",
                "payload": {
                    "connector_id": 1
                }
            }

        elif message == "Get Configuration":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "get_configuration",
                "payload": {
                    "key": [
                        "MeterValuesSampledData",
                        "AbsoluterBullshit"
                    ]
                }
            }

        elif message == "Change Configuration":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "change_configuration",
                "payload": {
                "payload": {
                    "key": "MeterValuesSampledData",
                    "value": "Energy.Active.Import.Register"
                     }
                }
            }

        elif message == "FTP Server":

            send_json_data = {
                "msg_type": "control",
                "msg_id": "configure_ftp_server",
                "payload": {
                    "status": "start",
                    "port": 4563
                }
            }

        elif message == "Update Firmware":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "update_firmware",
                "payload": {
                    "location": "ftp://FT:laboratory@192.168.178.70:4563/data/ftp_server/FT/charx-ocpp16-agent_1.2.2_RC33_arm.ipk.sig",
                    "retrieve_date": "2022-09-16T07:51:00Z"
                    }
            }

        elif message == "Set Charging Profile":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "set_charging_profile",
                "payload": {
                    "connector_id": "2",
                    "cs_charging_profiles": {
                        "charging_profile_id": 101,
                        "stack_level": 0,
                        "charging_profile_purpose": "TxProfile",
                        "charging_profile_kind": "Absolute",
                        "charging_schedule": {
                            "charging_rate_unit": "A",
                            "charging_schedule_period": {
                                "start_period": 0,
                                "limit": 16,
                                "number_phases": 3
                            }
                        }
                    }
                }
            }

        elif message == "Get Composite Schedule":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "get_composite_schedule",
                "payload": {
                    "duration": 600,
                    "connector_id": 2
                }
            }

        elif message == "Clear Charging Profile":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "clear_charging_profile",
                "payload": {}
            }

        elif message == "Reset":

            send_json_data = {
                "msg_type": "ocpp",
                "msg_id": "reset",
                "payload": {
                    "type": "Soft"
                }
            }

        elif message == "Control: Get id tags":

            send_json_data = {
                "msg_type": "control",
                "msg_id": "manage_ocpp_id_tags",
                "payload": {
                    "action": "get_all"
                }
            }

        elif message == "Control: Add id tag":

            send_json_data = {
                "msg_type": "control",
                "msg_id": "manage_ocpp_id_tags",
                "payload": {
                    "action": "add_tag",
                    "id_tag": "234565"
                }
            }

    def sendbutton_func_of_OCPP_Messages(self):

        l1 = "msg_type"
        l11 = "ocpp"
        l2 = "msg_id"
        l12 = "remote_start_transaction"
        l3 = "payload"
        l4 = "connector_id"
        l5 = "id_tag"
        l14 = self.ui.lineEdit_14.text()
        l15 = self.ui.lineEdit_15.text()

        dict_1 = {l1: l11, l2: l12, l3: {l4: l14, l5: l15}}




        l14 = int(self.ui.lineEdit_14.text())
        l15 = int(self.ui.lineEdit_15.text())

    #   dict_1 = {l1: l11, l2: l12, l3: {l4: l14, l5: l15}}
        json_string = json.dumps(dict_1)
        print(type(json_string))
        print(json_string)